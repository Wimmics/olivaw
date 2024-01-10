from os.path import sep
from requests import get
from json import loads

from olivaw.constants import (
    ROOT_FOLDER,
    REPO_URI,
    DEV_USERNAME
)

def show_gists():
    parameters = None
    with open(f"{ROOT_FOLDER}/.acimov/parameters.json", "r") as parametersFile:
        parameters = loads(parametersFile.read())
    
    index = parameters["gist_index"]

    url = f"https://gist.githubusercontent.com/{DEV_USERNAME}/{index}/raw/{REPO_URI.split('/')[-1]}.json"
    response = get(url).text
    print(" ")
    print(url)
    print(" ")
    print(url)
    gists = loads(response)

    for badge, gist in gists.items():
        print(f"{badge}\t:\t{gist}")