
ERROR_TABLE_HEADER = [
    "|*Jump*|*Number*|*Status*|*Subject*|*Criterion*|*Title*|*Link*|",
    "|------|--------|--------|---------|-----------|-------|------|"
]

COLOR_BOX_TEMPLATE = "EMOJI*TEXT*"

MODULE_URL_FORMAT = MODELET_URL_FORMAT = DATASET_URL_FORMAT = USECASE_URL_FORMAT = None

try:
    from regex import compile as regex_compile

    MODULE_URL_FORMAT = regex_compile('src/(([^/]+/)*[^/]+)$')
    MODELET_URL_FORMAT = regex_compile('domains/[^/]+/[^/]+/onto\.ttl')
    DATASET_URL_FORMAT = regex_compile('domains/[^/]+/[^/]+/dataset\.ttl')
    USECASE_URL_FORMAT = regex_compile('use-cases/[^/]+/[^/]+$')
    QUESTION_URL_FORMAT = regex_compile('domains/[^/]+/[^/]+/[^\.]+\.rq')

    NEW_LINES = regex_compile('\\n+')
    NEW_BR = regex_compile('((\\&\\#10;)+)')
except:
    MODULE_URL_FORMAT = None
    MODELET_URL_FORMAT = None
    DATASET_URL_FORMAT = None,
    USECASE_URL_FORMAT = None

LITERAL_CUTTING_LENGTH = 60