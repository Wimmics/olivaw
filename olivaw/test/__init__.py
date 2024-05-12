__main__ = ["model", "data"]

from sys import exit
from olivaw.constants import (
    ONTOLOGY_PREFIX,
    ONTOLOGY_NAMESPACE,
    TERM_DISTANCE_THRESHOLD,
    BLOCKING_ERRORS,
    BRANCH
)

required = [
    "ONTOLOGY_PREFIX",
    "ONTOLOGY_NAMESPACE",
    "TERM_DISTANCE_THRESHOLD",
    "BLOCKING_ERRORS"
]

errors = [
    f'fatal: parameter "{variable.lower()}" not found in parameters.json'
    for variable in required
    if locals()[variable] is None
]

if len(errors) > 0:
    print("\n".join(errors))
    exit(1)

if BRANCH is None:
    print('fatal: Command "git rev-parse --abbrev-ref HEAD" should return the current branch or BRANCH option should be set')
    exit(1)