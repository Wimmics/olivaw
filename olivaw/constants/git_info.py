from subprocess import check_output
from os.path import relpath, sep

from sys import argv, exit

modes = [
  item.split('=')[1]
  for item in argv
  if item.startswith("--mode=")
]
MODE = modes[0] if len(modes) > 0 else "manual"

arg_root = [item.split("=")[1] for item in argv if item.startswith("--REPO-ROOT=")]

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

REPO_NAME = REPO_URI.split('/')[-1]

# Base reporitory platform URL
PLATFORM_URL = "/".join(REPO_URI.split("/")[:-2])

REPO_REF = REPO_URI[len(PLATFORM_URL) + 1:]

# The current branch
arg_branch = [item.split("=")[1] for item in argv if item.startswith("--BRANCH=")]

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

# The currrent ref
arg_ref = [item.split("=")[1] for item in argv if item.startswith("--REF=")]

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

IS_PROFILE_FOLDER_PWD = PATH_TO_PROFILE_FOLDER == "." or PATH_TO_PROFILE_FOLDER == f".{sep}"

# The path to the profile check README.md
PROFILE_CHECK_URI = f"{REPO_URI}/blob/{BRANCH}/{'' if IS_PROFILE_FOLDER_PWD else PATH_TO_PROFILE_FOLDER}"

arg_dev_username = [item.split("=")[1] for item in argv if item.startswith("--DEV_USERNAME=")]

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
DOMAINS_URL = SRC_URL.replace("src", "domains")
USECASES_URL = SRC_URL.replace("src", "use-cases")

OLIVAW_REF = "Wimmics/olivaw"

SHAPE_BASE_URIS = None

OLIVAW_EARL_DATASET = "https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#"

GIT_RAW = "https://raw.githubusercontent.com"

try:
  SHAPE_BASE_URIS = f"{GIT_RAW}/{'/'.join(REPO_URI.split('/')[-2:])}/{BRANCH}/.acimov/custom-tests/"
except:
  pass