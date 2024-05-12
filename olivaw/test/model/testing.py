from os.path import sep, relpath

from olivaw.constants.sparql import LINK_SUBJECTS_FOR_MODULE, REMOVE_DESCRIPTION_LINKS
from olivaw.test.corese import (
    query_graph, 
    safe_load,
    OWLProfile,
    check_OWL_constraints,
    profile_errors
)
from olivaw.constants import (
    GET_BY_MODULE,
    DECIDABILITY_RANGE,
    PWD_TO_ROOT_FOLDER,
    MODEL_BEST_PRACTICES_TESTS,
    MODEL_BEST_PRACTICES_TESTS,
    CUSTOM_MODEL_TESTS,
    MODULES_TTL_GLOB_PATH,
    GET_DECLARED_ONTOLOGIES,
    TRIPLES_FOR_MODULE
)

from olivaw.test.model.best_practices import best_practices_test

from olivaw.test.generic.shacl import (
    custom_test,
    load_valid_custom_tests
)

from rdflib import Graph as RdflibGraph

from olivaw.test.turtle import make_assertion, make_not_tested, make_subject
from olivaw.test.util import AssertDraft, progress_bar

shape_tests, shape_data = load_valid_custom_tests(CUSTOM_MODEL_TESTS)
ontologies = {}

for module in MODULES_TTL_GLOB_PATH:
    try:
        g = RdflibGraph()
        g.parse(module)
        found_ontologies = [
            str(ontology[0])
            for ontology
            in g.query(GET_DECLARED_ONTOLOGIES)
        ]
        ontologies = {**ontologies, **{ontology: module for ontology in found_ontologies}}
    except:
        continue

def group_terms_by_module(modelet):
    """Get all the triples that has a subject included in the ontology.
    Group all of these triples by module (using rdfs:isDefinedBy property)

    :param modelet: Corese graph containing the modelet
    :returns: A dictionary of n3 for each module to be merged with the given n3
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

def profile_check(fragment, draft):
    """Returns a report about whether an ontology is compatible with each profile and if not, why

    :param ontology: Corese graph containing the modelet
    :param extra: string in n3 notation, additional triples to add to the graph
    :returns: A dictionary with a key for each profile containing itself another dictionary
    with a key "is_reached" mapping a boolean indicating a compatibility, and a "message" justifying the result
    """

    engine = OWLProfile(fragment)
    draft(criterion="profile-compatibility", graph=fragment)

    packed_errors = []
    packed_messages = []
    packed_pointers = []

    for decidability_level in DECIDABILITY_RANGE:
        if draft.should_skip():
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
                    pointers[i][0]
                    for i in range(len(pointers))
                    if messages[i] == message
                ]
                for message in distinct_messages
            ]

        packed_errors.append(error_id)
        packed_messages.append(distinct_messages)
        packed_pointers.append(grouped_pointers)
    
    if not draft.should_skip():
        make_assertion(
            draft(
                error=packed_errors,
                messages=packed_messages,
                pointers=packed_pointers
            )
        )

    # Check for respect for OWL constraints
    if not draft.should_skip(criterion="owl-rl-constraint"):
        make_assertion(
            draft(
                error="owl-rl-constraint-violation",
                messages=check_OWL_constraints(fragment)
            )
        )

def fragment_check(fragments, draft, extras=""):
    fragment_no_import = safe_load(
        fragments,
        extras,
        disable_import=True
    )
    no_import_load_error = isinstance(fragment_no_import, list)

    draft(criterion="syntax", error="syntax-error")

    if no_import_load_error:
        make_assertion(
            draft(
                messages=["The subject has turtle syntax errors that makes it unprocessable by an engine"],
                pointers=[[f'"{pointer}"' for pointer in fragment_no_import]]
            )
        )
        make_not_tested(draft, *MODEL_BEST_PRACTICES_TESTS)
        return True
    
    fragment_with_import = safe_load(fragments, extras)
    with_import_load_error = isinstance(fragment_with_import, list)

    profile_check(fragment_no_import, draft)

    if with_import_load_error:
        draft.make_not_tested(*MODEL_BEST_PRACTICES_TESTS)
        return True
    
    fragment_no_owl = safe_load(fragments, extras, disable_owl=True)

    best_practices_test(
        draft,
        fragment_no_import,
        fragment_no_owl,
    )

    custom_test(draft, fragment_no_owl, shape_tests)
    
    return False

def modules_tests(modules, report=None, assertor=None):
    """Returns a report about of a profile check of a set of ontologies

    :param glob_path: A glob-format path string
    :returns: A dictionary of reports, the keys are the file paths
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

def modelets_tests(modelets, report=None, assertor=None):
    """Test of the modelets
    Test them individually, and then checks how each module behave
    when merged with their related terms in the modelets

    :param glob_path: A glob-format path string
    :returns: A dictionary of reports
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

            if draft.should_skip(file=[modelet, module_key]):
                continue

            make_subject(draft, [module_path], [modelet_key])

            fragment_check(
                module_path,
                draft,
                extras=moduled_triples[module]
            )

    return safe_modelets

def merged_fragment_set_test(
        report,
        assertor,
        fragments_to_merge,
        heart_name,
        custom_title=""
    ):
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
