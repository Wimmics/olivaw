"""Module providing constants related to Corese"""

from os.path import abspath, sep
from regex import compile as regex_compile, Pattern

from .uris import CORESE_PYTHON_URL
from .paths import PWD_TO_CONSTANTS

DECIDABILITY_RANGE: list[str] = ["OWL_RL", "OWL_QL", "OWL_EL"]
"""Set of standard profiles that Corese can detect  on an ontology fragment"""

CORESE_JAR_NAME: str = CORESE_PYTHON_URL.split('/')[-1]
"""Corese jar name"""

CORESE_LOCAL_PATH: str = abspath(f"{PWD_TO_CONSTANTS}{sep}..{sep}{CORESE_JAR_NAME}")
"""Local path is expected for Corese executable"""

AST_ERROR_FORMAT: Pattern = regex_compile("ERROR fr\\.inria\\.corese\\.sparql\\.triple\\.parser\\.ASTQuery")
"""Regex: Detects SparQL parsing errors """