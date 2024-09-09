"""Module executing the `olivaw test data` command"""

from olivaw.test.markdown import markdown_export
from olivaw.test.turtle import new_report
from .testing import data_tests, shapes_data
from olivaw.constants import DATASETS
from olivaw.test.util import print_title, save_reports, file_name

def test_data() -> None:
    """Executes the data tests over the project"""
    print_title("Running data tests")

    report, assertor = new_report("data")

    data_tests(
        DATASETS,
        report=report,
        assertor=assertor
    )

    file_base_name = file_name("data")

    print_title("Exporting results")
    save_reports(
        file_base_name,
        assertor,
        report,
        ""#markdown_export(report, file_base_name, shape_data=shapes_data)
    )
    
