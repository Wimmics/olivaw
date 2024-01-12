from os.path import relpath, sep

from olivaw.test.corese import safe_load
from olivaw.test.turtle import (
    make_subject,
    make_assertion
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
    graph = safe_load(dataset, disable_import=True)

    make_assertion(
        report,
        assertor,
        subject,
        "syntax",
        "syntax-error",
        graph if isinstance(graph, list) else [],
        skip_pass=skip_pass,
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