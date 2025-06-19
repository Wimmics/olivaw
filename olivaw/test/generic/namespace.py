"""Module providing the namespace-validity test"""

from typing import Callable
from olivaw.constants import (
    NAMESPACE_SIMILARITY_THRESHOLD,
    GET_URIS,
    GET_NAMESPACE_USAGE,
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

from rdflib.term import Identifier

from olivaw.test.turtle import make_assertion, text_pointer, turtle_pointer
from olivaw.test.util import make_index, similar_namespace_search, COMMON_URIS_TREE
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
        uris += [(fragment['file'], term) for term in graph_uris]

    uris = list(set(uris))
    uris.sort()

    return uris

def namespace_test(
    draft: AssertDraft,
    uris: list[str],
    get_namespace_usage: Callable[[str], Identifier]
) -> None:
    """Executes the namespace test on the provided URIs

    :param draft:The assertion draft containing the useful information for reporting
    :type draft: `olivaw.test.AssertDraft`

    :param uris: The URIs that can be found in the subject
    :type uris: `list[str]`

    :param get_namespace_usage: Pointer to a function that provides the error pointer providing the usage of a URI in the subject
    :type get_namespace_usage: `typing.Callable[[str], rdflib.term.Identifier]`
    """
    if "namespace-validity" in SKIPPED_TESTS:
        return
    
    namespaces = list(set([get_prefix_suffix(uri)[0] for uri in uris]))

    datasets_prefixes = [
        (path, get_prefix_suffix(uri)[0])
        for path, uri in get_uris(DATASETS)
    ]
    datasets_prefixes_tree = make_index(datasets_prefixes)

    messages = []
    pointers = []

    for namespace in namespaces:
        similar_common = similar_namespace_search(namespace, COMMON_URIS_TREE, NAMESPACE_SIMILARITY_THRESHOLD)
        similar_uncommon = [
            (path, uri)
            for path, uri in similar_namespace_search(namespace, datasets_prefixes_tree, NAMESPACE_SIMILARITY_THRESHOLD)
            # Avoiding here all the exact matches and double matching (match between A and B and between B and A)
            if uri > namespace
        ]

        if len(similar_common) == 0 and len(similar_uncommon) == 0:
            continue

        # Testing namespace with common existing namespaces
        message = f"The following namespace seems suspicious:\n\n {namespace} \n\nWas it supposed to correspond to one of these namespaces?"
        
        namespace_pointers = [text_pointer("Namespace usage in the subject file:"), get_namespace_usage(namespace)]
        
        namespace_pointers += [
            text_pointer(f"Common namespace found \n@prefix {domain}: <{uri}> .")
            for domain, uri in similar_common
        ]

        for fragment_path, uri in similar_uncommon:
            namespace_pointers += [
                text_pointer(f"Similar namespace found in file:\n{fragment_path} \n\nNamespace found:\n{uri}"),
                turtle_pointer(
                    query_graph(
                        safe_load(fragment_path, disable_import=True, profile=OWL_RL),
                        GET_NAMESPACE_USAGE.replace("NAMESPACE", uri),
                        format=TURTLE
                    ),
                    extra_prefix_declaration=[("similar-namespace", uri)]
                )
            ]

        messages.append(message)
        pointers.append(namespace_pointers)

    make_assertion(
        draft,
        criterion="namespace-validity",
        error="namespace-typo",
        messages=messages,
        pointers=pointers,
        outcome_type="CannotTell"
    )