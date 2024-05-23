"""Module responsible for the "olivaw test data" command"""

from olivaw.test.markdown import markdown_export
from .testing import data_tests, shapes_data
from olivaw.constants import DATASETS
from olivaw.test.util import print_title, save_reports, file_name

def test_data():
    print_title("Running data tests")
    report = data_tests(DATASETS)

    file_base_name = file_name("data")

    print_title("Exporting results")
    save_reports(
        file_base_name,
        report.serialize(format="ttl"),
        markdown_export(report, file_base_name, shape_data=shapes_data)
    )
    
