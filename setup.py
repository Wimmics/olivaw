from setuptools import setup, find_packages
from os.path import sep

requirements = None
with open(f"{sep.join(__file__.split(sep)[:-1])}{sep}requirements.txt", "r") as requirementsFile:
    requirements = requirementsFile.readlines()
    requirements = [
        line.strip()
        for line in requirements
        if len(line.strip()) > 0
    ]

setup(
    name='olivaw',
    version='1.0',
    packages=find_packages(include=["olivaw", "olivaw.*"]),
    package_data={'': ['*.json', '*.ttl']},
    install_requires=[requirements],
    entry_points = {
        "console_scripts": ["olivaw=olivaw.main:run"]
    },
    author='Me',
    description='Set of tools meant for acimov structured projects',
    python_requires='>=3.8'
)