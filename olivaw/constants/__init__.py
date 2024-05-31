"""Package aggregating olivaw constants and repository constants from parameters.json to provide constants all over olivaw package"""

from json import load
from os.path import sep, exists
from typing import Union

from .paths import *

from .git_info import *
from .sparql import *

from .badges import *

from .prefixcc import *

from .corese_info import *

from .markdown import *

try:
  from .rdflib_info import *
except:
  pass

try:
  from .regex import *
except:
  pass

__all__ = ["uris", "paths", "corese_info", "git_info", "sparql", "rdflib_info", "markdown", "badges", "prefixcc", "regex"]

COMMAND: list[str] = []
"""List of all the arguments that were typed after "olivaw" in the command line"""

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

MODE: str = modes[0] if len(modes) > 0 else "manual"
"""The execution mode that will drive some olivaw behaviour, default is manual"""

ACTIONS: bool = MODE == "ACTIONS"
"""Indicates if olivaw is in actions mode"""

PRECOMMIT: bool = MODE == "PRECOMMIT"
"""Indicates if olivaw is in pre-commit mode"""

SKIP_PASS: bool = "--SKIP-PASS" in COMMAND
"""Indicates if the reports should ommit the Pass outcomes"""

TESTED_ONLY: bool = "--TESTED-ONLY" in COMMAND
"""Indicates if the reports should ommit the NotTested outcomes"""

QUIET: bool = ACTIONS or PRECOMMIT
"""Indicates if the reports should hide the progress bars"""

ERROR_RESOURCES: dict = None
"""Provides the useful data concerning the errors"""

with open(f"{PWD_TO_CONSTANTS}{sep}error-resources.json", "r") as f:
  ERROR_RESOURCES = load(f)

ERROR_IDS: list[str] = list(ERROR_RESOURCES.keys())
"""Set of all the errors of the default tests"""

ONTOLOGY_PREFIX: str = None
"""Preferred prefix for the ontology"""

ONTOLOGY_NAMESPACE: str = None
"""The ontology base URL"""

TERM_DISTANCE_THRESHOLD: int = None
"""The desired levenshtein threshold to accept terms as different enough"""

PROJECT_PREFIXES: dict[str, str] = {}
"""The additional set of prefix declaration to use in the reports pointers"""

BLOCKING_ERRORS: list[str] = None
"""The errors ids that are defined as blocking"""

GIST_INDEX: str = None
"""Id of Gist containing all the badges data"""

SKIPPED_ERRORS: list[str] = None
"""Error identifiers for errors that should not be written in the reports"""

SKIPPED_TESTS: list[str] = None
"""Test identifiers that should not be written in the reports"""

SKIPPED_SUBJECTS: list[str] = None
"""Subject identifiers or relative paths from repo root to files that should be skipped in tests"""

SKIP_FOR_TEST: dict[str, list[str]] = None
"""Dictionary of tests identifier linked to test that should not be run for this subject"""

SKIP_FOR_SUBJECT: dict[str, list[str]] = None
"""Dictionary of subjects (subjects identifiers or relative paths from repo root to files) that are linked to tests that should not be run on it"""

TESTED_MODULES: list[str] = None
"""List of all the modules that should be tested"""

TESTED_MODELETS: list[str] = None
"""List of all the modelets that should be tested"""

DATASETS: list[str] = None
"""Set of data fragments that should be tested"""

VARIABLE_REQUESTS: list[str] = None
"""SparQL request that rely on some repository data"""

if exists(f"{ROOT_FOLDER}{sep}.acimov{sep}parameters.json"):
  with open(f"{ROOT_FOLDER}{sep}.acimov{sep}parameters.json", "r") as f:
    repo_parameters = None
    
    try:
      repo_parameters = load(f)
    except:
      pass

    if "ontology_prefix" in repo_parameters:
      ONTOLOGY_PREFIX = repo_parameters["ontology_prefix"]

    if "ontology_namespace" in repo_parameters:
      ONTOLOGY_NAMESPACE = repo_parameters["ontology_namespace"]

    if "term_distance_threshold" in repo_parameters:
      TERM_DISTANCE_THRESHOLD = repo_parameters["term_distance_threshold"]

    if "project_prefixes" in repo_parameters:
      PROJECT_PREFIXES = repo_parameters["project_prefixes"]

    if "blocking_errors" in repo_parameters:
      BLOCKING_ERRORS = repo_parameters["blocking_errors"]

    if "gist_index" in repo_parameters:
      GIST_INDEX = repo_parameters["gist_index"]

    SKIPPED_ERRORS = repo_parameters["skipped_errors"] if "skipped_errors" in repo_parameters else []

    SKIPPED_TESTS = repo_parameters["skipped_tests"] if "skipped_tests" in repo_parameters else []

    SKIPPED_SUBJECTS = [
      (
        abspath(f"{ROOT_FOLDER}{sep}{path}")
        if exists(f"{ROOT_FOLDER}{sep}{path}")
        else path
      )
      for path in repo_parameters["skipped_subjects"]
    ] if "skipped_subjects" in repo_parameters else []

    TESTED_MODULES = [
      file for file in MODULES_TTL_GLOB_PATH
      if not abspath(file) in SKIPPED_SUBJECTS
    ]

    TESTED_MODELETS = [
      file for file in MODELETS_TTL_GLOB_PATH
      if not abspath(file) in SKIPPED_SUBJECTS
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

    SKIP_FOR_SUBJECT = {
      (
        abspath(f"{ROOT_FOLDER}{sep}{file}")
        if exists(f"{ROOT_FOLDER}{sep}{file}")
        else file
      ): criterions
      for file, criterions
      in repo_parameters["skip_for_subject"].items()
    } if "skip_for_subject" in repo_parameters else {}

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

  try:
    from .uris import *
  except:
    pass

  VARIABLE_REQUESTS = [
    "NOT_REFERENCED",
    "GET_BY_MODULE",
    "DOMAIN_OUT_OF_VOCABULARY",
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

ONTOLOGY_RDFLIB_NAMESPACE = None
"""Object representing the ontology namespace"""

ONTOLOGY_SEPARATOR: str = None
"""Last character from the end of the ontology namespace"""

if not ONTOLOGY_NAMESPACE is None:
  # The character separating the ontology base URL from the suffix
  ONTOLOGY_SEPARATOR = ONTOLOGY_NAMESPACE[-1]

if not BLOCKING_ERRORS is None:
  for error in ERROR_RESOURCES.keys():
    ERROR_RESOURCES[error]["blocking"] = error in BLOCKING_ERRORS

CRITERION_DATA: dict[str, dict[str, Union[str, list[str]]]] = None
"""Dictonary storing the criterions from the earl-olivaw dataset"""

try:
    from rdflib import Graph
    from rdflib.namespace import Namespace

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
              str(error)
              for line in criterions_graph.query(
                GET_ERRORS_OF_TEST.replace("CRITERION_ID", criterion_id)
              )
              for error in line
            ]
        }
        for criterion_id, criterion_title, criterion_description in criterions
    }
    CRITERION_IDS = list(CRITERION_DATA.keys())
except:
  pass

MODEL_BEST_PRACTICES_TESTS: list[str] = ["owl-rl-constraint", "profile-compatibility", "term-referencing", "domain-and-range-referencing", "terms-differenciation", "labeled-terms"]
"""Set of model tests that rely on the syntax test to pass"""