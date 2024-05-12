from olivaw.constants import URI_FORMAT, SKIPPED_TESTS

def uri_test(draft, uris, get_uri_usage, graph=None):
    if "uri-validity" in SKIPPED_TESTS:
        return
    
    invalid_uris = [
        uri
        for uri in uris
        if len(URI_FORMAT.findall(uri)) == 0
    ]

    messages = [
        f"Expected valid URIs in subject but got: {uri}"
        for uri in invalid_uris
    ]

    pointers = [[get_uri_usage(uri)] for uri in uris]

    draft.make_assertion(
        criterion="uri-validity",
        error="invalid-uri",
        messages=messages,
        pointers=pointers,
        graph=graph
    )

    return len(invalid_uris) == 0