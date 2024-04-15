from sys import argv
from os.path import sep, abspath
from glob import glob
from datetime import datetime
from codecs import open as copen

from olivaw.constants import (
    DEV_USERNAME,
    PWD_TO_OUTPUT_FOLDER,
    DATASETS,
    MODE,
    SKIP_PASS,
    TESTED_ONLY
)

from olivaw.test.corese import print_title
from olivaw.test.markdown import make_turtle_page
from olivaw.test.data.testing import data_tests
from olivaw.test.turtle import (
    prepare_graph,
    make_assertor
)

def datetime_id():
    return ".".join(
            datetime\
            .now()\
            .isoformat()\
            .split(".")[:-1]
        ).replace(":", "-")

def test_data():
    report = prepare_graph()
    assertor = make_assertor(
        report,
        f"https://github.com/Wimmics/olivaw/blob/main/olivaw/test/data/suite.py"
    )
    
    print_title("Running data tests")

    data_tests(
        DATASETS,
        report,
        assertor
    )

    file_name = MODE if not MODE == "manual" else f"{MODE}-{DEV_USERNAME}-{datetime_id()}"
    file_base = f"{PWD_TO_OUTPUT_FOLDER}data-test-{file_name}"

    print_title("Exporting results")

    markdown = make_turtle_page(report, file_base.split(sep)[-1])

    with copen(f"{file_base}.ttl", "w", "utf-8") as f:
        f.write(report.serialize(format="ttl"))

    with copen(f"{file_base}.md", "w", "utf-8") as f:
        f.write(markdown)