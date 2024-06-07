"""Olivaw installation script"""

from setuptools import setup, find_packages
from os.path import sep, exists
from urllib.request import urlopen

from olivaw.constants import CORESE_PYTHON_URL, CORESE_LOCAL_PATH

# Parse the requirements from requirements.txt
requirements = None
with open(f"{sep.join(__file__.split(sep)[:-1])}{sep}requirements.txt", "r") as requirementsFile:
    requirements = requirementsFile.readlines()
    requirements = [
        line.strip()
        for line in requirements
        if len(line.strip()) > 0
    ]

# Download the corese jar from inria website
if not exists(CORESE_LOCAL_PATH):
    with urlopen(CORESE_PYTHON_URL) as downloaded:
        with open(CORESE_LOCAL_PATH, "wb") as jar:
            jar.write(downloaded.read())

# Reading README.rst file for injection into python package long description
long_description = ""
with open("./README.rst", "r") as readme:
    long_description = readme.read()

setup(
    name='olivaw',
    description="Python framework for supporting agile ontology development",
    long_description=long_description,
    license="LGPL-2.1",
    keywords="semantics ontology",
    version="v0.0.5",
    packages=find_packages(include=["olivaw", "olivaw.*"]),
    package_data={'': ['*.json', '*.ttl', '*.lock', '*.txt', '*.jar']},
    install_requires=[requirements],
    entry_points = {
        "console_scripts": ["olivaw=olivaw.main:run"]
    },
    author='Nicolas Robert',
    author_email="nicolas_robert_31@hotmail.fr",
    url="https://github.com/Wimmics/olivaw",
    python_requires='>=3.8'
)