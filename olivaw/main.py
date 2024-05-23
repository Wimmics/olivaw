"""Module providing the entry point of the program and the call of the proper functions in the olivaw package"""

from os import listdir, remove
from os.path import sep
from olivaw.constants import COMMAND, ROOT_FOLDER

def run():
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

def test(line):
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
        # Best way to deal with invalid command...?
        print(f"Unknown target: {target}")

def flush():
    for filename in listdir(f"{ROOT_FOLDER}{sep}.acimov{sep}output"):
        if filename.split("-")[-1].split(".")[0] == "actions":
            continue
        remove(f"{ROOT_FOLDER}/.acimov/output/{filename}")

def init(line):
    target = line[0]

    if target == "repo":
        from olivaw.init.repo import init_repo
        init_repo()
    elif target == "branch":
        from olivaw.init.branch import init_branch
        init_branch()
        return
    else:
        # Best way to deal with invalid command...?
        print(f"Unknown target: {target}")

def show(line):
    target = line[0]

    if target == "gist":
        from olivaw.show.gist import show_gist
        show_gist()
    elif target == "badges":
        from olivaw.show.badges import show_badges
        show_badges()
    else:
        print(f"Unknown target: {target}")