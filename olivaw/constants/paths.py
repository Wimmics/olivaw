from os import getcwd
from glob import glob
from os.path import sep, relpath

from .git_info import ROOT_FOLDER

##################
# Relative paths #
##################

PWD_TO_ROOT_FOLDER = f"{relpath(ROOT_FOLDER, getcwd())}{sep}"
PWD_TO_OUTPUT_FOLDER = f"{PWD_TO_ROOT_FOLDER}.acimov{sep}output{sep}"
PWD_TO_MODEL_TEST = f"{PWD_TO_ROOT_FOLDER}.acimov{sep}test{sep}model{sep}"
MODULES_TTL_GLOB_PATH = glob(f"{PWD_TO_ROOT_FOLDER}src{sep}**{sep}*.ttl", recursive=True)
MODELETS_TTL_GLOB_PATH = glob(f"{PWD_TO_ROOT_FOLDER}domains{sep}*{sep}*{sep}onto.ttl")
DATASETS_TTL_GLOB_PATH = glob(f"{PWD_TO_ROOT_FOLDER}domains{sep}*{sep}*{sep}dataset.ttl")
USE_CASES_TTL_GLOB_PATH = glob(f"{PWD_TO_ROOT_FOLDER}use-cases{sep}*{sep}**{sep}*.ttl", recursive=True)
QUESTIONS_GLOB_PATH = glob(f"{PWD_TO_ROOT_FOLDER}domains{sep}*{sep}*{sep}*.rq")

CUSTOM_MODEL_TESTS = f"{PWD_TO_ROOT_FOLDER}.acimov{sep}custom-tests{sep}model{sep}*.shacl"
CUSTOM_DATA_TESTS = f"{PWD_TO_ROOT_FOLDER}.acimov{sep}custom-tests{sep}data{sep}*.shacl"

PWD_TO_CONSTANTS = sep.join(__file__.split(sep)[:-1])
PWD_TO_OVILAW = sep.join(__file__.split(sep)[:-2])
PWD_TO_MODEL_TEST_ONTO = f"{PWD_TO_OVILAW}{sep}test{sep}olivaw-earl.ttl"

PWD_TO_CUSTOM_TESTS = f"{PWD_TO_ROOT_FOLDER}.acimov{sep}custom-tests{sep}"