"""Module managing the "olivaw init branch" command"""

from .readme import update_readme

def init_branch():
    # In case more behavior needs to be implemented in the future
    update_readme()