from json import load
from os.path import sep

from .paths import *

from .corese_info import *
from .git_info import *
from .sparql import *

from .rdflib_info import *

from .markdown import *

__all__ = ["parameters", "paths", "corese_info", "git_info", "sparql", "rdflib_info", "markdown"]

from .parameters import ONTOLOGY_URL, BLOCKING_ERRORS

# The character separating the ontology base URL from the suffix
ONTOLOGY_SEPARATOR = ONTOLOGY_URL[-1]

TEST_RESOURCES = None
with open(f"{sep.join(__file__.split(sep)[:-1])}{sep}tests-resources.json", "r") as f:
  TEST_RESOURCES = load(f)

ONTOLOGY_URL = None
CORESE_PYTHON_URL = None
TERM_DISTANCE_THRESHOLD = None
EARL_PREFIX = None
BLOCKING_ERRORS = None

with open(f"{ROOT_FOLDER}{sep}.acimov{sep}parameters.json") as f:
  repo_parameters = load(f)

  ##############
  # Parameters #
  ##############

  # The ontology base URL
  ONTOLOGY_URL = repo_parameters["ontology_url"]

  # The URL of the Corese python library to fetch
  CORESE_PYTHON_URL = repo_parameters["corese_python_url"]

  # The desired levenshtein threshold to accept terms as different enough
  TERM_DISTANCE_THRESHOLD = repo_parameters["term_distance_threshold"]

  # The EARL ontology prefix
  EARL_PREFIX= repo_parameters["earl_prefix"]

  # The errors ids that are defined as blocking
  BLOCKING_ERRORS = repo_parameters["blocking_errors"]

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