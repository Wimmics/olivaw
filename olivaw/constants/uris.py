##############
# Parameters #
##############

# The URL of the Corese python library to fetch
CORESE_PYTHON_URL = "https://files.inria.fr/corese/distrib/corese-library-python-4.4.1.jar"

# The EARL ontology prefix
EARL_PREFIX="http://www.w3.org/ns/earl#"

# Regex specifying the format of a URI
URI_FORMAT = None
try:
    from regex import compile as regex_compile
    URI_FORMAT = regex_compile("^(([^:/?#\s]+):)(\/\/([^/?#\s]*))?([^?#\s]*)(\?([^#\s]*))?(#(.*))?$")
except:
    pass