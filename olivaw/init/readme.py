from os import sep
from json import loads

from olivaw.constants import (
    ROOT_FOLDER,
    BADGE_LIST,
    DEV_USERNAME,
    NEW_LINES,
    GIST_INDEX
)
from olivaw.init.util.badge import badge_url

def update_readme(gist_id=None):
    readme = None
    with open(f"{ROOT_FOLDER}{sep}README.md", "r") as readmeFile:
        readme = readmeFile.readlines()

    first_title_line = [
        i
        for i in range(len(readme))
        if readme[i].strip()[:2] == "# "
    ][0]

    if gist_id is None:
        gist_id = GIST_INDEX

    readme = ["Profiles:\t"] + [
        f"![{BADGE_LIST[badge]['label']} Badge]({badge_url(DEV_USERNAME, gist_id, badge)})"
        for badge in list(BADGE_LIST.keys())[5:8]
    ] + [" "] + ["Model tests:\t"] + [
        f"![{BADGE_LIST[badge]['label']} Badge]({badge_url(DEV_USERNAME, gist_id, badge)})"
        for badge in list(BADGE_LIST.keys())[:5]
    ] + [" "] + ["Data tests:\t"] + [
        f"![{BADGE_LIST[badge]['label']} Badge]({badge_url(DEV_USERNAME, gist_id, badge)})"
        for badge in list(BADGE_LIST.keys())[8:]
    ] + [" "] + readme[first_title_line:]
    
    readme = NEW_LINES.sub("\n", "\n".join(readme))
    
    with open(f"{ROOT_FOLDER}{sep}README.md", "w") as readmeFile:
        readmeFile.write(readme)