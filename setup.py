from setuptools import setup, find_packages

requirements = None
with open("requirements.txt", "r") as requirementsFile:
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
    install_requires=[requirements],
    entry_points = {
        "console_scripts": ["olivaw=olivaw.main:run"]
    },
    author='Me',
    description='Set of tools meant for acimov structured projects',
    python_requires='>=3.8'
)