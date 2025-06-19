"""Module responsible for the business logic behind the `olivaw test data` command"""

from os.path import relpath, sep

from rdflib import BNode, Graph

from olivaw.constants.sparql import GET_DECLARED_ONTOLOGIES
from olivaw.test.corese import (
    safe_load,
    check_OWL_constraints,
    query_graph,
    TURTLE,
    OWL_RL,
    TEXT_CSV
)

from olivaw.constants import (
    MODULES,
    GET_ONTOLOGY_TERMS,
    GET_TERM_USAGE,
    GET_URIS,
    GET_NAMESPACE_USAGE,
    ONTOLOGY_NAMESPACE,
    SKIPPED_TESTS,
    CUSTOM_DATA_TESTS
)

from olivaw.test.turtle import make_assertion, make_not_tested, make_subject, new_report, text_pointer, turtle_pointer
from olivaw.test.generic.shacl import load_valid_custom_tests, custom_test
from olivaw.test.generic.namespace import namespace_test
from olivaw.test.util import progress_bar, AssertDraft

from py4j.java_gateway import JavaObject

shape_tests, shape_data = load_valid_custom_tests(CUSTOM_DATA_TESTS)

ONTOLOGIES: dict[str, str] = {}
""""Dictionary `dict[str, str]` linking each project ontology URI as `str` to a give module absolute file path as `str` it corresponds to"""

for module in MODULES:
    try:
        g = Graph()
        g.parse(module["file"])
        found_ontologies = [
            str(ontology[0])
            for ontology
            in g.query(GET_DECLARED_ONTOLOGIES)
        ]
        ontologies = {**ontologies, **{ontology: module for ontology in found_ontologies}}
    except:
        continue

def fragment_check(draft: AssertDraft, dataset: dict[str, str]) -> None:
    """Executes a data test over a data fragment

    :param draft: The assertion draft containing the useful information for reporting
    :type draft: `olivaw.test.AssertDraft`

    :param dataset: Dictionary reprenting the data fragment to be tested, see `~olivaw.constants.DATASETS` for more details
    :type dataset: `dict[str, str]`
    """
    draft(subject=make_subject(draft, [dataset]))
    graph_no_import = safe_load(dataset, disable_import=True)

    is_syntax_valid = not isinstance(graph_no_import, list)

    make_assertion(
        draft,
        criterion="syntax",
        error="syntax-error",
        messages=[] if is_syntax_valid else [
            message\
                .replace("\\r", "")\
                .replace("\\n", "\n")
            for message in graph_no_import
        ]
    )

    graph_with_import = safe_load(dataset, ontologies=ONTOLOGIES) if is_syntax_valid else None
    is_valid = is_syntax_valid and not isinstance(graph_with_import, list)

    if not is_valid:
        make_not_tested(draft, "owl-rl-constraint", "term-recognition", "namespace-validity")
        make_not_tested(draft(custom_test_data=shape_data), *list(shape_data.keys()))
        return

    constraint_violations = []
    
    # Check for respect for OWL constraints
    if not "owl-rl-constraint" in SKIPPED_TESTS:
        constraint_violations = check_OWL_constraints(graph_with_import)
        make_assertion(
            draft,
            criterion="owl-rl-constraint",
            error="owl-rl-constraint-violation",
            messages=constraint_violations,
            graph=graph_with_import
        )

    if len(constraint_violations) > 0:
        make_not_tested(draft(criterion="term-recognition"))
        return
    
    graph_rl = safe_load(dataset, disable_import=True, profile=OWL_RL)
    graph_no_owl = safe_load(dataset, disable_owl=True)
    
    best_practices(draft, graph_rl)
    custom_test(draft, graph_no_owl,shape_tests)
        

def get_ontology_terms(fragments: list[dict[str, str]]) -> list[str]:
    """Get all the terms that are defined in the ontology

    :param fragments: List of presentations of project RDF resources, see `~olivaw.constants.MODULES`, `~olivaw.constants.MODELETS`, `~olivaw.constants.DATASETS` and `~olivaw.constants.USE_CASES` for more details
    :type fragments: `list[dict[str, str]]`

    :returns: The list of the ontology terms URIs
    :rtype: `list[str]`
    """
    terms = []

    for fragment in fragments:
        graph = safe_load(fragment, disable_import=True)

        if isinstance(graph, list):
            continue

        graph_terms = query_graph(graph, GET_ONTOLOGY_TERMS)
        terms += [(fragment['file'], term[1:-1]) for term in graph_terms if len(term[1:-1]) > 0]

    terms = list(set(terms))
    terms.sort()

    return terms

def data_tests(data_fragments: list[str], report: Graph=None, assertor: BNode=None) -> None:
    """Execute a data test on each data fragment passed as input

    :param data_fragments: List of all the data fragments to be tested
    :type data_fragments: `list[str]`

    :param report: Test report to use for the tests to be run, defaults to `None` and create a new one
    :type report: `rdflib.Graph`, optional

    :param assertor: Test assertor to use in the test, defaults to `None` and create a new one
    :type assertor: `rdflib.BNode`, optional
    """
    if report is None or assertor is None:
        report, assertor = new_report("data")

    draft = AssertDraft(report, assertor)

    for dataset in progress_bar(data_fragments):
        fragment_check(draft, dataset)

    return report

def best_practices(draft: AssertDraft, graph_rl: JavaObject) -> None:
    """Executes the data best practices tests over the Corese graph passed as input

    :param draft: The assertion draft containing the useful information for reporting
    :type draft: `olivaw.test.AssertDraft`

    :param graph_rl: The Corese graph containing the data fragment
    :type graph_rl: `py4j.java_gateway.JavaObject` referencing an instance of `fr.inria.corese.core.Graph`
    """
    if not "term-recognition" in SKIPPED_TESTS:
        ontology_terms = list(set([term for _, term in get_ontology_terms(MODULES)]))

        fragment_terms = query_graph(graph_rl, GET_ONTOLOGY_TERMS)
        fragment_terms = [term[1:-1] for term in fragment_terms if len(term[1:-1]) > 0]

        unknown_terms = [term for term in fragment_terms if not term in ontology_terms]

        messages = [
            'Some fragment terms are in ontology namespace but not defined in ontology'
        ] if len(unknown_terms) > 0 else []

        pointers = [
            [
                item
                for couple in zip(
                    [
                        text_pointer(f'Term not recognized: <{ONTOLOGY_NAMESPACE}{term}>')
                        for term in unknown_terms
                    ],
                    [
                        turtle_pointer(
                            query_graph(
                                graph_rl,
                                GET_TERM_USAGE.replace("TERM", f"{ONTOLOGY_NAMESPACE}{term}"),
                                format=TURTLE
                            ).strip(),
                            [("", ONTOLOGY_NAMESPACE)]
                        )
                        for term in unknown_terms
                    ]
                )
                for item in couple
            ]
        ] if len(unknown_terms) > 0 else []

        make_assertion(
            draft,
            criterion="term-recognition",
            error="unknown-term",
            messages=messages,
            pointers=pointers,
            graph=graph_rl
        )

    if not "namespace-validity" in SKIPPED_TESTS:
        uris = query_graph(graph_rl, GET_URIS, format=TEXT_CSV)
        
        def get_namespace_usage(prefix):
            return turtle_pointer(
                query_graph(
                    graph_rl,
                    GET_NAMESPACE_USAGE.replace("NAMESPACE", prefix),
                    format=TURTLE
                )
            )

        namespace_test(draft, uris, get_namespace_usage)