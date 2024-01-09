from os.path import sep
from json import loads
from requests import get

from olivaw.constants import (
    ROOT_FOLDER,
    DEV_USERNAME,
    REPO_URI,
    REF
)

def badge_uri(gist_id):
    suffix = "__".join(REF.split("/")[1:])
    return f"https://img.shields.io/endpoint?url=https://gist.githubusercontent.com/{DEV_USERNAME}/{gist_id}/raw/{REPO_URI.split('/')[-1]}__{suffix}.json"

def init_branch():
    readme = None
    with open(f"{ROOT_FOLDER}{sep}README.md", "r") as readmeFile:
        readme = readmeFile.readlines()
    
    parameters = None
    with open(f"{ROOT_FOLDER}{sep}.acimov{sep}parameters.json", "r") as parametersFile:
        parameters = loads(parametersFile.read())
    
    gist_index = parameters["gist_index"]
    project_name = REPO_URI.split('/')[-1]
    gist_url = f"https://gist.githubusercontent.com/{DEV_USERNAME}/{gist_index}/raw/{project_name}.json"

    get_gists = get(gist_url)
    gists = loads(get_gists.text)

    badges = ["Pass", "NotTested", "CannotTell", "MinorFail", "MajorFail", "OWL EL", "OWL QL", "OWL RL"]

    readme = [
            f"![{item} Badge]({badge_uri(gists[item.replace(' ', '').upper()])})"
            for item in badges[5:]
        ] + [" "] + [
            f"![{item} Badge]({badge_uri(gists[item.replace(' ', '').upper()])})"
            for item in badges[:5]
        ] + [" "] + readme[4:]
    
    readme = "\n".join(readme)
    
    with open(f"{ROOT_FOLDER}{sep}README.md", "w") as readmeFile:
        readmeFile.write(readme)