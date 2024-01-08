##############
# Parameters #
##############

# The ontology base URL
ONTOLOGY_URL = "https://purl.org/hmas/"
# The URL of the Corese python library to fetch
CORESE_PYTHON_URL = "https://files.inria.fr/corese/distrib/corese-library-python-4.4.1.jar"
# The desired levenshtein threshold to accept terms as different enough
TERM_DISTANCE_THRESHOLD = 3
# The EARL ontology prefix
EARL_PREFIX="http://www.w3.org/ns/earl#"
# The errors ids that are defined as blocking
BLOCKING_ERRORS = [
    "syntax-error",
    "owl-rl-constraint-violation"
]
