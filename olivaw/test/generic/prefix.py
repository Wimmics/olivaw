from olivaw.constants import (
    similar_prefix_search,
    COMMON_URIS_TREE,
    PREFIX_SIMILARITY_THRESHOLD,
    GET_URIS,
    make_index,
    GET_PREFIX_USAGE,
    DATASETS
)

from olivaw.test.corese import (
    safe_load,
    query_graph,
    TEXT_CSV,
    TURTLE,
    OWL_RL
)

from olivaw.test.turtle import (
    make_assertion
)

def get_prefix_suffix(uri):

    for i in range(len(uri) - 1, 0, -1):
        if uri[i] in ["#", "/", ":", "="]:
            return uri[:i+1], uri[i+1:]
        
    return uri, ""

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

def prefix_test(
    report,
    subject,
    assertor,
    uris,
    get_prefix_usage,
    skip_pass=False
):
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