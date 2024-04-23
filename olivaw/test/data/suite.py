from .testing import data_tests
from olivaw.constants import DATASETS
from olivaw.test.util import print_title, save_reports

def test_data():
    print_title("Running data tests")
    report = data_tests(DATASETS)

    print_title("Exporting results")
    save_reports("data", report)