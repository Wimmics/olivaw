"""A module meant to store the important regexes of the project"""

from regex import Pattern, compile as regex_compile

AST_ERROR_FORMAT: Pattern = regex_compile("ERROR fr\\.inria\\.corese\\.sparql\\.triple\\.parser\\.ASTQuery")
"""Regex: Detects SparQL parsing errors """

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

URI_PATTERN: Pattern = regex_compile("<[^>]*>")
"""Regex detecting a URI node in some RDF data"""

PREFIX_PATTERN: Pattern = regex_compile("@prefix:[^<]*<[^>]*>[^\\.]*.")
"""Regex detecting a prefix declaration with `@prefix` syntax in some turtle data and captures the prefix and namespace"""

PREFIX_ERROR: Pattern = regex_compile('Prefix "[^"]+:" not bound')
"""Regex detecting the rdflib prefix error"""

URI_FORMAT: Pattern = regex_compile("^(([^:/?#\s]+):)(\/\/([^/?#\s]*))?([^?#\s]*)(\?([^#\s]*))?(#(.*))?$")
"""Regex specifying the format of a URI"""

