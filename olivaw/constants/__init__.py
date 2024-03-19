from json import load
from os.path import sep, exists

from .paths import *

from .corese_info import *
from .git_info import *
from .sparql import *

from .rdflib_info import *

from .markdown import *

from .badges import *

from .prefixcc import *

__all__ = ["uris", "paths", "corese_info", "git_info", "sparql", "rdflib_info", "markdown", "badges", "prefixcc"]

TEST_RESOURCES = None
with open(f"{sep.join(__file__.split(sep)[:-1])}{sep}tests-resources.json", "r") as f:
  TEST_RESOURCES = load(f)

ONTOLOGY_URL = None
TERM_DISTANCE_THRESHOLD = None
BLOCKING_ERRORS = None
GIST_INDEX = None
SKIPPED_ERRORS = None

if exists(f"{ROOT_FOLDER}{sep}.acimov{sep}parameters.json"):
  with open(f"{ROOT_FOLDER}{sep}.acimov{sep}parameters.json", "r") as f:
    repo_parameters = load(f)

    # The ontology base URL
    ONTOLOGY_URL = repo_parameters["ontology_url"]

    # The desired levenshtein threshold to accept terms as different enough
    TERM_DISTANCE_THRESHOLD = repo_parameters["term_distance_threshold"]

    # The errors ids that are defined as blocking
    BLOCKING_ERRORS = repo_parameters["blocking_errors"]

    # Id of Gist containing al the badges data
    GIST_INDEX = repo_parameters["gist_index"]

    # Error identifiers that should not be written in the reports
    SKIPPED_ERRORS = repo_parameters["skipped_errors"] if "skipped_errors" in repo_parameters else []

    # Test identifiers that should not be written in the reports
    SKIPPED_TESTS = repo_parameters["skipped_tests"] if "skipped_tests" in repo_parameters else []

    # Relative paths between repo root and files that should be skipped in tests
    SKIPPED_FILES = repo_parameters["skipped_files"] if "skipped_files" in repo_parameters else []
    SKIPPED_FILES = [abspath(f"{ROOT_FOLDER}{sep}{path}") for path in SKIPPED_FILES]

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
  GET_ONTOLOGY_TERMS = add_repo_variables(GET_ONTOLOGY_TERMS)

  ONTOLOGY_NAMESPACE = Namespace(ONTOLOGY_URL)

  # The character separating the ontology base URL from the suffix
  ONTOLOGY_SEPARATOR = ONTOLOGY_URL[-1]

  for criterion in TEST_RESOURCES.keys():
    criterion_resource = TEST_RESOURCES[criterion]
    for error in criterion_resource["errors"].keys():
      error_resource = criterion_resource["errors"][error]
      error_resource["blocking"] = error in BLOCKING_ERRORS

MODEL_BEST_PRACTICES_TESTS = ["owl-rl-constraint", "profile-compatibility", "term-referencing", "domain-and-range-referencing", "terms-differenciation", "labeled-terms"]

DATASETS = None
try:
  from glob import glob
  DATASETS = [
    item
    for item in glob(USE_CASES_TTL_GLOB_PATH) + glob(DATASETS_TTL_GLOB_PATH)
    if not abspath(item) in SKIPPED_FILES
  ]

  ALL_SUBJECTS = [
    item
    for item in glob(USE_CASES_TTL_GLOB_PATH) + glob(DATASETS_TTL_GLOB_PATH) + glob(MODULES_TTL_GLOB_PATH) + glob(MODELETS_TTL_GLOB_PATH) + glob(COMPETENCY_QUESTIONS_GLOB_PATH)
    if not abspath(item) in SKIPPED_FILES
  ]
except:
  pass