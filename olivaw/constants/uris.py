"""Module providing URIs constants and formats"""

from regex import compile as regex_compile, Pattern

##############
# Parameters #
##############

CORESE_PYTHON_URL: str = "https://files.inria.fr/corese/distrib/corese-library-python-4.4.1.jar"
"""The URL of the Corese python library to fetch"""

EARL_PREFIX: str ="http://www.w3.org/ns/earl#"
"""The EARL ontology prefix"""

URI_FORMAT: Pattern = regex_compile("^(([^:/?#\s]+):)(\/\/([^/?#\s]*))?([^?#\s]*)(\?([^#\s]*))?(#(.*))?$")
"""Regex specifying the format of a URI"""