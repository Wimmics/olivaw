"""Module providing constants related to project files paths"""

from os import getcwd
from typing import Union
from glob import glob
from os.path import sep, relpath

from .git_info import ROOT_FOLDER

##################
# Relative paths #
##################

PWD_TO_ROOT_FOLDER: str = f"{relpath(ROOT_FOLDER, getcwd())}{sep}" if not ROOT_FOLDER is None else None
"""Path to the repository folder"""

PWD_TO_OUTPUT_FOLDER: str = f"{PWD_TO_ROOT_FOLDER}.acimov{sep}output{sep}" if not ROOT_FOLDER is None else None
"""Path to the repository output folder"""

MODULES_TTL_GLOB_PATH: list[str] = glob(f"{PWD_TO_ROOT_FOLDER}src{sep}**{sep}*.ttl", recursive=True) if not ROOT_FOLDER is None else None
"""Modules files in the repository"""

MODELETS_TTL_GLOB_PATH: list[str] = glob(f"{PWD_TO_ROOT_FOLDER}domains{sep}*{sep}*{sep}onto.ttl") if not ROOT_FOLDER is None else None
"""Modelets files in the repository"""

DATASETS_TTL_GLOB_PATH: list[str] = glob(f"{PWD_TO_ROOT_FOLDER}domains{sep}*{sep}*{sep}dataset.ttl") if not ROOT_FOLDER is None else None
"""Dataset files in the repository"""

USE_CASES_TTL_GLOB_PATH: list[str] = glob(f"{PWD_TO_ROOT_FOLDER}use-cases{sep}*{sep}**{sep}*.ttl", recursive=True) if not ROOT_FOLDER is None else None
"""Use case files in the repository"""

QUESTIONS_GLOB_PATH: list[str] = glob(f"{PWD_TO_ROOT_FOLDER}domains{sep}*{sep}*{sep}*.rq") if not ROOT_FOLDER is None else None
"""Competency questions files in the repository"""

CUSTOM_MODEL_TESTS: str = f"{PWD_TO_ROOT_FOLDER}.acimov{sep}custom-tests{sep}model{sep}*.shacl" if not ROOT_FOLDER is None else None
"""Custom model test files in the repository"""

CUSTOM_DATA_TESTS: str = f"{PWD_TO_ROOT_FOLDER}.acimov{sep}custom-tests{sep}data{sep}*.shacl" if not ROOT_FOLDER is None else None
"""Custom data test files in the repository"""

PWD_TO_CONSTANTS: str = sep.join(__file__.split(sep)[:-1]) if not ROOT_FOLDER is None else None
"""Path to the olivaw constants folder"""

PWD_TO_OVILAW: str = sep.join(__file__.split(sep)[:-2]) if not ROOT_FOLDER is None else None
"""Path to the olivaw subfolder"""

PWD_TO_OLIVAW_ONTOLOGY: str = f"{PWD_TO_OVILAW}{sep}test{sep}olivaw.ttl" if not ROOT_FOLDER is None else None
"""Path to the olivaw ontology"""

PWD_TO_CUSTOM_TESTS: str = f"{PWD_TO_ROOT_FOLDER}.acimov{sep}custom-tests{sep}" if not ROOT_FOLDER is None else None
"""Path to the repository custom-tests folder"""


#####################################
# Setting generalization for v0.0.8 #
#####################################
MODULES_DEFINITION: list[dict[str,Union[str, dict[str, str]]]] = [
    {
        "glob": f"src{sep}**{sep}*.ttl",
        "patterns": {"module": "src[\\\\/](([^\\\\/]+[\\\\/]?)+)\\.ttl$"}
    }
]
"""Represents the useful information to find and identify each _module_ in the current project.

Each array element is a dictionary representing some criterias identifyng some resources as `modules`.

In each of theses dictionaries:
- **glob** key containing a `str` that is a glob path pointing to some resources that are assumed as _modules_ (paths are expressed as relative to project root folder),
- **patterns** key containing a `dict` containing different regexes, each of them helping to identify some key information in a _module_ path that complies to the above **glob**. In this dictionary:
    - **module**: A `str` containing a regex that matches the _module_ name in the file path

Default value, in case the value was not set in the parameter file:

```
[
    {
        "glob": "src/**/*.ttl",
        "patterns": {"module": "src[\\\\\\/](([^\\\\\\/]+[\\\\\\/]?)+)\\.ttl$"}
    }
]
```
"""

MODELETS_DEFINITION: list[dict[str,Union[str, dict[str, str]]]] = [
    {
        "glob": f"domains{sep}*{sep}*{sep}onto.ttl",
        "patterns": {
            "domain": "[\\\\/]([^\\\\/]+)[\\\\/][^\\\\/]+[\\\\/]onto\\.ttl$",
            "scenario": "[\\\\/]([^\\\\/]+)[\\\\/]onto\\.ttl$"
        }
    }
]
"""Represents the useful information to find and identify each _modelet_ in the current project.

Each array element is a dictionary representing some criterias identifyng some resources as `modules`.

In each of theses dictionaries:
- **glob** key containing a `str` that is a glob path pointing to some resources that are assumed as _modelet_ (paths are expressed as relative to project root folder),
- **patterns** key containing a `dict` containing different regexes, each of them helping to identify some key information in a _modelet_ path that complies to the above **glob**. In this dictionary:
    - **domain**: A `str` containing a regex that matches the _domain_ name in the file path
    - **scenario**: A `str` containing a regex that matches the _scenario_ name in the file path

Default value, in case the value was not set in the parameter file:

```
[
    {
        "glob": "domains/*/*/onto.ttl",
        "patterns": {
            "domain": "[\\\\\\/]([^\\\\\\/]+)[\\\\\\/][^\\\\\\/]+[\\\\\\/]onto\\.ttl$",
            "scenario": "[\\\\\/]([^\\\\\\/]+)[\\\\\\/]onto\\.ttl$"
        }
    }
]
```
"""

DATASETS_DEFINITION: list[dict[str,Union[str, dict[str, str]]]] = [
    {
        "glob": f"domains{sep}*{sep}*{sep}dataset.ttl",
        "patterns": {
            "domain": "[\\\\/]([^\\\\/]+)[\\\\/][^\\\\/]+[\\\\/]dataset\\.ttl$",
            "scenario": "[\\\\/]([^\\\\/]+)[\\\\/]dataset\\.ttl$"
        }
    }
]
"""Represents the useful information to find and identify each _dataset_ in the current project.

Each array element is a dictionary representing some criterias identifyng some resources as `dataset`.

In each of theses dictionaries:
- **glob** key containing a `str` that is a glob path pointing to some resources that are assumed as _dataset_ (paths are expressed as relative to project root folder),
- **patterns** key containing a `dict` containing different regexes, each of them helping to identify some key information in a _dataset_ path that complies to the above **glob**. In this dictionary:
    - **domain**: A `str` containing a regex that matches the _domain_ name in the file path
    - **scenario**: A `str` containing a regex that matches the _scenario_ name in the file path

Default value, in case the value was not set in the parameter file:

```
[
    {
        "glob": "domains/*/*/dataset.ttl",
        "patterns": {
            "domain": "[\\\\\\/]([^\\\\\\/]+)[\\\\\\/][^\\\\\\/]+[\\\\\\/]dataset\\.ttl$",
            "scenario": "[\\\\\\/]([^\\\\\\/]+)[\\\\\\/]dataset\\.ttl$"
        }
    }
]
```
"""

QUERIES_DEFINITION: list[dict[str,Union[str, dict[str, str]]]] = [
    {
        "glob": f"domains{sep}*{sep}*{sep}*.rq",
        "patterns": {
            "domain": "[\\\\/]([^\\\\/]+)[\\\\/][^\\\\/]+[\\\\/][^\\\\/]+\\.rq$",
            "scenario": "[\\\\/]([^\\\\/]+)[\\\\/][^\\\\/]+\\.rq$",
            "question": "[\\\\/]([^\\\\/]+)\\.rq$"
        }
    }
]
"""Represents the useful information to find and identify each _query_ in the current project.

Each array element is a dictionary representing some criterias identifyng some resources as `query`.

In each of theses dictionaries:
- **glob** key containing a `str` that is a glob path pointing to some resources that are assumed as _query_ (paths are expressed as relative to project root folder),
- **patterns** key containing a `dict` containing different regexes, each of them helping to identify some key information in a _query_ path that complies to the above **glob**. In this dictionary:
    - **domain**: A `str` containing a regex that matches the _domain_ name in the file path
    - **scenario**: A `str` containing a regex that matches the _scenario_ name in the file path
    - **question**: A `str` containing a regex that matches the *competency question* name in the file path

Default value, in case the value was not set in the parameter file:

```
[
    {
        "glob": "domains/*/*/*.rq",
        "patterns": {
            "domain": "[\\\\\\/]([^\\\\\\/]+)[\\\\\\/][^\\\\\\/]+[\\\\\\/][^\\\\\\/]+\\.rq$",
            "scenario": "[\\\\\\/]([^\\\\\\/]+)[\\\\\\/][^\\\\\\/]+\\.rq$",
            "question": "[\\\\\\/]([^\\\\\\/]+)\\.rq$"
        }
    }
]
```
"""

USE_CASES_DEFINITION: list[dict[str,Union[str, dict[str, str]]]] = [
    {
        "glob": f"use-cases{sep}*{sep}**{sep}*.ttl",
        "patterns": {
            "use-case": "^use-cases[\\\\/]([^\\\\/]+)[\\\\/]",
            "fragment": "use-cases[\\\\/][^\\\\/]+[\\\\/](([^\\\\/]+[\\\\/]?)+)\\.ttl$"
        }
    }
]
"""Represents the useful information to find and identify each _query_ in the current project.

Each array element is a dictionary representing some criterias identifyng some resources as `query`.

In each of theses dictionaries:
- **glob** key containing a `str` that is a glob path pointing to some resources that are assumed as _query_ (paths are expressed as relative to project root folder),
- **patterns** key containing a `dict` containing different regexes, each of them helping to identify some key information in a _query_ path that complies to the above **glob**. In this dictionary:
    - **domain**: A `str` containing a regex that matches the _domain_ name in the file path
    - **scenario**: A `str` containing a regex that matches the _scenario_ name in the file path
    - **question**: A `str` containing a regex that matches the *competency question* name in the file path

Default value, in case the value was not set in the parameter file:

```
[
    {
        "glob": "use-cases/*/**/*.ttl",
        "patterns": {
            "use-case": "^use-cases[\\\\\\/]([^\\\\\\/]+)[\\\\\\/]",
            "fragment": "use-cases[\\\\\\/](([^\\\\\\/]+[\\\\\\/]?)+)\\.ttl$"
        }
    }
]
```
"""
