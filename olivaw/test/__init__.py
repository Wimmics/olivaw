__main__ = ["model", "data"]

from json import dumps, loads
from os import sep
from ssl import CERT_NONE, create_default_context
from sys import exit
from urllib.request import urlopen

from olivaw.constants import (
    BRANCH,
    PREFIX_CC_PREFIXES,
)
from olivaw.constants.paths import PWD_TO_CONSTANTS
from olivaw.test.util.prefix import make_index, parse_tree_to_tuple_leaves

if BRANCH is None:
    print('fatal: Command "git rev-parse --abbrev-ref HEAD" should return the current branch or BRANCH option should be set')
    exit(1)