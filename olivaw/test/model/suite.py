from glob import glob
from datetime import datetime
from os import makedirs
from os.path import exists, sep, abspath
from sys import argv
from codecs import open as copen

from olivaw.constants import (
    MODULES_TTL_GLOB_PATH,
    MODELETS_TTL_GLOB_PATH,
    DEV_USERNAME,
    PWD_TO_OUTPUT_FOLDER,
    BRANCH,
    SKIPPED_FILES,
    MODE
)

from olivaw.test.corese import print_title # TODO Need later for a utils.py?

from .testing import (
    modules_tests,
    modelets_tests,
    merged_fragment_set_test,
)

from olivaw.test.turtle import (
    prepare_graph,
    make_assertor
)

from olivaw.test.markdown import (
    make_turtle_page
)

def datetime_id():
    return ".".join(
            datetime\
            .now()\
            .isoformat()\
            .split(".")[:-1]
        ).replace(":", "-")

###
# Test OWL_RL
###
def test_model():

    report = prepare_graph()
    test_assertor = make_assertor(
        report,
        f"https://github.com/Wimmics/olivaw/blob/main/olivaw/test/model/suite.py"
    )

    print_title("Checking existing modules")
    modules = [
        item
        for item in MODULES_TTL_GLOB_PATH
        if not abspath(item) in SKIPPED_FILES
    ]

    unsafe_modules = modules_tests(modules, report, test_assertor)

    print_title("Checking modelets")
    modelets = [
        item
        for item in MODELETS_TTL_GLOB_PATH
        if not abspath(item) in SKIPPED_FILES
    ]
    unsafe_modelets = modelets_tests(modelets, report, test_assertor)

    print_title("Checking the merge of safe modules")
    safe_modules = [
        module for module in modules
        if not module in unsafe_modules
    ]
    merged_fragment_set_test(
        report,
        test_assertor,
        safe_modules,
        "all-modules",
        custom_title=f"All the modules from branch {BRANCH} that are syntaxically correct as well as their recursive imports"    
    )

    print_title("Checking the merge of safe fragments")
    fragments = modules + modelets
    unsafe_fragments = unsafe_modules + unsafe_modelets

    safe_fragment = [
        fragment for fragment in fragments
        if not fragment in unsafe_fragments
    ]
    merged_fragment_set_test(
        report,
        test_assertor,
        safe_fragment,
        "all-fragments",
        custom_title=f"All the fragments from branch {BRANCH} that are syntaxically correct as well as their recursive imports"  
    )

    file_name = MODE if not MODE == "manual" else f"{MODE}-{DEV_USERNAME}-{datetime_id()}"
    file_base = f"{PWD_TO_OUTPUT_FOLDER}model-test-{file_name}"

    print_title("Exporting results")

    markdown = make_turtle_page(report, file_base.split(sep)[-1])

    if not exists(PWD_TO_OUTPUT_FOLDER):
        makedirs(PWD_TO_OUTPUT_FOLDER)

    with copen(f"{file_base}.ttl", "w", "utf-8") as f:
        f.write(report.serialize(format="ttl"))

    with copen(f"{file_base}.md", "w", "utf-8") as f:
        f.write(markdown)