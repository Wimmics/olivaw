from os.path import abspath, sep

from .uris import CORESE_PYTHON_URL
from .paths import PWD_TO_CONSTANTS

# Set of standard profiles that Corese can detect  on an ontology fragment
DECIDABILITY_RANGE = ["OWL_RL", "OWL_QL", "OWL_EL"]

# Corese jar name
CORESE_JAR_NAME = CORESE_PYTHON_URL.split('/')[-1]

# Local path is expected for Corese executable
CORESE_LOCAL_PATH = abspath(f"{PWD_TO_CONSTANTS}{sep}..{sep}{CORESE_JAR_NAME}")

# Regex detecting SparQL parsing errors 
AST_ERROR_FORMAT = None

# Regex detecting RDF parsing formats
PROFILE_ERROR_FORMAT = None

try:
    from regex import compile as regex_compile

    AST_ERROR_FORMAT = regex_compile("ERROR fr\\.inria\\.corese\\.sparql\\.triple\\.parser\\.ASTQuery")
    PROFILE_ERROR_FORMAT = regex_compile("^[0-9]+\\. [^\\n]+|$")
except:
    pass