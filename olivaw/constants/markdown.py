"""Module providing constants related to the markdown report format generation"""

from regex import compile as regex_compile, Pattern

ERROR_TABLE_HEADER: list[str] = [
    "|*Jump*|*Number*|*Status*|*Subject*|*Criterion*|*Title*|*Link*|",
    "|------|--------|--------|---------|-----------|-------|------|"
]
"""Head of the summary tables of the report"""

MODULE_URL_FORMAT: Pattern = regex_compile('src/(([^/]+/)*[^/]+)$')
"""Format of a module fragment URL"""

MODELET_URL_FORMAT: Pattern = regex_compile('domains/[^/]+/[^/]+/onto\.ttl')
"""Format of a modelet fragment URL"""

DATASET_URL_FORMAT: Pattern = regex_compile('domains/[^/]+/[^/]+/dataset\.ttl')
"""Format of a dataset fragment URL"""

USECASE_URL_FORMAT: Pattern = regex_compile('use-cases/[^/]+/[^/]+$')
"""Format of a use-case fragment URL"""

QUESTION_URL_FORMAT: Pattern = regex_compile('domains/[^/]+/[^/]+/[^\.]+\.rq')
"""Format of a competency question fragment URL"""

NEW_LINES: Pattern = regex_compile('\\n+')
"""Regex for detecting multiple line breaks in a row"""

NEW_BR: Pattern = regex_compile('((\\&\\#10;)+)')
"""Regex for detecting multiple HTML line breaks in a row"""