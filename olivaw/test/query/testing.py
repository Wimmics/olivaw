"""Module providing the business logic behind the "olivaw test query" command"""

from os.path import relpath, sep

from rdflib import BNode, Graph as RdfLibGraph

from olivaw.test.corese import Graph, QueryProcess
from olivaw.test.turtle import make_assertion, make_not_tested, make_subject, new_report, text_pointer
from olivaw.constants import SKIPPED_TESTS

from olivaw.test.query.uris import retrieveURIFromQuery

from olivaw.test.generic.namespace import namespace_test
from olivaw.test.generic.uri import uri_test
from olivaw.test.util import AssertDraft, progress_bar

def question_tests(
        queries: list[dict[str, str]],
        report: RdfLibGraph=None,
        assertor: BNode=None
    ) -> RdfLibGraph:
    """Executes the query tests over the provided subjects

    :param queries: List of representations of queries, see `~olivaw.constants.queries` for more details
    :type queries: `list[dict[str, str]]`

    :param report: Test report to use, defaults to `None` and creates a new one
    :type report: `rdflib.Graph`

    :param assertor: Assertor to use in the tests, defaults to `None` and creates a new one
    :type assertor: `rdflib.BNode`

    :returns: The test report
    :rtype: `rdflib.Graph`
    """
    if report is None or assertor is None:
        report, assertor = new_report("query")
    draft = AssertDraft(report, assertor)
    for query in progress_bar(queries):
        test_competency_question(draft, query)
    return report

def test_competency_question(draft: RdfLibGraph, query: str) -> None:
    """Executes the query tests over a provided file

    :param draft: The assertion draft containing the useful information for reporting
    :type draft: `olivaw.test.AssertDraft`

    :param file: File path leading to the file that is to be tested
    :type file: `str`
    """
    graph = Graph()
    query_process = QueryProcess.create(graph)

    query_text = ""
    with open(query["file"], "r") as query_file:
        query_text = query_file.read()

    draft(subject=make_subject(draft, [query]))

    ast = None
    messages = []

    try:
        ast = query_process.ast(query_text)
    except Exception as e:
        splitted = str(e).split("\n")[1].split(":")
        message = ":".join(splitted[3:]).strip()
        messages.append(message)

    if not "syntax" in SKIPPED_TESTS:
        make_assertion(
            draft,
            criterion="syntax",
            error="syntax-error",
            messages=messages,
            pointers=[[text_pointer(query_text)]] * len(messages)
        )

    if len(messages) > 0:
        make_not_tested(draft, "query-type", "namespace-validity", "uri-validity")
        return

    if not "query-type" in SKIPPED_TESTS:
        queryType = ""

        if ast.isSelect():
            queryType = "Select"
        elif ast.isAsk():
            queryType = "Ask"
        elif ast.isDelete():
            queryType = "Delete"
        elif ast.isInsert():
            queryType = "Insert"
        elif ast.isConstruct():
            queryType = "Construct"
        elif ast.isDescribe():
            queryType = "Describe"

        messages = []
        pointers = []

        if queryType != "Select" and queryType != "Ask":
            messages =  [f"The query type was expected to be 'Ask' or 'Select', but got '{queryType}'"]
            pointers = [[text_pointer(query_text)]]
        
        make_assertion(
            draft,
            criterion="query-type",
            error="wrong-query-type",
            messages=messages,
            pointers=pointers
        )

    if not "uri-validity" in SKIPPED_TESTS:
        query_uris = retrieveURIFromQuery(query_text)

        def get_uri_usage(_):
            return text_pointer(query_text)

        uris_valid = uri_test(draft, query_uris, get_uri_usage)

        if not uris_valid:
            make_not_tested(draft, "namespace-validity", description="All the subject URIs should conform to RFC 3986")
            return
        
    if not "namespace-validity" in SKIPPED_TESTS:    
        def get_prefix_usage(_):
            return text_pointer(query_text)
        
        namespace_test(draft, query_uris, get_prefix_usage)
    