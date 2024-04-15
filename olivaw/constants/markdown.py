
ERROR_TABLE_HEADER = [
    "|*Jump*|*Number*|*Status*|*Subject*|*Criterion*|*Title*|*Link*|",
    "|------|--------|--------|---------|-----------|-------|------|"
]

COLOR_BOX_TEMPLATE = "EMOJI*TEXT*"

global MODULE_URL_FORMAT, MODELET_URL_FORMAT, DATASET_URL_FORMAT, USECASE_URL_FORMAT

try:
    import regex as re

    MODULE_URL_FORMAT = re.compile('src/[^/]+$')
    MODELET_URL_FORMAT = re.compile('domains/[^/]+/[^/]+/onto\.ttl')
    DATASET_URL_FORMAT = re.compile('domains/[^/]+/[^/]+/dataset\.ttl')
    USECASE_URL_FORMAT = re.compile('use-cases/[^/]+/[^/]+$')
    QUESTION_URL_FORMAT = re.compile('domains/[^/]+/[^/]+/[^\.]+\.rq')

    NEW_LINES = re.compile('\\n+')
    NEW_BR = re.compile('((\\&\\#10;)+)')
except:
    MODULE_URL_FORMAT = None
    MODELET_URL_FORMAT = None
    DATASET_URL_FORMAT = None,
    USECASE_URL_FORMAT = None

LITERAL_CUTTING_LENGTH = 60