from os.path import abspath

from olivaw.constants import (
    MODULES_TTL_GLOB_PATH,
    MODELETS_TTL_GLOB_PATH,
    BRANCH,
    SKIPPED_FILES
)

from olivaw.test.util import print_title
from olivaw.test.util.encoding import save_reports

from .testing import (
    modules_tests,
    modelets_tests,
    merged_fragment_set_test,
)

from olivaw.test.turtle import new_report

###
# Test OWL_RL
###
def test_model():
    report, assertor = new_report("model")

    print_title("Checking existing modules")
    modules = [
        item
        for item in MODULES_TTL_GLOB_PATH
        if not abspath(item) in SKIPPED_FILES
    ]

    safe_modules = modules_tests(modules, report=report, assertor=assertor)

    print_title("Checking modelets")
    modelets = [
        item
        for item in MODELETS_TTL_GLOB_PATH
        if not abspath(item) in SKIPPED_FILES
    ]
    safe_modelets = modelets_tests(modelets, report=report, assertor=assertor)

    print_title("Checking the merge of safe modules")
    merged_fragment_set_test(
        report,
        assertor,
        safe_modules,
        "all-modules",
        custom_title=f"All the modules from branch {BRANCH} that are syntaxically correct as well as their recursive imports"    
    )

    print_title("Checking the merge of safe fragments")
    merged_fragment_set_test(
        report,
        assertor,
        safe_modules + safe_modelets,
        "all-fragments",
        custom_title=f"All the fragments from branch {BRANCH} that are syntaxically correct as well as their recursive imports"  
    )

    print_title("Exporting results")
    save_reports("model", report)