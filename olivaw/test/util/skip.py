from os.path import abspath

from rdflib import DCTERMS

from olivaw.constants import SKIP_FOR_TEST, SKIP_FOR_FILE, SKIPPED_TESTS, SKIPPED_FILES

def should_skip(draft):
    if draft.has_field("file") and isinstance(draft.file, str):
        subject_ref = abspath(draft.file)
    elif draft.has_field("subject"):
        subject_ref = str(draft.report.value(draft.subject, DCTERMS.identifier))

    result =  draft.criterion in SKIPPED_TESTS or \
        subject_ref in SKIPPED_FILES or \
        ( # skip for test
            draft.criterion in SKIP_FOR_TEST and
            subject_ref in SKIP_FOR_TEST[draft.criterion]
        ) or \
        ( # skip for file
            subject_ref in SKIP_FOR_FILE and \
            draft.criterion in SKIP_FOR_FILE[subject_ref]
        )
    return result