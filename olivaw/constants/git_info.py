"""Module providing constants related to the git information of the project and the developper"""

from subprocess import check_output, Popen, PIPE
from sys import argv, builtin_module_names, exit

from .olivaw import VERSION

arg_root = [item.split("=")[1] for item in argv if item.startswith("--REPO_ROOT=")]

ROOT_FOLDER: str = None
"""Root folder of the current repository"""

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
  # git will print an error message explaining program working directory is not in a git repository
  exit(1)

# The repository URI
arg_repo = [item.split("=")[1] for item in argv if item.startswith("--REPO_URI=")]

REPO_URI: str = None
"""Repository origin URI"""

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
    print('fatal: Command "git config --get remote.origin.url" should return the repository URI or argument "REPO_URI" should be set')
    exit(1)

# The repository state
REPO_STATE: str = None
"""Hash representing the current state of the local repository"""

arg_state = [item.split("=")[1] for item in argv if item.startswith("--REPO_STATE=")]

if len(arg_state) > 0:
  REPO_STATE = arg_state[0]
else:
  try:
    # Launch the process that will output current repo state
    snapshot = Popen(
      "git ls-files -m -d -s .".split(" "),
      stdout=PIPE
    )

    # Launch a hash process and inject as input the previous process output
    REPO_STATE = check_output(
      "git hash-object --stdin".split(" "),
      stdin=snapshot.stdout
    )\
    .decode("utf-8")\
    .strip()
    
    # Wait for snapshot process to end
    snapshot.wait()
  except:
    pass
  
if REPO_URI.endswith("/"):
  REPO_URI = REPO_URI[:-1]

REPO_NAME: str = REPO_URI.split('/')[-1]
"""Repository name"""

PLATFORM_URL: str = "/".join(REPO_URI.split("/")[:-2])
"""Base reporitory platform URL"""

REPO_REF: str = REPO_URI[len(PLATFORM_URL) + 1:]
"""Identifier of the current repository"""

# The current branch
arg_branch = [item.split("=")[1] for item in argv if item.startswith("--BRANCH=")]

BRANCH: str = None
"""Current branch of the head repository"""

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

# The current commit hash
COMMIT_HASH: str = None
"""Local repository commit hash"""

arg_hash = [item.split("=")[1] for item in argv if item.startswith("--COMMIT_HASH=")]

if len(arg_hash) > 0:
  COMMIT_HASH = arg_hash[0]
else:
  try:
    COMMIT_HASH = check_output(
      f"git rev-parse origin/{BRANCH}".split(" ")
    )\
    .decode('utf-8')\
    .strip()
  except:
    pass

# The commit date
arg_date = [item.split("=")[1] for item in argv if item.startswith("--COMMIT_DATE=")]

COMMIT_DATE: str = None
"""Local repository last commit date"""

if len(arg_date) > 0:
  COMMIT_DATE = arg_date[0]
else:
  try:
    COMMIT_DATE = check_output(
      f"git log -1 --format=%cd --date=format:%Y-%m-%dT%H:%M:%S {COMMIT_HASH}".split(" ")
    )\
    .decode('utf-8')\
    .strip()
  except:
    print('fatal: Command "git log -1 --format=%cd --date=format:%Y-%m-%dT%H:%M:%S {COMMIT_HASH}" should return the current last commit date or argument "COMMIT_DATE" should be set')
    exit(1)

# The repository ref
arg_ref = [item.split("=")[1] for item in argv if item.startswith("--REF=")]

REF: str = None
"""The current repository ref"""

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

arg_dev_username = [item.split("=")[1] for item in argv if item.startswith("--DEV_USERNAME=")]

DEV_USERNAME: str = None
"""Name of the current developper"""

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

SRC_URL: str = f"{REPO_URI}/blob/{BRANCH}/src/"
"""URL prefix for the files in the current branch in src"""

DOMAINS_URL: str = SRC_URL.replace("src", "domains")
"""URL prefix for the files in the current branch in domains folder"""

USECASES_URL: str = SRC_URL.replace("src", "use-cases")
"""URL prefix for the files in the current branch in use-cases folder"""

OLIVAW_REF: str = "Wimmics/olivaw"
"""Identifier of olivaw repository"""

OLIVAW_REPOSITORY: str = "https://github.com/Wimmics/olivaw"
"""URL to olivaw repository"""

SHAPE_BASE_URIS: str = None
"""Prefix of the URIs of the custom tests criterions and shapes"""

GIT_RAW: str = "https://raw.githubusercontent.com"
"""Base URL for the files hosted on GitHub, on raw mode"""

OLIVAW_ONTOLOGY: str = f"https://ns.inria.fr/olivaw#"
"""URI of the olivaw ontology"""

OLIVAW_TEST_BLOB_URI: str = "https://github.com/Wimmics/olivaw/blob/main/olivaw/test"
"""URI prefix for the files in the test folder, in olivaw repository, on branch main"""

OLIVAW_VERSION_BLOB_URI: str = f"https://github.com/Wimmics/olivaw/blob/{VERSION}"
"""URI prefix for the files in olivaw project, on current tag"""

try:
  SHAPE_BASE_URIS = f"{GIT_RAW}/{'/'.join(REPO_URI.split('/')[-2:])}/{BRANCH}/.acimov/custom-tests/"
except:
  pass

ON_POSIX: bool = 'posix' in builtin_module_names
"""Boolean stating if the current OS is Linux based"""