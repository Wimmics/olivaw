from olivaw.constants import URI_FORMAT, SKIPPED_TESTS
from olivaw.test.turtle import make_assertion

def uri_test(
    report,
    assertor,
    subject,
    uris,
    get_uri_usage,
    skip_pass=False,
    tested_only=False
):
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

    make_assertion(
        report,
        assertor,
        subject,
        "uri-validity",
        "invalid-uri",
        messages,
        pointers,
        skip_pass=skip_pass,
        tested_only=tested_only
    )

    return len(invalid_uris) == 0