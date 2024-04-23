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

try:
    common_prefixes = None

    # This site uses self signed certificate
    myssl = create_default_context()
    myssl.check_hostname = False
    myssl.verify_mode = CERT_NONE
    
    with urlopen(PREFIX_CC_PREFIXES, context=myssl) as downloaded:
        common_prefixes = loads(downloaded.read().decode())

    common_prefixes = common_prefixes["@context"]
    uris = list(common_prefixes.items())

    COMMON_URIS_TREE = make_index(uris)
    with open(f"{PWD_TO_CONSTANTS}{sep}uri_index.json", "w") as f:
        f.write(dumps(COMMON_URIS_TREE))
except:
    with open(f"{sep.join(__file__.split(sep)[:-1])}{sep}uri_index.json", "r") as f:
        COMMON_URIS_TREE = loads(f.read())
        parse_tree_to_tuple_leaves(COMMON_URIS_TREE)