from os.path import sep
from json import loads
from requests import get

from olivaw.constants import (
    ROOT_FOLDER,
    DEV_USERNAME,
    REPO_URI,
    REF,
    NEW_LINES,
    BADGE_LIST,
    badge_url
)

from .readme import update_readme

def init_branch():
    # In case more behavior needs to be implemented in the future
    update_readme()