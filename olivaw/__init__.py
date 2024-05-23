"""Package providing features for supporting continuous integration and quality check over an Agile ontology development project"""

from os import makedirs
from os.path import exists

from olivaw.constants.paths import PWD_TO_OUTPUT_FOLDER

__all__ = ["main", "test", "init"]

if not exists(PWD_TO_OUTPUT_FOLDER):
        makedirs(PWD_TO_OUTPUT_FOLDER)