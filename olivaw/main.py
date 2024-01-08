from sys import argv
from os.path import sep

def run():
    olivaw_index = [
        i for i in range(len(argv))
        if argv[i].split(sep)[-1] == "olivaw"
    ]
    command, *args = argv[olivaw_index[0] + 1:]
    
    if command == "test":
        test(args)
    elif command == "init":
        init(args)
    else:
        print(f"Unknown command: {command}")

def test(line):
    target = line[0]
    
    if target == "model":
        # Only instanciate Corese server if needed
        from .test.model.suite import modelTest
        modelTest()
    elif target == "data":
        # Implement here
        return
    elif target == "query":
        # Implement here
        return
    else:
        # Best way to deal with invalid command...?
        print(f"Unknown target: {target}")

def init(line):
    target = line[0]

    if target == "repo":
        from .init.repo.repo import init_repo
        init_repo()
    elif target == "branch":
        # Implement here
        return
    else:
        # Best way to deal with invalid command...?
        print(f"Unknown target: {target}")