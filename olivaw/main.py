"""Module providing the entry point of the program and the call of the proper functions in the olivaw package"""

from os import listdir, remove
from os.path import sep
from olivaw.constants import COMMAND, ROOT_FOLDER

def run() -> None:
    """Parse an olivaw command and execute it"""

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
    else:
        print(f"Unknown command: {command}")

def test(line: list[str]) -> None:
    """Parse an olivaw command starting with `olivaw test` and execute it

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
    else:
        print(f"Unknown target: {target}")

def flush():
    """Execute the `olivaw flush` command"""

    for filename in listdir(f"{ROOT_FOLDER}{sep}.acimov{sep}output"):
        if filename.split("-")[-1].split(".")[0] == "actions":
            continue
        remove(f"{ROOT_FOLDER}/.acimov/output/{filename}")

def init(line: list[str]):
    """Parse an olivaw command starting with `olivaw init` and execute it

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
    else:
        print(f"Unknown target: {target}")

def show(line: list[str]):
    """Parse an olivaw command starting with `olivaw show` and execute it

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
    else:
        print(f"Unknown target: {target}")