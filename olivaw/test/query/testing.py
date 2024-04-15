from tqdm import tqdm
from os.path import relpath, sep

from olivaw.test.corese import Graph, QueryProcess
from olivaw.test.turtle import make_assertion, make_subject, make_not_tested
from olivaw.constants import PWD_TO_ROOT_FOLDER, SKIPPED_TESTS, QUIET

from olivaw.test.query.uris import retrieveURIFromQuery

from olivaw.test.generic.prefix import prefix_test
from olivaw.test.generic.uri import uri_test

def question_tests(glob_path, report, assertor):
    for query in tqdm(glob_path, disable=QUIET):
        test_competency_question(report, assertor, query)

def test_competency_question(report, assertor, file):
    graph = Graph()
    query_process = QueryProcess.create(graph)

    query = ""
    with open(file, "r") as query_file:
        query = query_file.read()

    query_key = relpath(file, PWD_TO_ROOT_FOLDER).replace(sep, "/")
    subject = make_subject(
        report,
        [query_key]
    )

    ast = None
    messages = []

    try:
        ast = query_process.ast(query)
    except Exception as e:
        messages.append(str(e).split("\n")[1].split(":")[-1].strip())

    if not "syntax" in SKIPPED_TESTS:
        make_assertion(
            report,
            assertor,
            subject,
            "syntax",
            "syntax-error",
            messages,
            pointers= [[f'"{query}"']] * len(messages)
        )

    if len(messages) > 0:
        make_not_tested(
            report,
            assertor,
            subject,
            "query-type"
        )
        make_not_tested(
            report,
            assertor,
            subject,
            "prefix-validity"
        )
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
        
        make_assertion(
            report,
            assertor,
            subject,
            "query-type",
            "wrong-query-type",
            messages,
            pointers
        )

    if not "uri-validity" in SKIPPED_TESTS:
        query_uris = retrieveURIFromQuery(query)

        def get_uri_usage(_):
            return f'"{query}"'

        uris_valid = uri_test(
            report,
            assertor,
            subject,
            query_uris,
            get_uri_usage
        )

        if not uris_valid:
            make_not_tested(
                report,
                assertor,
                subject,
                "prefix-validity"
            )
            return
        
    if not "prefix-validity" in SKIPPED_TESTS:    
        def get_prefix_usage(_):
            return query
        
        prefix_test(
            report,
            subject,
            assertor,
            query_uris,
            get_prefix_usage
        )
    