from sys import argv
from glob import glob
from datetime import datetime
from tqdm import tqdm
from codecs import open as copen
from os.path import sep

from olivaw.test.corese import print_title
from olivaw.test.turtle import prepare_graph, make_assertor
from olivaw.test.markdown import make_turtle_page

from .testing import test_competency_question

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
        f"https://github.com/Wimmics/olivaw/blob/main/olivaw/test/query/suite.py"
    )

    # MAKE QUERY TEST MAGIC HERE
    queries = glob(COMPETENCY_QUESTIONS_GLOB_PATH)

    for query in tqdm(queries, disable=MODE=="actions"):
        test_competency_question(report, assertor, query)

    file_name = mode if not mode == "manual" else f"{mode}-{DEV_USERNAME}-{datetime_id()}"
    file_base = f"{PWD_TO_OUTPUT_FOLDER}query-test-{file_name}"

    print_title("Exporting results")

    markdown = make_turtle_page(report, file_base.split(sep)[-1])

    with copen(f"{file_base}.ttl", "w", "utf-8") as f:
        f.write(report.serialize(format="ttl"))

    with copen(f"{file_base}.md", "w", "utf-8") as f:
        f.write(markdown)