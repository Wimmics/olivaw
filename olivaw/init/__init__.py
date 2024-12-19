"""Package managing any olivaw command starting with `olivaw init` """

___main__ = ["branch", "repo"]

from sys import exit
from olivaw.constants import REF, ROOT_FOLDER, REPO_URI

if ROOT_FOLDER is None:
  # git will print an error message explaining program working directory is not in a git repository
  print("`olivaw init` commands need to be run inside a git repository")
  exit(1)

if REF is None:
    print('fatal: Command "git symbolic-ref HEAD" should return the current ref or parameter REF should be set')
    exit(1)

if REPO_URI is None:
    print('fatal: Command "git config --get remote.origin.url" should return the repository URI or argument "REPO_URI" should be set')
    exit(1)

from .branch import *
from .repo import *