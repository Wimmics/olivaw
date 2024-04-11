from os.path import relpath, sep
from glob import glob
from requests import get
from tqdm import tqdm

from olivaw.test.corese import (
    safe_load,
    check_OWL_constraints,
    query_graph,
    TURTLE,
    OWL_RL,
    TEXT_CSV,
    TEXT_TSV
)

from olivaw.test.turtle import (
    make_subject,
    make_assertion,
    make_not_tested
)
from olivaw.constants import (
    ROOT_FOLDER,
    GET_ONTOLOGY_TERMS,
    MODULES_TTL_GLOB_PATH,
    GET_TERM_USAGE,
    GET_URIS,
    GET_PREFIX_USAGE,
    ONTOLOGY_URL,
    SKIPPED_TESTS,
    QUIET,
    DATASETS,
    CUSTOM_DATA_TESTS
)

from olivaw.test.generic.shacl import load_valid_custom_tests, custom_test
from olivaw.test.generic.prefix import prefix_test

shape_tests = load_valid_custom_tests(CUSTOM_DATA_TESTS)

def fragment_check(
    report,
    assertor,
    dataset,
    skip_pass=False,
    tested_only=False
):
    dataset_key = relpath(dataset, ROOT_FOLDER).replace(sep, "/")
    subject = make_subject(report, [dataset_key])
    graph_no_import = safe_load(dataset, disable_import=True)

    is_syntax_valid = not isinstance(graph_no_import, list)

    make_assertion(
        report,
        assertor,
        subject,
        "syntax",
        "syntax-error",
        [] if is_syntax_valid else graph_no_import,
        skip_pass=skip_pass,
        tested_only=tested_only
    )

    graph_with_import = safe_load(dataset) if is_syntax_valid else None
    is_valid = is_syntax_valid and not isinstance(graph_with_import, list)

    if not is_valid:
        make_not_tested(
            report,
            assertor,
            subject,
            "owl-rl-constraint",
            tested_only=tested_only
        )

        make_not_tested(
            report,
            assertor,
            subject,
            "term-recognition",
            tested_only=tested_only
        )
        return

    # Check for respect for OWL constraints
    if not "owl-rl-constraint" in SKIPPED_TESTS:
        constraint_violations = check_OWL_constraints(graph_with_import)
        make_assertion(
            report,
            assertor,
            subject,
            "owl-rl-constraint",
            "owl-rl-constraint-violation",
            constraint_violations,
            graph=graph_with_import,
            skip_pass=skip_pass,
            tested_only=tested_only
        )

    if len(constraint_violations) > 0:
        make_not_tested(
            report,
            assertor,
            subject,
            "term-recognition",
            tested_only=tested_only
        )
        return
    
    graph_rl = safe_load(dataset, disable_import=True, profile=OWL_RL)
    graph_no_owl = safe_load(dataset, disable_owl=True)
    
    best_practices(
        report,
        assertor,
        subject,
        dataset,
        graph_no_import,
        graph_with_import,
        graph_rl,
        skip_pass=skip_pass
    )

    custom_test(
        report,
        assertor,
        subject,
        graph_no_owl,
        shape_tests,
        skip_pass=skip_pass,
        tested_only=tested_only
    )
        

def get_ontology_terms(fragments):
    terms = []

    for fragment in fragments:
        graph = safe_load(fragment, disable_import=True)

        if isinstance(graph, list):
            continue

        graph_terms = query_graph(graph, GET_ONTOLOGY_TERMS)
        terms += [(fragment, term[1:-1]) for term in graph_terms if len(term[1:-1]) > 0]

    terms = list(set(terms))
    terms.sort()

    return terms

def data_tests(glob_path, report, assertor, skip_pass, tested_only):

    for dataset in tqdm(glob_path, disable=QUIET):
        fragment_check(
            report,
            assertor,
            dataset,
            skip_pass=skip_pass,
            tested_only=tested_only
        )

def best_practices(
        report,
        assertor,
        subject,
        file_path,
        graph_no_import,
        graph_with_import,
        graph_rl,
        skip_pass=False
    ):

    if not "term-recognition" in SKIPPED_TESTS:
        ontology_terms = list(set([term for _, term in get_ontology_terms(MODULES_TTL_GLOB_PATH)]))

        fragment_terms = query_graph(graph_rl, GET_ONTOLOGY_TERMS)
        fragment_terms = [term[1:-1] for term in fragment_terms if len(term[1:-1]) > 0]

        unknown_terms = [term for term in fragment_terms if not term in ontology_terms]
        messages = [
            'Some fragment terms are in ontology namespace but not defined in ontology'
        ] if len(unknown_terms) > 0 else []

        pointers = [[
            item
            for term in unknown_terms
            for item in [
                query_graph(
                    graph_rl,
                    GET_TERM_USAGE.replace("TERM", f"{ONTOLOGY_URL}{term}"),
                    format=TURTLE
                ).strip()
            ]
        ]] if len(unknown_terms) > 0 else []

        make_assertion(
            report,
            assertor,
            subject,
            "term-recognition",
            "unknown-term",
            messages=messages,
            pointers=pointers,
            graph=graph_rl,
            skip_pass=skip_pass
        )

    if not "prefix-validity" in SKIPPED_TESTS:
        uris = query_graph(graph_rl, GET_URIS, format=TEXT_CSV)
        
        def get_prefix_usage(prefix):
            return query_graph(
                graph_rl,
                GET_PREFIX_USAGE.replace("PREFIX", prefix),
                format=TURTLE
            )
        
        prefix_test(
            report,
            subject,
            assertor,
            uris,
            get_prefix_usage,
            skip_pass=skip_pass
        )