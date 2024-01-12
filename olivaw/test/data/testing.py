from os.path import relpath, sep

from olivaw.test.corese import safe_load, check_OWL_constraints
from olivaw.test.turtle import (
    make_subject,
    make_assertion,
    make_not_tested
)
from olivaw.constants import ROOT_FOLDER

def fragment_check(
    report,
    assertor,
    dataset,
    skip_pass=False,
    tested_only=False
):
    dataset_key = relpath(dataset, ROOT_FOLDER).replace(sep, "/")
    subject = make_subject(report, [dataset_key])
    graph_no_import = safe_load(dataset, disable_import=True)

    is_syntax_valid = not isinstance(graph_no_import, list)

    make_assertion(
        report,
        assertor,
        subject,
        "syntax",
        "syntax-error",
        [] if is_syntax_valid else graph_no_import,
        skip_pass=skip_pass,
        tested_only=tested_only
    )

    graph_with_import = safe_load(dataset) if is_syntax_valid else None
    is_valid = is_syntax_valid and not isinstance(graph_with_import, list)

    if is_valid:
        # Check for respect for OWL constraints
        make_assertion(
            report,
            assertor,
            subject,
            "owl-rl-constraint",
            "owl-rl-constraint-violation",
            check_OWL_constraints(graph_with_import),
            skip_pass=skip_pass,
            tested_only=tested_only
        )
    else:
        make_not_tested(
            report,
            assertor,
            subject,
            "owl-rl-constraint",
            tested_only=tested_only
        )
    


def data_fragment_test(report, assertor, datasets, skip_pass, tested_only):

    for dataset in datasets:
        fragment_check(
            report,
            assertor,
            dataset,
            skip_pass=skip_pass,
            tested_only=tested_only
        )