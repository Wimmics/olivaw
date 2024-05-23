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

# List of all the arguments that were typed after "olivaw" in the command line
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
  if item.startswith("--MODE=")
]

# The execution mode that will drive some olivaw behaviour, default is manual
MODE = modes[0] if len(modes) > 0 else "manual"

# Boolean indicating if olivaw is in actions mode
ACTIONS = MODE == "ACTIONS"

# Boolean inidication if olivaw is in pre-commit mode
PRECOMMIT = MODE == "PRECOMMIT"

# Boolean indicating if the reports should ommit the Pass outcomes
SKIP_PASS = "--SKIP-PASS" in COMMAND

# Boolean indicating if the reports should ommit the NotTested outcomes
TESTED_ONLY = "--TESTED-ONLY" in COMMAND

# Boolean indicating if the reports should hide the progress bars
QUIET = ACTIONS or PRECOMMIT

# Dictionary providing the useful data concerning the errors
ERROR_RESOURCES = None
with open(f"{PWD_TO_CONSTANTS}{sep}error-resources.json", "r") as f:
  ERROR_RESOURCES = load(f)

# Set of all the errors of the default tests
ERROR_IDS = list(ERROR_RESOURCES.keys())

ONTOLOGY_PREFIX = ONTOLOGY_NAMESPACE = TERM_DISTANCE_THRESHOLD = BLOCKING_ERRORS = GIST_INDEX = SKIPPED_ERRORS = SKIPPED_TESTS = SKIP_FOR_TEST = SKIP_FOR_SUBJECT = None
TESTED_MODULES = TESTED_MODELETS = None

if exists(f"{ROOT_FOLDER}{sep}.acimov{sep}parameters.json"):
  with open(f"{ROOT_FOLDER}{sep}.acimov{sep}parameters.json", "r") as f:
    repo_parameters = None
    
    try:
      repo_parameters = load(f)
    except:
      pass

    # Preferred prefix for the ontology
    if "ontology_prefix" in repo_parameters:
      ONTOLOGY_PREFIX = repo_parameters["ontology_prefix"]

    # The ontology base URL
    if "ontology_namespace" in repo_parameters:
      ONTOLOGY_NAMESPACE = repo_parameters["ontology_namespace"]

    # The desired levenshtein threshold to accept terms as different enough
    if "term_distance_threshold" in repo_parameters:
      TERM_DISTANCE_THRESHOLD = repo_parameters["term_distance_threshold"]

    # The errors ids that are defined as blocking
    if "blocking_errors" in repo_parameters:
      BLOCKING_ERRORS = repo_parameters["blocking_errors"]

    # Id of Gist containing al the badges data
    if "gist_index" in repo_parameters:
      GIST_INDEX = repo_parameters["gist_index"]

    # Error identifiers that should not be written in the reports
    SKIPPED_ERRORS = repo_parameters["skipped_errors"] if "skipped_errors" in repo_parameters else []

    # Test identifiers that should not be written in the reports
    SKIPPED_TESTS = repo_parameters["skipped_tests"] if "skipped_tests" in repo_parameters else []

    # Relative paths between repo root and files that should be skipped in tests
    SKIPPED_SUBJECTS = [
      (
        abspath(f"{ROOT_FOLDER}{sep}{path}")
        if exists(f"{ROOT_FOLDER}{sep}{path}")
        else path
      )
      for path in repo_parameters["skipped_subjects"]
    ] if "skipped_subjects" in repo_parameters else []

    # List of all the modules that should be tested 
    TESTED_MODULES = [
      file for file in MODULES_TTL_GLOB_PATH
      if not abspath(file) in SKIPPED_SUBJECTS
    ]

    # List of all the modelets that should be tested
    TESTED_MODELETS = [
      file for file in MODELETS_TTL_GLOB_PATH
      if not abspath(file) in SKIPPED_SUBJECTS
    ]

    # Dictionary of tests identifier linked to test that should not be run for this subject
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

    # Dictionary of subjects (subjects identifiers or files) that are linked to tests that should not be run on it
    SKIP_FOR_SUBJECT = {
      (
        abspath(f"{ROOT_FOLDER}{sep}{file}")
        if exists(f"{ROOT_FOLDER}{sep}{file}")
        else file
      ): criterions
      for file, criterions
      in repo_parameters["skip_for_subject"].items()
    } if "skip_for_subject" in repo_parameters else {}

    # Set of data fragments that should be tested
    DATASETS = [
      item
      for item in USE_CASES_TTL_GLOB_PATH + DATASETS_TTL_GLOB_PATH
      if not abspath(item) in SKIPPED_SUBJECTS
    ]

  def add_repo_variables(request):
    return request\
      .replace(
        "ONTOLOGY_NAMESPACE",
        ONTOLOGY_NAMESPACE if (not ONTOLOGY_NAMESPACE is None) else "ONTOLOGY_NAMESPACE"
      )\
      .replace(
        "TERM_DISTANCE_THRESHOLD",
        str(TERM_DISTANCE_THRESHOLD) if (not TERM_DISTANCE_THRESHOLD is None) else "TERM_DISTANCE_THRESHOLD"
      )

  from .uris import *

  # SparQL request that rely on some repository data
  VARIABLE_REQUESTS = [
    "NOT_REFERENCED",
    "GET_BY_MODULE",
    "DOMAIN_OUT_Of_VOCABULARY",
    "RANGE_OUT_OF_VOCABULARY",
    "NOT_LABELED",
    "GET_TERM_PAIRS",
    "GET_ONTOLOGY_TERMS",
    "GET_IMPORTS",
    "ADD_VARIABLE"
  ]

  for request_name in VARIABLE_REQUESTS:
    request_value = locals()[request_name]
    locals()[request_name] = add_repo_variables(request_value)

# Rdflib object representing the ontology namespace
ONTOLOGY_RDFLIB_NAMESPACE = None

# Last character from the end of the ontology namespace
ONTOLOGY_SEPARATOR = None

if not ONTOLOGY_NAMESPACE is None:
  # The character separating the ontology base URL from the suffix
  ONTOLOGY_SEPARATOR = ONTOLOGY_NAMESPACE[-1]

if not BLOCKING_ERRORS is None:
  for error in ERROR_RESOURCES.keys():
    ERROR_RESOURCES[error]["blocking"] = error in BLOCKING_ERRORS

# Dictonary storing the criterions from the earl-olivaw dataset
CRITERION_DATA = None
try:
    from rdflib import Graph
    if not ONTOLOGY_NAMESPACE is None:
      ONTOLOGY_RDFLIB_NAMESPACE = Namespace(ONTOLOGY_NAMESPACE)
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
    CRITERION_IDS = list(CRITERION_DATA.keys())
except:
  pass

# Set of model tests that rely on the syntax test to pass
MODEL_BEST_PRACTICES_TESTS = ["owl-rl-constraint", "profile-compatibility", "term-referencing", "domain-and-range-referencing", "terms-differenciation", "labeled-terms"]