from json import load
from os.path import sep

from .paths import *

from .corese_info import *
from .git_info import *
from .sparql import *

from .rdflib_info import *

from .markdown import *

__all__ = ["uris", "paths", "corese_info", "git_info", "sparql", "rdflib_info", "markdown"]

TEST_RESOURCES = None
with open(f"{sep.join(__file__.split(sep)[:-1])}{sep}tests-resources.json", "r") as f:
  TEST_RESOURCES = load(f)

ONTOLOGY_URL = None
TERM_DISTANCE_THRESHOLD = None
BLOCKING_ERRORS = None

with open(f"{ROOT_FOLDER}{sep}.acimov{sep}parameters.json") as f:
  repo_parameters = load(f)

  # The ontology base URL
  ONTOLOGY_URL = repo_parameters["ontology_url"]

  # The desired levenshtein threshold to accept terms as different enough
  TERM_DISTANCE_THRESHOLD = repo_parameters["term_distance_threshold"]

  # The errors ids that are defined as blocking
  BLOCKING_ERRORS = repo_parameters["blocking_errors"]

def add_repo_variables(request):
  return request.replace("ONTOLOGY_URL", ONTOLOGY_URL).replace("TERM_DISTANCE_THRESHOLD", str(TERM_DISTANCE_THRESHOLD))

from .uris import *

NOT_REFERENCED = add_repo_variables(NOT_REFERENCED)
GET_BY_MODULE = add_repo_variables(GET_BY_MODULE)
DOMAIN_OUT_Of_VOCABULARY = add_repo_variables(DOMAIN_OUT_Of_VOCABULARY)
RANGE_OUT_OF_VOCABULARY = add_repo_variables(RANGE_OUT_OF_VOCABULARY)
GET_TOO_CLOSED_PAIRS = add_repo_variables(GET_TOO_CLOSED_PAIRS)
NOT_LABELED = add_repo_variables(NOT_LABELED)
GET_TERM_PAIRS = add_repo_variables(GET_TERM_PAIRS)

ONTOLOGY_NAMESPACE = Namespace(ONTOLOGY_URL)

# The character separating the ontology base URL from the suffix
ONTOLOGY_SEPARATOR = ONTOLOGY_URL[-1]

for criterion in TEST_RESOURCES.keys():
  criterion_resource = TEST_RESOURCES[criterion]
  for error in criterion_resource["errors"].keys():
    error_resource = criterion_resource["errors"][error]
    error_resource["blocking"] = error in BLOCKING_ERRORS

CRITERIONS_NEEDING_SYNTAX = [
  criterion for criterion in TEST_RESOURCES.keys()
  if not criterion == "syntax"
]

BEST_PRACTICES_TESTS = [
  criterion for criterion in CRITERIONS_NEEDING_SYNTAX
  if not criterion in ["syntax", "owl-rl-constraint", "profile"]
]