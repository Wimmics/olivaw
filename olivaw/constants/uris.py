##############
# Parameters #
##############

# The URL of the Corese python library to fetch
CORESE_PYTHON_URL = "https://files.inria.fr/corese/distrib/corese-library-python-4.4.1.jar"
# The EARL ontology prefix
EARL_PREFIX="http://www.w3.org/ns/earl#"

URI_FORMAT = None
try:
    import regex as re
    URI_FORMAT = re.compile("^(([^:/?#\s]+):)(\/\/([^/?#\s]*))?([^?#\s]*)(\?([^#\s]*))?(#(.*))?$")
except:
    pass