from os.path import relpath, sep

from olivaw.test.corese import Graph, QueryProcess
from olivaw.test.turtle import make_subject, new_report
from olivaw.constants import PWD_TO_ROOT_FOLDER, SKIPPED_TESTS

from olivaw.test.query.uris import retrieveURIFromQuery

from olivaw.test.generic.prefix import prefix_test
from olivaw.test.generic.uri import uri_test
from olivaw.test.util import AssertDraft, progress_bar

def question_tests(glob_path, report=None, assertor=None):
    if report is None or assertor is None:
        report, assertor = new_report("query")
    draft = AssertDraft(report, assertor)
    for query in progress_bar(glob_path):
        test_competency_question(draft, query)
    return report

def test_competency_question(draft, file):
    graph = Graph()
    query_process = QueryProcess.create(graph)

    query = ""
    with open(file, "r") as query_file:
        query = query_file.read()

    query_key = relpath(file, PWD_TO_ROOT_FOLDER).replace(sep, "/")
    make_subject(draft, [query_key])

    ast = None
    messages = []

    try:
        ast = query_process.ast(query)
    except Exception as e:
        messages.append(str(e).split("\n")[1].split(":")[-1].strip())

    if not "syntax" in SKIPPED_TESTS:
        draft.make_assertion(
            criterion="syntax",
            error="syntax-error",
            messages=messages,
            pointers=[[f'"{query}"']] * len(messages)
        )

    if len(messages) > 0:
        draft.make_not_tested("query-type", "prefix-validity")
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
            pointers = [[f'"{query}"']]
        
        draft.make_assertion(
            criterion="query-type",
            error="wrong-query-type",
            messages=messages,
            pointers=pointers
        )

    if not "uri-validity" in SKIPPED_TESTS:
        query_uris = retrieveURIFromQuery(query)

        def get_uri_usage(_):
            return f'"{query}"'

        uris_valid = uri_test(draft, query_uris, get_uri_usage)

        if not uris_valid:
            draft.make_not_tested("prefix-validity")
            return
        
    if not "prefix-validity" in SKIPPED_TESTS:    
        def get_prefix_usage(_):
            return query
        
        prefix_test(draft, query_uris, get_prefix_usage)
    