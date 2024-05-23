from subprocess import check_output
from os.path import relpath, sep

from sys import argv, exit

arg_root = [item.split("=")[1] for item in argv if item.startswith("--REPO-ROOT=")]

# Root folder of the current repository
ROOT_FOLDER = None
if len(arg_root) > 0:
  ROOT_FOLDER = arg_root[0]
else:
  try:
    ROOT_FOLDER = check_output(
      "git rev-parse --show-toplevel".split(" ")
    )\
    .decode("utf-8")\
    .strip()
  except:
    ROOT_FOLDER = None

if ROOT_FOLDER is None:
  # git will print an error message explaining we are no in a git reository
  exit(1)

# The repository URI
arg_repo = [item.split("=")[1] for item in argv if item.startswith("--REPO_URI=")]

# Repository origin URI
REPO_URI = None
if len(arg_repo) > 0:
  REPO_URI = arg_repo[0]
else:
  try:
    REPO_URI = check_output(
      "git config --get remote.origin.url".split(" ")
    )\
    .decode('utf-8')\
    .strip()
  except:
    pass

if REPO_URI is None:
  print('fatal: Command "git config --get remote.origin.url" should return the repository URI or argument "REPO_URI" should be set')

if REPO_URI.endswith("/"):
  REPO_URI = REPO_URI[:-1]

# Repository name
REPO_NAME = REPO_URI.split('/')[-1]

# Base reporitory platform URL
PLATFORM_URL = "/".join(REPO_URI.split("/")[:-2])

# Identifier of the current repository
REPO_REF = REPO_URI[len(PLATFORM_URL) + 1:]

# The current branch
arg_branch = [item.split("=")[1] for item in argv if item.startswith("--BRANCH=")]

# Current branch of the head repository
BRANCH = None
if len(arg_branch) > 0:
  BRANCH = arg_branch[0]
else:
  try:
    BRANCH = check_output(
      "git rev-parse --abbrev-ref HEAD".split(" ")
    )\
    .decode('utf-8')\
    .strip()
  except:
    BRANCH = None

arg_ref = [item.split("=")[1] for item in argv if item.startswith("--REF=")]

# The currrent repository ref
REF = None
if len(arg_ref) > 0:
  REF = arg_ref[0]
else:
  try:
    REF = check_output(
      "git symbolic-ref HEAD".split(" ")
    )\
    .decode('utf-8')\
    .strip()
  except:
    REF = None

# The relative path from root to the profile_test folder
PATH_TO_PROFILE_FOLDER = relpath(".", ROOT_FOLDER)

# Is the PWD at the root of the repository
IS_PROFILE_FOLDER_PWD = PATH_TO_PROFILE_FOLDER == "." or PATH_TO_PROFILE_FOLDER == f".{sep}"

arg_dev_username = [item.split("=")[1] for item in argv if item.startswith("--DEV_USERNAME=")]

# Name of the current developper
DEV_USERNAME = None
if len(arg_dev_username) > 0:
  DEV_USERNAME = arg_dev_username[0]
else:
  try:
    DEV_USERNAME = check_output(
      "git config --global user.name".split(" ")
    )\
    .decode('utf-8')\
    .strip()
  except:
    DEV_USERNAME = None

# URL prefix for the files in the current branch in src
SRC_URL = f"{REPO_URI}/blob/{BRANCH}/src/"

# URL prefix for the files in the current branch in domains folder
DOMAINS_URL = SRC_URL.replace("src", "domains")

# URL prefix for the files in the current branch in use-cases folder
USECASES_URL = SRC_URL.replace("src", "use-cases")

# Identifier of olivaw repository
OLIVAW_REF = "Wimmics/olivaw"

# Prefix of the URIs of the custom tests criterions and shapes
SHAPE_BASE_URIS = None

# Base URL for the files hosted on GitHub, on raw mode
GIT_RAW = "https://raw.githubusercontent.com"

# URI of the olivaw-earl dataset
OLIVAW_EARL_DATASET = f"{GIT_RAW}/{OLIVAW_REF}/main/olivaw/test/olivaw-earl.ttl#"

# URI prefix for the files in the test folder, in olivaw repository, on branch main 
OLIVAW_TEST_BLOB_URI = "https://github.com/Wimmics/olivaw/blob/main/olivaw/test"

try:
  SHAPE_BASE_URIS = f"{GIT_RAW}/{'/'.join(REPO_URI.split('/')[-2:])}/{BRANCH}/.acimov/custom-tests/"
except:
  pass