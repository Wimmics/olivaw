__main__ = ["model", "data"]

from olivaw.constants import BRANCH
from sys import exit

if BRANCH is None:
    print('fatal: Command "git rev-parse --abbrev-ref HEAD" should return the current branch or BRANCH option should be set')
    exit(1)