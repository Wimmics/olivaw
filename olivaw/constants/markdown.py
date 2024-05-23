"""Module providing constants related to the markdown report format generation"""

ERROR_TABLE_HEADER: list[str] = [
    "|*Jump*|*Number*|*Status*|*Subject*|*Criterion*|*Title*|*Link*|",
    "|------|--------|--------|---------|-----------|-------|------|"
]
"""Head of the summary tables of the report"""

MODULE_URL_FORMAT = None
"""Format of a module fragment URL"""

MODELET_URL_FORMAT = None
"""Format of a modelet fragment URL"""

DATASET_URL_FORMAT = None
"""Format of a dataset fragment URL"""

USECASE_URL_FORMAT = None
"""Format of a use-case fragment URL"""

QUESTION_URL_FORMAT = None
"""Format of a competency question fragment URL"""

NEW_LINES = None
"""Regex for detecting multiple line breaks in a row"""

NEW_BR = None
"""Regex for detecting multiple HTML line breaks in a row"""

try:
    from regex import compile as regex_compile, Pattern

    MODULE_URL_FORMAT: Pattern = regex_compile('src/(([^/]+/)*[^/]+)$')

    MODELET_URL_FORMAT: Pattern = regex_compile('domains/[^/]+/[^/]+/onto\.ttl')

    DATASET_URL_FORMAT: Pattern = regex_compile('domains/[^/]+/[^/]+/dataset\.ttl')

    USECASE_URL_FORMAT: Pattern = regex_compile('use-cases/[^/]+/[^/]+$')

    QUESTION_URL_FORMAT: Pattern = regex_compile('domains/[^/]+/[^/]+/[^\.]+\.rq')

    NEW_LINES: Pattern = regex_compile('\\n+')

    NEW_BR: Pattern = regex_compile('((\\&\\#10;)+)')
except:
    MODULE_URL_FORMAT = None
    MODELET_URL_FORMAT = None
    DATASET_URL_FORMAT = None,
    USECASE_URL_FORMAT = None