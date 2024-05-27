"""Module providing functions for updating the main README.md project file using badges URIs"""

from os import sep

from olivaw.constants import (
    ROOT_FOLDER,
    BADGE_LIST,
    DEV_USERNAME,
    NEW_LINES,
    GIST_INDEX
)
from olivaw.init.util import badge_url

def update_readme(gist_id: str=None) -> None:
    """Updates the main README.md file with the proper badges URIs

    :param gist_id: ID of the gist storing the project badges data, defaults to `None`
    :type gist_id: `str`, optional
    """

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
        for badge in list(BADGE_LIST.keys())[8:13]
    ] + [" "] + ["Query tests:\t"] + [
        f"![{BADGE_LIST[badge]['label']} Badge]({badge_url(DEV_USERNAME, gist_id, badge)})"
        for badge in list(BADGE_LIST.keys())[13:]
    ] + [" "] + readme[first_title_line:]
    
    readme = NEW_LINES.sub("\n", "\n".join(readme))
    
    with open(f"{ROOT_FOLDER}{sep}README.md", "w") as readmeFile:
        readmeFile.write(readme)