# Head of the summary tables of the report
ERROR_TABLE_HEADER = [
    "|*Jump*|*Number*|*Status*|*Subject*|*Criterion*|*Title*|*Link*|",
    "|------|--------|--------|---------|-----------|-------|------|"
]

MODULE_URL_FORMAT = MODELET_URL_FORMAT = DATASET_URL_FORMAT = USECASE_URL_FORMAT = None

try:
    from regex import compile as regex_compile

    # Format of a module fragment URL
    MODULE_URL_FORMAT = regex_compile('src/(([^/]+/)*[^/]+)$')

    # Format of a modelet fragment URL
    MODELET_URL_FORMAT = regex_compile('domains/[^/]+/[^/]+/onto\.ttl')

    # Format of a dataset fragment URL
    DATASET_URL_FORMAT = regex_compile('domains/[^/]+/[^/]+/dataset\.ttl')

    # Format of a use-case fragment URL
    USECASE_URL_FORMAT = regex_compile('use-cases/[^/]+/[^/]+$')

    # Format of a competency question fragment URL
    QUESTION_URL_FORMAT = regex_compile('domains/[^/]+/[^/]+/[^\.]+\.rq')

    # Regex for detecting multiple line breaks in a row
    NEW_LINES = regex_compile('\\n+')

    # Regex for detecting multiple HTML line breaks in a row
    NEW_BR = regex_compile('((\\&\\#10;)+)')
except:
    MODULE_URL_FORMAT = None
    MODELET_URL_FORMAT = None
    DATASET_URL_FORMAT = None,
    USECASE_URL_FORMAT = None

# Maximal length of a literal in a report code snippet
LITERAL_CUTTING_LENGTH = 60