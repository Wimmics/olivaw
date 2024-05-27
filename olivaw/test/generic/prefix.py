"""Module providing the prefix-validity test"""

from typing import Callable
from olivaw.constants import (
    PREFIX_SIMILARITY_THRESHOLD,
    GET_URIS,
    GET_PREFIX_USAGE,
    DATASETS,
    SKIPPED_TESTS
)

from olivaw.test.corese import (
    safe_load,
    query_graph,
    TEXT_CSV,
    TURTLE,
    OWL_RL
)

from olivaw.test.turtle import make_assertion
from olivaw.test.util import make_index, similar_prefix_search, COMMON_URIS_TREE
from olivaw.test.util.draft import AssertDraft

def get_prefix_suffix(uri: str) -> tuple[str, str]:
    """Returns the namespace and the suffix related to the given URI

    :param uri: The URI to analyze
    :type uri: `str`

    :returns: The namespace and the suffix of that URI
    :rtype: `tuple[str, str]`
    """
    for i in range(len(uri) - 1, 0, -1):
        if uri[i] in ["#", "/", ":", "="]:
            return uri[:i+1], uri[i+1:]
        
    return uri, ""

def get_uris(fragments: list[str]) -> list[str]:
    """Retrieves all the URIs that can be found in a set of fragments

    :param fragments: List of files paths to retrieve URIs
    :type fragments: `list[str]`

    :returns: A list of URIs that can be found in the fragments
    :rtype: `list[str]`
    """
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

def prefix_test(
    draft: AssertDraft,
    uris: list[str],
    get_prefix_usage: Callable[[str], str]
) -> None:
    """Executes the prefix test on the provided URIs

    :param draft:The assertion draft containing the useful information for reporting
    :type draft: `olivaw.test.AssertDraft`

    :param uris: The URIs that can be found in the subject
    :type uris: `list[str]`

    :param get_prefix_usage: Pointer to a function that provides the usage of a URI in the subject
    :type get_prefix_usage: `typing.Callable[[str], str]`
    """
    if "prefix-validity" in SKIPPED_TESTS:
        return
    
    prefixes = list(set([get_prefix_suffix(uri)[0] for uri in uris]))

    datasets_prefixes = [
        (path, get_prefix_suffix(uri)[0])
        for path, uri in get_uris(DATASETS)
    ]
    datasets_prefixes_tree = make_index(datasets_prefixes)

    messages = []
    pointers = []

    for prefix in prefixes:
        similar_common = similar_prefix_search(prefix, COMMON_URIS_TREE, PREFIX_SIMILARITY_THRESHOLD)
        similar_uncommon = [
            (path, uri)
            for path, uri in similar_prefix_search(prefix, datasets_prefixes_tree, PREFIX_SIMILARITY_THRESHOLD)
            # Avoiding here all the exact matches and double matching (match between A and B and between B and A)
            if uri > prefix
        ]

        if len(similar_common) == 0 and len(similar_uncommon) == 0:
            continue

        # Testing prefixes with common existing prefixes
        message = f"The prefix {prefix} seems suspicious. Did you mean one of these prefixes?"
        
        prefix_pointers = [f'"Prefix usage in the subject file:\n\n\n {get_prefix_usage(prefix)}"']
        
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
        draft(
            criterion="prefix-validity",
            error="prefix-typo",
            messages=messages,
            pointers=pointers,
            outcome_type="CannotTell"
        )
    )