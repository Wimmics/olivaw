from os.path import abspath, sep

from .uris import CORESE_PYTHON_URL
from .paths import PWD_TO_CONSTANTS

# The corese python executable name
DECIDABILITY_RANGE = ["OWL_RL", "OWL_QL", "OWL_EL"]
CORESE_JAR_NAME = CORESE_PYTHON_URL.split('/')[-1]
CORESE_LOCAL_PATH = abspath(f"{PWD_TO_CONSTANTS}{sep}..{sep}{CORESE_JAR_NAME}")

AST_ERROR_FORMAT = None
PROFILE_ERROR_FORMAT = None

try:
    from regex import compile as regex_compile

    AST_ERROR_FORMAT = regex_compile("ERROR fr\\.inria\\.corese\\.sparql\\.triple\\.parser\\.ASTQuery")
    PROFILE_ERROR_FORMAT = regex_compile("^[0-9]+\\. [^\\n]+|$")
except:
    pass