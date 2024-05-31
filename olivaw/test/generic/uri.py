"""Module responsible for the uri-validity test"""

from typing import Callable
from py4j.java_gateway import JavaObject

from olivaw.constants import SKIPPED_TESTS
from olivaw.constants.regex import URI_FORMAT
from olivaw.test.turtle import make_assertion, text_pointer
from olivaw.test.util.draft import AssertDraft

def uri_test(
        draft: AssertDraft,
        uris: list[str],
        get_uri_usage: Callable[[str], str],
        graph: JavaObject=None
    ) -> None:
    """Executes the uri-validity tests over the provided URIs

    :param draft: The assertion draft containing the useful information for reporting
    :type draft: `olivaw.test.AssertDraft`

    :param uris: List of URIs to tests
    :type uris: `list[str]`

    :param get_uri_usage: Function providing a given URI usage in the subject
    :type get_uri_usage: `Callable[[str], str]`

    :param graph: Corese graph storing the subject, defaults to `None`
    :type graph: `py4j.java_gateway.JavaObject` referencing an instance of `fr.inria.corese.core.Graph`
    """
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

    pointers = [[text_pointer(get_uri_usage(uri))] for uri in invalid_uris]

    make_assertion(
        draft,
        criterion="uri-validity",
        error="invalid-uri",
        messages=messages,
        pointers=pointers,
        graph=graph
    )

    return len(invalid_uris) == 0