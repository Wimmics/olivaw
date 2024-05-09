from os.path import abspath

from olivaw.constants import (
    MODULES_TTL_GLOB_PATH,
    MODELETS_TTL_GLOB_PATH,
    BRANCH,
    SKIPPED_FILES,
    TESTED_MODELETS,
    TESTED_MODULES
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
    safe_modules = modules_tests(TESTED_MODULES, report=report, assertor=assertor)

    print_title("Checking modelets")
    safe_modelets = modelets_tests(TESTED_MODELETS, report=report, assertor=assertor)

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