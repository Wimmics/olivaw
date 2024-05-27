"""Module executing the `olivaw test model` command"""

from olivaw.constants import (
    BRANCH,
    TESTED_MODELETS,
    TESTED_MODULES
)

from olivaw.test.markdown import markdown_export
from olivaw.test.util import print_title, file_name, save_reports

from .testing import (
    modules_tests,
    modelets_tests,
    merged_fragment_set_test,
    shape_data
)

from olivaw.test.turtle import new_report

###
# Test OWL_RL
###
def test_model() -> None:
    """Executes the model tests over all the model fragments from the project"""
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
    file_base_name = file_name("model")
    save_reports(
        file_base_name,
        report.serialize(format="ttl"),
        markdown_export(report, file_base_name, shape_data=shape_data)
    )