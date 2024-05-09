from json import load
from sys import exit
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

COMMAND = []
try:
  COMMAND = [
    argv[index]
    for index in range(len(argv))
    if index > [
      i for i in range(len(argv))
      if argv[i].split(sep)[-1].split(".")[0] == "olivaw"
    ][0]
  ]
except:
  pass

modes = [
  item.split('=')[1]
  for item in COMMAND
  if item.startswith("--mode=")
]

MODE = modes[0] if len(modes) > 0 else "manual"

ACTIONS = MODE == "actions"
PRECOMMIT = MODE == "precommit"

SKIP_PASS = "--skip-pass" in COMMAND
TESTED_ONLY = "--tested-only" in COMMAND

QUIET = ACTIONS or PRECOMMIT

ERROR_RESOURCES = None
with open(f"{PWD_TO_CONSTANTS}{sep}error-resources.json", "r") as f:
  ERROR_RESOURCES = load(f)

ERROR_IDS = list(ERROR_RESOURCES.keys())

ONTOLOGY_PREFIX = ONTOLOGY_URL = TERM_DISTANCE_THRESHOLD = BLOCKING_ERRORS = GIST_INDEX = SKIPPED_ERRORS = SKIPPED_TESTS = SKIP_FOR_TEST = SKIP_FOR_FILE = None
TESTED_MODULES = TESTED_MODELETS = None

if exists(f"{ROOT_FOLDER}{sep}.acimov{sep}parameters.json"):
  with open(f"{ROOT_FOLDER}{sep}.acimov{sep}parameters.json", "r") as f:
    repo_parameters = None
    
    try:
      repo_parameters = load(f)
    except:
      print("fatal: parameters.json is not a well formed json file")
      exit(1)

    if "ontology_prefix" in repo_parameters:
      ONTOLOGY_PREFIX = repo_parameters["ontology_prefix"]

    # The ontology base URL
    if "ontology_url" in repo_parameters:
      ONTOLOGY_URL = repo_parameters["ontology_url"]
    else:
      print('fatal: parameter "ontology_url" not found in parameters.json')
      exit(1)

    # The desired levenshtein threshold to accept terms as different enough
    if "term_distance_threshold" in repo_parameters:
      TERM_DISTANCE_THRESHOLD = repo_parameters["term_distance_threshold"]
    else:
      print('fatal: parameter "term_distance_threshold" not found in parameters.json')
      exit(1)

    # The errors ids that are defined as blocking
    if "blocking_errors" in repo_parameters:
      BLOCKING_ERRORS = repo_parameters["blocking_errors"]
    else:
      print('fatal: parameter "blocking_errors" not found in parameters.json')
      exit(1)

    # Id of Gist containing al the badges data
    if "gist_index" in repo_parameters:
      GIST_INDEX = repo_parameters["gist_index"]
    else:
      print('fatal: parameter "gist_index" not found in parameters.json')
      exit(1)

    # Error identifiers that should not be written in the reports
    SKIPPED_ERRORS = repo_parameters["skipped_errors"] if "skipped_errors" in repo_parameters else []

    # Test identifiers that should not be written in the reports
    SKIPPED_TESTS = repo_parameters["skipped_tests"] if "skipped_tests" in repo_parameters else []

    # Relative paths between repo root and files that should be skipped in tests
    SKIPPED_FILES = [
      (
        abspath(f"{ROOT_FOLDER}{sep}{path}")
        if exists(f"{ROOT_FOLDER}{sep}{path}")
        else path
      )
      for path in repo_parameters["skipped_files"]
    ] if "skipped_files" in repo_parameters else []

    TESTED_MODULES = [
      file for file in MODULES_TTL_GLOB_PATH
      if not abspath(file) in SKIPPED_FILES
    ]

    TESTED_MODELETS = [
      file for file in MODELETS_TTL_GLOB_PATH
      if not abspath(file) in SKIPPED_FILES
    ]

    SKIP_FOR_TEST = {
      criterion: [
        (
          abspath(f"{ROOT_FOLDER}{sep}{file}")
          if exists(f"{ROOT_FOLDER}{sep}{file}")
          else file
        )
        for file in files
      ]
      for criterion, files
      in repo_parameters["skip_for_test"].items()
    } if "skip_for_test" in repo_parameters else {}

    SKIP_FOR_FILE = {
      (
        abspath(f"{ROOT_FOLDER}{sep}{file}")
        if exists(f"{ROOT_FOLDER}{sep}{file}")
        else file
      ): criterions
      for file, criterions
      in repo_parameters["skip_for_file"].items()
    } if "skip_for_file" in repo_parameters else {}

  def add_repo_variables(request):
    return request\
      .replace("ONTOLOGY_URL", ONTOLOGY_URL)\
      .replace("TERM_DISTANCE_THRESHOLD", str(TERM_DISTANCE_THRESHOLD))

  from .uris import *

  VARIABLE_REQUESTS = [
    "NOT_REFERENCED",
    "GET_BY_MODULE",
    "DOMAIN_OUT_Of_VOCABULARY",
    "RANGE_OUT_OF_VOCABULARY",
    "GET_TOO_CLOSED_PAIRS",
    "NOT_LABELED",
    "GET_TERM_PAIRS",
    "GET_ONTOLOGY_TERMS",
    "GET_IMPORTS",
    "ADD_VARIABLE"
  ]

  for request_name in VARIABLE_REQUESTS:
    request_value = locals()[request_name]
    locals()[request_name] = add_repo_variables(request_value)

  ONTOLOGY_NAMESPACE = Namespace(ONTOLOGY_URL)

  # The character separating the ontology base URL from the suffix
  ONTOLOGY_SEPARATOR = ONTOLOGY_URL[-1]

  for error in ERROR_RESOURCES.keys():
    ERROR_RESOURCES[error]["blocking"] = error in BLOCKING_ERRORS

CRITERION_DATA = None
try:
    from rdflib import Graph
    criterions_graph = Graph()
    criterions_graph.parse(PWD_TO_MODEL_TEST_ONTO)
    criterions = criterions_graph.query(GET_CRITERION_DATA)
    CRITERION_DATA = {
        str(criterion_id): {
            "title": str(criterion_title),
            "description": str(criterion_description),
            "errors" : [
              str(id)
              for id in criterions_graph.query(
                GET_ERRORS_OF_TEST.replace("CRITERION_ID", criterion_id)
              )
            ]
        }
        for criterion_id, criterion_title, criterion_description in criterions
    }
except:
  raise

CRITERION_IDS = list(CRITERION_DATA.keys())

MODEL_BEST_PRACTICES_TESTS = ["owl-rl-constraint", "profile-compatibility", "term-referencing", "domain-and-range-referencing", "terms-differenciation", "labeled-terms"]

DATASETS = [
  item
  for item in USE_CASES_TTL_GLOB_PATH + DATASETS_TTL_GLOB_PATH
  if not abspath(item) in SKIPPED_FILES
]