from subprocess import check_output
from os.path import relpath, sep

from sys import argv

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
    REPO_URI = None

if REPO_URI.endswith("/"):
  REPO_URI = REPO_URI[:-1]

REPO_NAME = REPO_URI.split('/')[-1]

# Base reporitory platform URL
PLATFORM_URL = "/".join(REPO_URI.split("/")[:-2])

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


ACIMOV_MODEL_TEST_URI = f"https://github.com/Wimmics/olivaw/blob/main/olivaw/test/olivaw-earl.ttl"
# URL prefix for the files in the current branch in src
SRC_URL = f"{REPO_URI}/blob/{BRANCH}/src/"
DOMAINS_URL = SRC_URL.replace("src", "domains")
USECASES_URL = SRC_URL.replace("src", "use-cases")