from setuptools import setup, find_packages
from os.path import sep, exists
from urllib.request import urlopen

from olivaw.constants import CORESE_PYTHON_URL, CORESE_LOCAL_PATH

# Parse the requirements file
requirements = None
with open(f"{sep.join(__file__.split(sep)[:-1])}{sep}requirements.txt", "r") as requirementsFile:
    requirements = requirementsFile.readlines()
    requirements = [
        line.strip()
        for line in requirements
        if len(line.strip()) > 0
    ]

# Download the corese jar
if not exists(CORESE_LOCAL_PATH):
    with urlopen(CORESE_PYTHON_URL) as downloaded:
        with open(CORESE_LOCAL_PATH, "wb") as jar:
            jar.write(downloaded.read())

setup(
    name='olivaw',
    version='1.0',
    packages=find_packages(include=["olivaw", "olivaw.*"]),
    package_data={'': ['*.json', '*.ttl', '*.lock', '*.txt', '*.jar']},
    install_requires=[requirements],
    entry_points = {
        "console_scripts": ["olivaw=olivaw.main:run"]
    },
    author='Me',
    description='Set of tools meant for acimov structured projects',
    python_requires='>=3.8'
)