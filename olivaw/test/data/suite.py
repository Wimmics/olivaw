from sys import argv
from os.path import sep, abspath
from glob import glob
from datetime import datetime
from codecs import open as copen

from olivaw.constants import (
    DEV_USERNAME,
    PWD_TO_OUTPUT_FOLDER,
    DATASETS
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
    _, *args = argv

    modes = [
        item.split('=')[1]
        for item in args
        if item.startswith("--mode=")
    ]

    skip_pass = "--skip-pass" in args
    tested_only = "--tested-only" in args

    mode = modes[0] if len(modes) > 0 else "manual"

    report = prepare_graph()
    assertor = make_assertor(
        report,
        mode,
        f"https://github.com/Wimmics/olivaw/blob/main/olivaw/test/data/suite.py"
    )
    
    print_title("Running data tests")

    data_tests(
        DATASETS,
        report,
        assertor,
        skip_pass,
        tested_only
    )

    file_name = mode if not mode == "manual" else f"{mode}-{DEV_USERNAME}-{datetime_id()}"
    file_base = f"{PWD_TO_OUTPUT_FOLDER}data-test-{file_name}"

    print_title("Exporting results")

    markdown = make_turtle_page(report, file_base.split(sep)[-1])

    with copen(f"{file_base}.ttl", "w", "utf-8") as f:
        f.write(report.serialize(format="ttl"))

    with copen(f"{file_base}.md", "w", "utf-8") as f:
        f.write(markdown)