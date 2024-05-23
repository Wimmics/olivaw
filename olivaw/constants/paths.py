"""Module providing constants related to project files paths"""

from os import getcwd
from glob import glob
from os.path import sep, relpath

from .git_info import ROOT_FOLDER

##################
# Relative paths #
##################

PWD_TO_ROOT_FOLDER: str = f"{relpath(ROOT_FOLDER, getcwd())}{sep}"
"""Path to the repository folder"""

PWD_TO_OUTPUT_FOLDER: str = f"{PWD_TO_ROOT_FOLDER}.acimov{sep}output{sep}"
"""Path to the repository output folder"""

MODULES_TTL_GLOB_PATH: list[str] = glob(f"{PWD_TO_ROOT_FOLDER}src{sep}**{sep}*.ttl", recursive=True)
"""Modules files in the repository"""

MODELETS_TTL_GLOB_PATH: list[str] = glob(f"{PWD_TO_ROOT_FOLDER}domains{sep}*{sep}*{sep}onto.ttl")
"""Modelets files in the repository"""

DATASETS_TTL_GLOB_PATH: list[str] = glob(f"{PWD_TO_ROOT_FOLDER}domains{sep}*{sep}*{sep}dataset.ttl")
"""Dataset files in the repository"""

USE_CASES_TTL_GLOB_PATH: list[str] = glob(f"{PWD_TO_ROOT_FOLDER}use-cases{sep}*{sep}**{sep}*.ttl", recursive=True)
"""Use case files in the repository"""

QUESTIONS_GLOB_PATH: list[str] = glob(f"{PWD_TO_ROOT_FOLDER}domains{sep}*{sep}*{sep}*.rq")
"""Competency questions files in the repository"""

CUSTOM_MODEL_TESTS: str = f"{PWD_TO_ROOT_FOLDER}.acimov{sep}custom-tests{sep}model{sep}*.shacl"
"""Custom model test files in the repository"""

CUSTOM_DATA_TESTS: str = f"{PWD_TO_ROOT_FOLDER}.acimov{sep}custom-tests{sep}data{sep}*.shacl"
"""Custom data test files in the repository"""

PWD_TO_CONSTANTS: str = sep.join(__file__.split(sep)[:-1])
"""Path to the olivaw constants folder"""

PWD_TO_OVILAW: str = sep.join(__file__.split(sep)[:-2])
"""Path to the olivaw subfolder"""

PWD_TO_MODEL_TEST_ONTO: str = f"{PWD_TO_OVILAW}{sep}test{sep}olivaw-earl.ttl"
"""Path to the olivaw-earl dataset"""

PWD_TO_CUSTOM_TESTS: str = f"{PWD_TO_ROOT_FOLDER}.acimov{sep}custom-tests{sep}"
"""Path to the repository custom-tests folder"""