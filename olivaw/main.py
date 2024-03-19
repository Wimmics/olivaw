from sys import argv
from os.path import sep

def run():
    olivaw_index = [
        i for i in range(len(argv))
        if argv[i].split(sep)[-1].split(".")[0] == "olivaw"
    ]
    command, *args = argv[olivaw_index[0] + 1:]
    
    if command == "test":
        test(args)
    elif command == "init":
        init(args)
    elif command == "flush":
        from olivaw.constants import ROOT_FOLDER
        from os import listdir, remove
        for filename in listdir(f"{ROOT_FOLDER}{sep}.acimov{sep}output"):
            if filename.split("-")[-1].split(".")[0] == "actions":
                continue
            remove(f"{ROOT_FOLDER}/.acimov/output/{filename}")
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