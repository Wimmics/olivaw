"""Module providing the entry point of the program and the call of the proper functions in the olivaw package"""

import sys
from os import listdir, remove
from os.path import sep, exists

from olivaw.constants import (
    COMMAND,
    ROOT_FOLDER,
    HELP_OPTION,
    INIT_HELP,
    SHOW_HELP,
    TEST_HELP
)

def run() -> None:
    """
OLIVAW: Ontology Long-lived Integration Via ACIMOV Workflow

    Available tools: `olivaw test`, `olivaw init`, `olivaw show`, `olivaw flush`

    Olivaw provides some tools to assist ontology development in ACIMOV methodology 


    See documentation about command lines: https://github.com/Wimmics/olivaw/blob/main/docs/commands.md

    """

    if len(COMMAND) == 0:
        print('fatal: olivaw without any argument is not a valid command, please read the documentation')
        exit(1)
        
    command, *args = COMMAND

    if command == "test":
        test(args)
    elif command == "init":
        init(args)
    elif command == "flush":
        flush()
    elif command == "show":
        show(args)
    elif command in HELP_OPTION:
        this = sys.modules[__name__]
        tools = [
            x for x in dir(this)
            if callable(getattr(this, x)) and
            getattr(this, x).__module__ == "olivaw.main"
        ]
        tools.sort(key="run".__eq__, reverse=True)
        docs = "\n".join([
            "\n".join([
                line for line in
                getattr(this, x).__doc__.split("\n")
                if not line.strip().startswith(":")
            ])
            for x in tools
        ])
        print(docs)
    else:
        print(f"Unknown command: {command}")
        print("Type `olivaw --help` or `olivaw -h` for some help")

def test(line: list[str]) -> None:
    """`olivaw test` commands

    Available commands: `olivaw test model`, `olivaw test data`, `olivaw test query`

    Olivaw command lines for testing the repository


    Run only in a git repository

    Type `olivaw test --help` or `olivaw test -h` for more information

    :param line: list of options following `olivaw test` in the command line typed in the terminal
    :type line: `list[str]`
    """
    target = line.pop(0)
    
    if target == "model":
        # Only instanciate Corese server if needed
        from olivaw.test.model.suite import test_model
        test_model()
    elif target == "data":
        # Only instanciate Corese server if needed
        from olivaw.test.data.suite import test_data
        test_data()
    elif target == "query":
        # Only instanciate Corese server if needed
        from olivaw.test.query.suite import test_query
        test_query()
    elif target == "precommit":
        from olivaw.hook.test import run
        run(line)
    elif target in HELP_OPTION:
        print(TEST_HELP)
    else:
        print(f"Unknown target: {target}")
        print("Type `olivaw test --help` or `olivaw test -h` for some help")


def flush() -> None:
    """`olivaw flush` command

    Available command: `olivaw flush`
    
    Delete files in `PATH/.acimov/output/` folder except GitHub Actions test reports 
    
    """
    if not exists(f"{ROOT_FOLDER}{sep}.acimov{sep}output"):
        return

    for filename in listdir(f"{ROOT_FOLDER}{sep}.acimov{sep}output"):
        if filename.split("-")[-1].split(".")[0] == "actions":
            continue
        remove(f"{ROOT_FOLDER}/.acimov/output/{filename}")

def init(line: list[str]):
    """`olivaw init` commands

    Available commands: `olivaw init repo`, `olivaw init branch`

    Olivaw commands to initialize a repository or a branch


    Run only in a git repository

    Type `olivaw init --help` or `olivaw test -h` for more information

    :param line: list of options following `olivaw init` in the command line typed in the terminal
    :type line: `list[str]`
    """
    target = line[0]

    if target == "repo":
        from olivaw.init.repo import init_repo
        init_repo()
    elif target == "branch":
        from olivaw.init.branch import init_branch
        init_branch()
        return
    elif target in HELP_OPTION:
        print(INIT_HELP)
    else:
        print(f"Unknown target: {target}")
        print("Type `olivaw init --help` or `olivaw init -h` for some help")

def show(line: list[str]):
    """`olivaw show` commands

    Available commands: `olivaw show gist`, `olivaw show badges`

    Olivaw tool to display some repository useful information


    Run only in a git repository

    Type `olivaw show --help` or `olivaw test -h` for more information

    :param line: list of options following `olivaw show` in the command line typed in the terminal
    :type line: `list[str]`
    """
    target = line[0]

    if target == "gist":
        from olivaw.show.gist import show_gist
        show_gist()
    elif target == "badges":
        from olivaw.show.badges import show_badges
        show_badges()
    elif target in HELP_OPTION:
        print(SHOW_HELP)
    else:
        print(f"Unknown target: {target}")
        print("Type `olivaw show --help` or `olivaw show -h` for some help")
