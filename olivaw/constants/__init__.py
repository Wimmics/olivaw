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

from .olivaw import *

try:
  from .rdflib_info import *
  from .markdown import *
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

MODE: str = modes[0].upper() if len(modes) > 0 else "MANUAL"
"""The execution mode that will drive some olivaw behaviour, default is manual"""

MANUAL: str = MODE == "MANUAL"
"""Indicates if olivaw is in manual mode"""

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

if not PWD_TO_CONSTANTS is None:
  with open(f"{PWD_TO_CONSTANTS}{sep}error-resources.json", "r") as f:
    ERROR_RESOURCES = load(f)

ERROR_IDS: list[str] = list(ERROR_RESOURCES.keys()) if not ERROR_RESOURCES is None else []
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

SKIPPED_ERRORS: list[str] = []
"""Error identifiers for errors that should not be written in the reports"""

SKIPPED_TESTS: list[str] = []
"""Test identifiers that should not be written in the reports"""

SKIPPED_SUBJECTS: list[str] = []
"""Subject identifiers or relative paths from repo root to files that should be skipped in tests"""

SKIP_FOR_TEST: dict[str, list[str]] = None
"""Dictionary of tests identifier linked to test that should not be run for this subject"""

SKIP_FOR_SUBJECT: dict[str, list[str]] = None
"""Dictionary of subjects (subjects identifiers or relative paths from repo root to files) that are linked to tests that should not be run on it"""

TESTED_MODULES: list[dict[str, str]] = []
"""List of all the modules that should be tested"""

TESTED_MODELETS: list[dict[str, str]] = None
"""List of all the modelets that should be tested"""

TESTED_DATASETS: list[dict[str, str]] = None
"""List of all the datasets that should be tested"""

TESTED_USE_CASES: list[dict[str, str]] = None
"""List of all the use cases that should be tested"""

TESTED_QUERIES: list[dict[str, str]] = None
"""List of all the queries that should be tested"""

VARIABLE_REQUESTS: list[str] = None
"""SPARQL request that rely on some repository data"""

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

    if "modules_definition" in repo_parameters:
      MODULES_DEFINITION = repo_parameters["modules_definition"]

    if "modelets_definition" in repo_parameters:
      MODULES_DEFINITION = repo_parameters["modelets_definition"]

    if "datasets_definition" in repo_parameters:
      MODULES_DEFINITION = repo_parameters["datasets_definition"]

    if "usecases_definition" in repo_parameters:
      MODULES_DEFINITION = repo_parameters["usecases_definition"]

    if "queries_definition" in repo_parameters:
      MODULES_DEFINITION = repo_parameters["queries_definition"]

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
"""Dictonary storing the criterions from the olivaw ontology"""

MODULES: list[dict[str, str]] = []
"""Definition of the different *modules* present in the current project

This variable is a list of `dict`, each of them with the following key/value pairs:
- **file**(`str`): Relative path to the *module* file, stored as `str` 
- **module**(`str`): Given name of this *module*, stored as `str` 
"""

MODELETS: list[dict[str, str]] = []
"""Definition of the different *modelets* present in the current project

This variable is a list of `dict`, each of them with the following key/value pairs:
- **file**(`str`): Relative path to the *modelet* file
- **domain**(`str`): Given name of this *modelet*'s *domain*
- **scenario**(`str`): Given name of this *modelet*'s *scenario*
"""

DATASETS: list[dict[str, str]] = []
"""Definition of the different *datasets* present in the current project

This variable is a list of `dict`, each of them with the following key/value pairs:
- **file**(`str`): Relative path to the *dataset* file 
- **domain**(`str`): Given name of this *dataset*'s *domain*
- **scenario**(`str`): Given name of this *dataset*'s *scenario*
"""

QUERIES: list[dict[str, str]] = []
"""Definition of the different *queries* present in the current project

This variable is a list of `dict`, each of them with the following key/value pairs:
- **file** (`str`): Relative path to the *query* file
- **domain** (`str`): Given name of this *query*'s *domain*
- **scenario** (`str`): Given name of this *query*'s *scenario*
- **question** (`str`): Given name of this *query*'s *competency question*
"""

USE_CASES: list[dict[str, str]] = []
"""Definition of the different *use cases* present in the current project

This variable is a list of `dict`, each of them with the following key/value pairs:
- **file** (`str`): Relative path to the *use case* file
- **domain** (`str`): Given name of this *use case*'s *domain*
- **scenario** (`str`): Given name of this *use case*'s *scenario*
- **question** (`str`): Given name of this *use case*'s *competency question*
"""
 
try:
  import regex as re
  from glob import glob
  from json import dumps
  from os.path import relpath

  def retrieve_path_pattern(pattern, path):
    matches = next(
      iter(re.findall(pattern, relpath(path, PWD_TO_ROOT_FOLDER))[:1]),
      path
    )
    result = matches[0] if isinstance(matches, tuple) else matches
    return result[2 if result[:2] in ["./", ".\\"] else 0:].replace("/", "-").replace("\\", "-")
  
  resources=[
    ("MODULES", "module"),
    ("MODELETS", "modelet"),
    ("DATASETS", "dataset"),
    ("QUERIES", "query"),
    ("USE_CASES", "use-case")
  ]
  
  for (variable_name, resource_name) in resources:
    locals()[variable_name]=[]
    definitions = locals()[f"{variable_name}_DEFINITION"]

    for definition in definitions:
      try:
        locals()[variable_name].extend([
          {
            **{
              "file": f"{abspath(PWD_TO_ROOT_FOLDER)}{sep}{relpath(match, PWD_TO_ROOT_FOLDER)}",
              "type": resource_name
            },
            **{
              variable: retrieve_path_pattern(pattern, match)
              for variable, pattern in definition["patterns"].items()
            }
          }
          for match in glob(f"{PWD_TO_ROOT_FOLDER}/{definition['glob']}", recursive=True)
          if not "domain-template" in match
        ])
      except Exception as e:
        if not ACTIONS:
          print(f"Error: Could not parse resource {resource_name}.\n\tmessage: {str(e)}\n\tglob: {definition['glob']}\n\tpatterns:{str(definition['patterns'])}")

    locals()[f"TESTED_{variable_name}"]=[
      resource_item
      for resource_item in locals()[variable_name]
      if not resource_item["file"] in SKIPPED_SUBJECTS
    ]

    #print(dumps(locals()[f"TESTED_{variable_name}"], indent=4))
    
except:
  pass

try:
    from rdflib import Graph
    from rdflib.namespace import Namespace, DCTERMS

    if not ONTOLOGY_NAMESPACE is None:
      ONTOLOGY_RDFLIB_NAMESPACE = Namespace(ONTOLOGY_NAMESPACE)
    criterions_graph = Graph()
    criterions_graph.parse(PWD_TO_OLIVAW_ONTOLOGY)
    criterions_graph.bind("dcterms", DCTERMS)
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