__main__ = ["model", "data"]

from sys import exit
from olivaw.constants import BRANCH

if BRANCH is None:
    print('fatal: Command "git rev-parse --abbrev-ref HEAD" should return the current branch or BRANCH option should be set')
    exit(1)