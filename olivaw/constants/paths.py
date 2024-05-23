from os import getcwd
from glob import glob
from os.path import sep, relpath

from .git_info import ROOT_FOLDER

##################
# Relative paths #
##################

# Path to the repository folder
PWD_TO_ROOT_FOLDER = f"{relpath(ROOT_FOLDER, getcwd())}{sep}"

# Path to the repository output folder
PWD_TO_OUTPUT_FOLDER = f"{PWD_TO_ROOT_FOLDER}.acimov{sep}output{sep}"

# Modules files in the repository
MODULES_TTL_GLOB_PATH = glob(f"{PWD_TO_ROOT_FOLDER}src{sep}**{sep}*.ttl", recursive=True)

# Modelets files in the repository
MODELETS_TTL_GLOB_PATH = glob(f"{PWD_TO_ROOT_FOLDER}domains{sep}*{sep}*{sep}onto.ttl")

# Dataset files in the repository
DATASETS_TTL_GLOB_PATH = glob(f"{PWD_TO_ROOT_FOLDER}domains{sep}*{sep}*{sep}dataset.ttl")

# Use case files in the repository
USE_CASES_TTL_GLOB_PATH = glob(f"{PWD_TO_ROOT_FOLDER}use-cases{sep}*{sep}**{sep}*.ttl", recursive=True)

# Competency questions files in the repository
QUESTIONS_GLOB_PATH = glob(f"{PWD_TO_ROOT_FOLDER}domains{sep}*{sep}*{sep}*.rq")

# Custom model test files in the repository
CUSTOM_MODEL_TESTS = f"{PWD_TO_ROOT_FOLDER}.acimov{sep}custom-tests{sep}model{sep}*.shacl"

# Custom data test files in the repository
CUSTOM_DATA_TESTS = f"{PWD_TO_ROOT_FOLDER}.acimov{sep}custom-tests{sep}data{sep}*.shacl"

# Path to the olivaw constants folder
PWD_TO_CONSTANTS = sep.join(__file__.split(sep)[:-1])

# Path to the olivaw subfolder
PWD_TO_OVILAW = sep.join(__file__.split(sep)[:-2])

# Path to the olivaw-earl dataset
PWD_TO_MODEL_TEST_ONTO = f"{PWD_TO_OVILAW}{sep}test{sep}olivaw-earl.ttl"

# Path to the repository custom-tests folder
PWD_TO_CUSTOM_TESTS = f"{PWD_TO_ROOT_FOLDER}.acimov{sep}custom-tests{sep}"