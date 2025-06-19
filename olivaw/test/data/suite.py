"""Module executing the `olivaw test data` command"""

from olivaw.test.markdown import markdown_export
from olivaw.test.turtle import end_activity, new_report
from olivaw.constants import TESTED_DATASETS, TESTED_USECASES
from olivaw.test.util import print_title, save_reports, file_name
from .testing import data_tests, shape_data

def test_data() -> None:
    """Executes the data tests over the project"""
    print_title("Running data tests")

    report, assertor = new_report("data")

    data_tests(
        TESTED_DATASETS + TESTED_USECASES,
        report=report,
        assertor=assertor
    )

    print_title("Exporting results")

    file_base_name = file_name("data")
    end_activity(report, assertor, file_base_name)

    markdown = markdown_export(report, file_base_name, shape_data=shape_data)

    save_reports(
        file_base_name,
        report,
        markdown
    )
    
