"""Package managing any olivaw command starting with `olivaw init` """

___main__ = ["branch", "repo"]

from .branch import *
from .repo import *

from sys import exit

from olivaw.constants import REF

if REF is None:
    print('fatal: Command "git symbolic-ref HEAD" should return the current ref or parameter REF should be set')
    exit(1)