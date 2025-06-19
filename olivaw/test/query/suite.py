"""Module responsible for the "olivaw test query" command"""

from os.path import abspath

from olivaw.test.markdown import markdown_export
from olivaw.test.turtle import end_activity, new_report
from .testing import question_tests
from olivaw.test.util import save_reports, print_title, file_name
from olivaw.constants import TESTED_QUERIES, SKIPPED_SUBJECTS

def test_query() -> None:
    """Executes the query tests over the current project"""
    print_title("Running query tests")

    questions = [
        item
        for item in TESTED_QUERIES
        if not abspath(item["file"]) in SKIPPED_SUBJECTS
    ]

    report, assertor = new_report("query")
    report = question_tests(
        questions,
        report=report,
        assertor=assertor
    )

    print_title("Exporting results")

    file_base_name = file_name("query")
    end_activity(report, assertor, file_base_name)

    markdown = markdown_export(report, file_base_name)

    save_reports(
        file_base_name,
        report,
        markdown
    )