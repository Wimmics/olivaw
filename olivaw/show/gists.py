from os.path import sep
from requests import get
from json import loads

from olivaw.constants import (
    ROOT_FOLDER,
    REPO_URI,
    DEV_USERNAME
)

def show_gist():
    parameters = None
    with open(f"{ROOT_FOLDER}/.acimov/parameters.json", "r") as parametersFile:
        parameters = loads(parametersFile.read())
    
    index = parameters["gist_index"]
    print(index)