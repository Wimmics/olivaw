from os import getcwd
from os.path import sep, relpath, abspath

from .git_info import ROOT_FOLDER

##################
# Relative paths #
##################

PWD_TO_ROOT_FOLDER = f"{relpath(ROOT_FOLDER, getcwd())}{sep}"
PWD_TO_MODEL_OUTPUT_FOLDER = f"{PWD_TO_ROOT_FOLDER}.acimov{sep}output{sep}"
PWD_TO_MODEL_TEST = f"{PWD_TO_ROOT_FOLDER}.acimov{sep}test{sep}model{sep}"
MODULES_TTL_GLOB_PATH = f"{PWD_TO_ROOT_FOLDER}src{sep}*.ttl"
MODELETS_TTL_GLOB_PATH = f"{PWD_TO_ROOT_FOLDER}domains{sep}*{sep}*{sep}onto.ttl"
DATASETS_TTL_GLOB_PATH = f"{PWD_TO_ROOT_FOLDER}domains{sep}*{sep}*{sep}dataset.ttl"
USE_CASES_TTL_GLOB_PATH = f"{PWD_TO_ROOT_FOLDER}use-cases{sep}*{sep}*.ttl"

PWD_TO_OVILAW = sep.join(__file__.split(sep)[:-2])
PWD_TO_MODEL_TEST_ONTO = f"{PWD_TO_OVILAW}{sep}test{sep}olivaw-earl.ttl"