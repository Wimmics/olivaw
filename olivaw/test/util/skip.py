"""Module providing functions that states if a test should be run according to the test, the subject and the repository parameters"""

from os.path import abspath
from rdflib import DCTERMS
from olivaw.constants import (
    SKIP_FOR_TEST,
    SKIP_FOR_SUBJECT,
    SKIPPED_TESTS,
    SKIPPED_SUBJECTS
)
from olivaw.test.util.draft import AssertDraft

def should_skip(draft: AssertDraft) -> bool:
    """Returns a boolean stating if the current test should be skipped

    :param draft: Assertion draft useful information for the current test
    :type draft: `olivaw.test.AssertDraft`

    :returns: A boolean stating if the current test should be skipped
    :rtype: `bool`
    """
    subject_file = subject_id = None
    if draft.has_field("file") and isinstance(draft.file, str):
        subject_file = abspath(draft.file)
    if draft.has_field("subject"):
        subject_id = str(draft.report.value(draft.subject, DCTERMS.identifier))

    result =  draft.criterion in SKIPPED_TESTS or \
        subject_file in SKIPPED_SUBJECTS or \
        subject_id in SKIPPED_SUBJECTS or \
        ( # skip for test (by file)
            draft.criterion in SKIP_FOR_TEST and
            subject_file in SKIP_FOR_TEST[draft.criterion]
        ) or \
        ( # skip for test (by id)
            draft.criterion in SKIP_FOR_TEST and
            subject_id in SKIP_FOR_TEST[draft.criterion]
        ) or \
        ( # skip for subject (by file)
            subject_file in SKIP_FOR_SUBJECT and \
            draft.criterion in SKIP_FOR_SUBJECT[subject_file]
        ) or \
        ( # skip for subject (by id)
            subject_id in SKIP_FOR_SUBJECT and \
            draft.criterion in SKIP_FOR_SUBJECT[subject_id]
        )
    return result