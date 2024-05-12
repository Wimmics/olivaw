from os.path import abspath
from .testing import question_tests
from olivaw.test.util import save_reports, print_title
from olivaw.constants import QUESTIONS_GLOB_PATH, SKIPPED_SUBJECTS

def test_query():
    questions = [
        item
        for item in QUESTIONS_GLOB_PATH
        if not abspath(item) in SKIPPED_SUBJECTS
    ]
    report = question_tests(questions)

    print_title("Exporting results")
    save_reports("query", report)