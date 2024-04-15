from sys import argv
from datetime import datetime
from codecs import open as copen
from os.path import sep

from olivaw.test.corese import print_title
from olivaw.test.turtle import prepare_graph, make_assertor
from olivaw.test.markdown import make_turtle_page

from .testing import question_tests

from olivaw.constants import (
    DEV_USERNAME,
    PWD_TO_OUTPUT_FOLDER,
    COMPETENCY_QUESTIONS_GLOB_PATH,
    MODE
)

def datetime_id():
    return ".".join(
            datetime\
            .now()\
            .isoformat()\
            .split(".")[:-1]
        ).replace(":", "-")

def test_query():
    report = prepare_graph()
    assertor = make_assertor(
        report,
        f"https://github.com/Wimmics/olivaw/blob/main/olivaw/test/query/suite.py"
    )

    # MAKE QUERY TEST MAGIC HERE
    question_tests(
        COMPETENCY_QUESTIONS_GLOB_PATH,
        report,
        assertor
    )

    file_name = MODE if not MODE == "manual" else f"{MODE}-{DEV_USERNAME}-{datetime_id()}"
    file_base = f"{PWD_TO_OUTPUT_FOLDER}query-test-{file_name}"

    print_title("Exporting results")

    markdown = make_turtle_page(report, file_base.split(sep)[-1])

    with copen(f"{file_base}.ttl", "w", "utf-8") as f:
        f.write(report.serialize(format="ttl"))

    with copen(f"{file_base}.md", "w", "utf-8") as f:
        f.write(markdown)