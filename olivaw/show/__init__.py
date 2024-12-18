"""Package managing any olivaw command starting with `olivaw show` """

__main__ = ["gist", "badges"]

from .gist import *
from .badges import *
from .util import *

if ROOT_FOLDER is None:
  # git will print an error message explaining program working directory is not in a git repository
  print("`olivaw show` commands need to be run inside a git repository")
  exit(1)