from os.path import abspath, sep
from regex import compile as regex_compile

from .uris import CORESE_PYTHON_URL

# The corese python executable name
DECIDABILITY_RANGE = ["OWL_TC", "OWL_RL", "OWL_QL", "OWL_EL"]
CORESE_JAR_NAME = CORESE_PYTHON_URL.split('/')[-1]
CORESE_LOCAL_PATH = abspath(f"{sep.join(__file__.split(sep)[:-1])}{sep}..{sep}{CORESE_JAR_NAME}")
AST_ERROR_FORMAT = regex_compile("ERROR fr\\.inria\\.corese\\.sparql\\.triple\\.parser\\.ASTQuery")
PROFILE_ERROR_FORMAT = regex_compile("^[0-9]+\\. [^\\n]+|$")
