"""Module responsible for the "olivaw test query" command"""

from os.path import abspath

from olivaw.test.markdown import markdown_export
from .testing import question_tests
from olivaw.test.util import save_reports, print_title, file_name
from olivaw.constants import QUESTIONS_GLOB_PATH, SKIPPED_SUBJECTS

def test_query() -> None:
    """Executes the query tests over the current project"""
    questions = [
        item
        for item in QUESTIONS_GLOB_PATH
        if not abspath(item) in SKIPPED_SUBJECTS
    ]

    report = question_tests(questions)
    file_name_base = file_name("query")

    print_title("Exporting results")
    save_reports(
        file_name_base,
        report.serialize(format="ttl"),
        markdown_export(report, file_name_base)
    )