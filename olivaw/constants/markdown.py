import regex as re

ERROR_TABLE_HEADER = [
    "|*Jump*|*Number*|*Status*|*Subject*|*Criterion*|*Title*|*Link*|",
    "|------|--------|--------|---------|-----------|-------|------|"
]

COLOR_BOX_TEMPLATE = "EMOJI*TEXT*"

MODULE_URL_FORMAT = re.compile('src/[^/]+$')
MODELET_URL_FORMAT = re.compile('domains/[^/]+/[^/]+/onto\.ttl')
DATASET_URL_FORMAT = re.compile('domains/[^/]+/[^/]+/dataset\.ttl')
USECASE_URL_FORMAT = re.compile('use-cases/[^/]+/[^/]+$')

NEW_LINES = re.compile('\\n+')

LITERAL_CUTTING_LENGTH = 60