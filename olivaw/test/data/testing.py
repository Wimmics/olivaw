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
    SKIPPED_TESTS
)

from olivaw.constants.prefixcc import (
    COMMON_URIS_TREE,
    PREFIX_SIMILARITY_THRESHOLD,
    similar_prefix_search,
    make_index
)

# Checking most common prefixes
response = get("https://prefix.cc/context")
common_prefixes = response.json()["@context"]

def fragment_check(
    datasets,
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
    
    best_practices(
        datasets,
        report,
        assertor,
        subject,
        dataset,
        graph_no_import,
        graph_with_import,
        graph_rl,
        skip_pass=skip_pass
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

def get_uris(fragments):
    uris = []

    for fragment in fragments:
        graph = safe_load(fragment, disable_import=True)

        if isinstance(graph, list):
            continue

        graph_uris = query_graph(graph, GET_URIS, format=TEXT_CSV)
        uris += [(fragment, term) for term in graph_uris]

    uris = list(set(uris))
    uris.sort()

    return uris

def data_fragment_test(report, assertor, datasets, skip_pass, tested_only):

    for dataset in tqdm(datasets):
        fragment_check(
            datasets,
            report,
            assertor,
            dataset,
            skip_pass=skip_pass,
            tested_only=tested_only
        )


def get_prefix_suffix(uri):

    for i in range(len(uri) - 1, 0, -1):
        if uri[i] in ["#", "/", ":", "="]:
            return uri[:i+1], uri[i+1:]
        
    return uri, ""

def best_practices(
        datasets,
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
        modules = glob(MODULES_TTL_GLOB_PATH)
        ontology_terms = list(set([term for _, term in get_ontology_terms(modules)]))

        fragment_terms = query_graph(graph_rl, GET_ONTOLOGY_TERMS)
        fragment_terms = [term[1:-1] for term in fragment_terms if len(term[1:-1]) > 0]

        unknown_terms = [term for term in fragment_terms if not term in ontology_terms]
        messages = [f'The term "{term}" was used in the fragment but not defined in the ontology' for term in unknown_terms]
        pointers = [
            [
                query_graph(
                    graph_rl,
                    GET_TERM_USAGE.replace("TERM", f"{ONTOLOGY_URL}{term}"),
                    format=TURTLE
                ).strip()
            ]
            for term in unknown_terms
        ]

        make_assertion(
            report,
            assertor,
            subject,
            "term-recognition",
            "unknown-term",
            messages=messages,
            pointers=pointers,
            skip_pass=skip_pass
        )

    if not "prefix-validity" in SKIPPED_TESTS:
        uris = query_graph(graph_rl, GET_URIS, format=TEXT_CSV)
        prefixes = list(set([get_prefix_suffix(uri)[0] for uri in uris]))

        all_prefixes = [
            (path, get_prefix_suffix(uri)[0])
            for path, uri in get_uris(datasets)
        ]
        all_prefixes_tree = make_index(all_prefixes)

        messages = []
        pointers = []

        for prefix in prefixes:
            similar_common = similar_prefix_search(prefix, COMMON_URIS_TREE, PREFIX_SIMILARITY_THRESHOLD)
            similar_uncommon = [
                (path, uri)
                for path, uri in similar_prefix_search(prefix, all_prefixes_tree, PREFIX_SIMILARITY_THRESHOLD)
                # Avoiding here all the double matching on the test scale (match between A and B and between B and A)
                if uri > prefix
            ]

            if len(similar_common) == 0 and len(similar_uncommon) == 0:
                continue

            # Testing prefixes with common existing prefixes
            message = f"The prefix {prefix} seems suspicious. Did you mean one of these prefixes?"
            
            prefix_pointers = [
                '"Prefix usage in the subject file:\n\n\n' + query_graph(
                    graph_rl,
                    GET_PREFIX_USAGE.replace("PREFIX", prefix),
                    format=TURTLE) + '"'
                ]
            
            prefix_pointers += [
                f'"Common prefix found \n@prefix {domain}: <{uri}> ."'
                for domain, uri in similar_common
            ]

            for fragment_path, uri in similar_uncommon:
                prefix_pointers += [
                    f'"Similar prefix found in file {fragment_path}\nPrefix found: {uri}\n\n' +
                    query_graph(
                        safe_load(fragment_path, disable_import=True, profile=OWL_RL),
                        GET_PREFIX_USAGE.replace("PREFIX", uri),
                        format=TURTLE) + '"'
                ]
            
            messages.append(message)
            pointers.append(prefix_pointers)

        make_assertion(
            report,
            assertor,
            subject,
            "prefix-validity",
            "prefix-typo",
            messages=messages,
            pointers=pointers,
            outcome_type="CannotTell",
            skip_pass=skip_pass
        )