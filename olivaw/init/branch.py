from os.path import sep
from json import loads
from requests import get

from olivaw.constants import (
    ROOT_FOLDER,
    DEV_USERNAME,
    REPO_URI,
    REF,
    NEW_LINES
)

def badge_uri(gist_id, badge):
    ref = "_".join(REF.split("/")[1:])
    return f"https://img.shields.io/endpoint?url=https://gist.githubusercontent.com/{DEV_USERNAME}/{gist_id}/raw/{ref}_{badge}.json"

def init_branch():
    readme = None
    with open(f"{ROOT_FOLDER}{sep}README.md", "r") as readmeFile:
        readme = readmeFile.readlines()
    
    parameters = None
    with open(f"{ROOT_FOLDER}{sep}.acimov{sep}parameters.json", "r") as parametersFile:
        parameters = loads(parametersFile.read())
    
    gist_index = parameters["gist_index"]

    badges = ["Pass", "NotTested", "CannotTell", "MinorFail", "MajorFail", "EL", "QL", "RL"]

    readme = [
            f"![{badge} Badge]({badge_uri(gist_index, badge)})"
            for badge in badges[:5]
        ] + [" "] + [
            f"![{badge} Badge]({badge_uri(gist_index, badge)})"
            for badge in badges[5:]
        ] + [" "] + readme[10:]
    
    readme = NEW_LINES.sub("\n", "\n".join(readme))
    
    with open(f"{ROOT_FOLDER}{sep}README.md", "w") as readmeFile:
        readmeFile.write(readme)