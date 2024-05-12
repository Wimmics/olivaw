from os.path import abspath

from rdflib import DCTERMS

from olivaw.constants import SKIP_FOR_TEST, SKIP_FOR_SUBJECT, SKIPPED_TESTS, SKIPPED_SUBJECTS

def should_skip(draft):
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