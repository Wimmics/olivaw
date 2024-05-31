"""Module providing the business logic behind the `olivaw test model` command"""

from os.path import sep, relpath
from typing import Union
from py4j.java_gateway import JavaObject

from olivaw.constants.sparql import LINK_SUBJECTS_FOR_MODULE, REMOVE_DESCRIPTION_LINKS
from olivaw.test.corese import (
    query_graph, 
    safe_load,
    OWLProfile,
    check_OWL_constraints,
    profile_errors,
    ontologies
)
from olivaw.constants import (
    GET_BY_MODULE,
    DECIDABILITY_RANGE,
    PWD_TO_ROOT_FOLDER,
    MODEL_BEST_PRACTICES_TESTS,
    MODEL_BEST_PRACTICES_TESTS,
    CUSTOM_MODEL_TESTS,
    TRIPLES_FOR_MODULE
)

from olivaw.test.model.best_practices import best_practices_test

from olivaw.test.generic.shacl import (
    custom_test,
    load_valid_custom_tests
)

from olivaw.test.turtle import (
    make_assertion,
    make_not_tested,
    make_subject,
    text_pointer,
    turtle_pointer
)

from olivaw.test.util import AssertDraft, progress_bar

from rdflib import Graph, BNode

from olivaw.test.util.skip import should_skip

shape_tests, shape_data = load_valid_custom_tests(CUSTOM_MODEL_TESTS)

def group_terms_by_module(modelet: JavaObject) -> dict[str, str]:
    """Get all the triples that has a subject included in the ontology.
    Group all of these triples by module (using rdfs:isDefinedBy property)

    :param modelet: Corese graph containing the modelet
    :type modelet: `py4j.java_gateway.JavaObject` referencing an instance of `fr.inria.corese.core.Graph`

    :returns: A dictionary that links a module to some modelet turtle data
    :rtype: `dict[str, str]`
    """
    tsv = [
        ontology
        for ontology
        in query_graph(modelet, GET_BY_MODULE)
    ]

    grouped_triples = {}

    for line in tsv:
        module = line[1:-1]
        
        query_graph(modelet, LINK_SUBJECTS_FOR_MODULE.replace("MODULE", line))
        triple = query_graph(modelet, TRIPLES_FOR_MODULE.replace("MODULE", line))
        query_graph(modelet, REMOVE_DESCRIPTION_LINKS)

        triple = "\n".join(triple)

        if not module in grouped_triples:
            grouped_triples[module] = triple
        else:
            grouped_triples[module] += "\n" + triple

    return grouped_triples

def profile_check(fragment: JavaObject, draft: AssertDraft) -> None:
    """Executes the profile-compatibility tests over the provided fragment

    :param fragment: Corese fgraph containing the fragment to be tested
    :type fragment: `py4j.java_gateway.JavaObject` referencing an instance of `fr.inria.corese.core.Graph`

    :param draft: The assertion draft containing the useful information for reporting
    :type draft: `olivaw.test.AssertDraft`
    """

    engine = OWLProfile(fragment)
    draft(criterion="profile-compatibility", graph=fragment)

    packed_errors = []
    packed_messages = []
    packed_pointers = []

    for decidability_level in DECIDABILITY_RANGE:
        if should_skip(draft):
            break

        # Keeping 2 arrays containing almost the same thing was not necessary, so getattr
        profile = getattr(OWLProfile, decidability_level)
        compatible = engine.process(profile)
        raw_message = engine.getMessage()
        engine.setMessage("")
        error_id = f"{decidability_level.lower().replace('_', '-')}-profile-error"
        distinct_messages, grouped_pointers = [], []
        if not compatible:
            messages, pointers = profile_errors(raw_message)
            distinct_messages = list(set(messages))
            grouped_pointers = [
                [
                    turtle_pointer(pointers[i][0])
                    for i in range(len(pointers))
                    if messages[i] == message
                ]
                for message in distinct_messages
            ]

        packed_errors.append(error_id)
        packed_messages.append(distinct_messages)
        packed_pointers.append(grouped_pointers)
    
    if not should_skip(draft):
        make_assertion(
            draft(
                error=packed_errors,
                messages=packed_messages,
                pointers=packed_pointers
            )
        )

    # Check for respect for OWL constraints
    if not should_skip(draft, criterion="owl-rl-constraint"):
        make_assertion(
            draft,
            error="owl-rl-constraint-violation",
            messages=check_OWL_constraints(fragment)
        )

def fragment_check(fragments, draft, extras="") -> bool:
    """Executes the model tests over the files and extra turtle data passed as input

    :param fragments: List of paths of files that are the parts of the subject
    :type fragments: `list[str]`

    :param draft: The assertion draft containing the useful information for reporting
    :type draft: `olivaw.test.AssertDraft`

    :param extras: Extra turtle data to inject into the subject, defaults to `""`
    :type extras: `str`, optional

    :returns: Boolean stating if the fragment can be used in further aggregated graph tests
    :rtype: `bool`
    """
    fragment_no_import = safe_load(
        fragments,
        extras,
        disable_import=True
    )
    no_import_load_error = isinstance(fragment_no_import, list)

    draft(criterion="syntax", error="syntax-error")

    if no_import_load_error:
        make_assertion(
            draft,
            messages=["The subject has turtle syntax errors that makes it unprocessable by an engine"],
            pointers=[[text_pointer(pointer) for pointer in fragment_no_import]]
        )
        make_not_tested(draft, *MODEL_BEST_PRACTICES_TESTS)
        make_not_tested(draft(custom_test_data=shape_data), *list(shape_data.keys()))
        return True
    
    fragment_with_import = safe_load(fragments, extras)
    with_import_load_error = isinstance(fragment_with_import, list)

    profile_check(fragment_no_import, draft)

    if with_import_load_error:
        make_not_tested(draft, *MODEL_BEST_PRACTICES_TESTS)
        make_not_tested(draft(custom_test_data=shape_data), *list(shape_data.keys()))
        return True
    
    fragment_no_owl = safe_load(fragments, extras, disable_owl=True)

    best_practices_test(
        draft,
        fragment_no_import,
        fragment_no_owl,
    )

    custom_test(draft, fragment_no_owl, shape_tests)
    
    return False

def modules_tests(modules: list[str], report: Graph=None, assertor: BNode=None) -> list[str]:
    """Apply the modules test on the provided modules and write the result in the provided report

    :param modules: A list of module paths to test
    :type modules: `list[str]`

    :params report: the report where the results will be written, defaults to `None`
    :type report: `rdflib.Graph`, optional
    
    :params assertor: the assertor of this test, defaults to `None`
    :type assertor: `rdflib.URIRef`

    :return: The list of the module paths that can be used in further aggregated graph tests
    :rtype: `list[str]`
    """
    if len(modules) == 0:
        return []
    
    safe_modules = []

    draft = AssertDraft(report, assertor)

    for module in progress_bar(modules):
        module_key = relpath(module, PWD_TO_ROOT_FOLDER).replace(sep, "/")
        draft(file=module)
        draft(subject=make_subject(draft, [module_key]))
        load_error = fragment_check(module, draft)

        if not load_error:
            safe_modules.append(module)

    return safe_modules

def modelets_tests(modelets, report: Graph=None, assertor: BNode=None) -> list[str]:
    """Executes the tests related to modelets on the provided modelets

    :param modelets: List of modelets paths to test
    :type modelets: `list[str]`

    :param report: Test report to use, defaults to `None` and creating a new one
    :type report: `rdflib.Graph`, optional

    :param assertor: Assertor to use for report, defaults to `None` and creating a new one
    :type assertor: `rdflib.BNode`, optional

    :returns: The list of the modelet paths that can be used in further aggregated graph tests
    :rtype: list[str]
    """
    if len(modelets) == 0:
        return []

    safe_modelets = []

    draft = AssertDraft(report, assertor)

    for modelet in progress_bar(modelets):
        if "template" in modelet:
            continue

        modelet_key = relpath(modelet, PWD_TO_ROOT_FOLDER).replace(sep, "/")
        draft(subject=make_subject(draft, [modelet_key]))

        load_error = fragment_check(
            modelet,
            draft(file=modelet)
        )

        if load_error:
            continue
        else:
            safe_modelets.append(modelet)
        
        # Add each triple of the modelet to their related ontology, then proceed to profile checks
        alone_no_owl = safe_load(modelet, disable_owl=True)

        moduled_triples = group_terms_by_module(alone_no_owl)

        for module in moduled_triples.keys():
            if not module in ontologies:
                continue

            module_path = ontologies[module].replace(sep, "/")
            module_key = relpath(module_path, PWD_TO_ROOT_FOLDER).replace(sep, "/")

            if module_path.startswith("./"):
                module_path = module_path[2:]

            if should_skip(draft, file=[modelet, module_key]):
                continue

            draft(subject=make_subject(draft, [module_path], [modelet_key]))

            fragment_check(
                module_path,
                draft,
                extras=moduled_triples[module]
            )

    return safe_modelets

def merged_fragment_set_test(
        report: Graph,
        assertor: BNode,
        fragments_to_merge: list[str],
        heart_name: str,
        custom_title: str=""
    ) -> None:
    """Executes the model tests in an aggregation of ontology fragments
    
    :param report: The test report to use
    :type report: `rdflib.Graph`

    :param fragments_to_merge: List of paths to files to include in the test subject
    :type fragments_to_merge: `list[str]`

    :param heart_name: Identifier to attribute to the subject
    :type heart_name: `str`

    :param custom_title: Custom title to give to the subject, defaults to `""` and computes a title
    :type custom_title: `str`
    """
    fragments_keys = [
        relpath(fragment, PWD_TO_ROOT_FOLDER).replace(sep, "/")
        for fragment in fragments_to_merge
    ]

    if len(fragments_keys) == 0:
        return

    draft = AssertDraft(report, assertor, file=fragments_to_merge)
    
    draft(subject=make_subject(
        draft,
        fragments_keys,
        name=heart_name,
        custom_title=custom_title
    ))
        
    fragment_check(fragments_to_merge, draft)
