"""Package managing any olivaw commands starting with `olivaw test` """

__main__ = ["model", "data"]

from sys import exit

from os import makedirs
from os.path import exists

from olivaw.constants import (
    ONTOLOGY_PREFIX,
    ONTOLOGY_NAMESPACE,
    TERM_DISTANCE_THRESHOLD,
    BLOCKING_ERRORS,
    BRANCH,
    PWD_TO_OUTPUT_FOLDER,
    COMMIT_HASH
)

errors = []

if ONTOLOGY_PREFIX is None:
    errors.append("ONTOLOGY_PREFIX")

if ONTOLOGY_NAMESPACE is None:
    errors.append("ONTOLOGY_NAMESPACE")

if TERM_DISTANCE_THRESHOLD is None:
    errors.append("TERM_DISTANCE_THRESHOLD")

if BLOCKING_ERRORS is None:
    errors.append("BLOCKING_ERRORS")

errors = [
    f'fatal: parameter "{variable.lower()}" not found in parameters.json'
    for variable in errors
]

if len(errors) > 0:
    print("\n".join(errors))
    exit(1)

if BRANCH is None:
    print('fatal: Command "git rev-parse --abbrev-ref HEAD" should return the current branch or BRANCH option should be set')
    exit(1)

if COMMIT_HASH is None:
    print('fatal: Command "git rev-parse origin/HEAD" should return the current commit hash or argument "COMMIT_HASH" should be set')
    exit(1)

if not exists(PWD_TO_OUTPUT_FOLDER):
        makedirs(PWD_TO_OUTPUT_FOLDER)