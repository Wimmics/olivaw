from os.path import exists
from json import loads

from olivaw.constants import ROOT_FOLDER

def show_gist():
    parameters_path = f"{ROOT_FOLDER}/.acimov/parameters.json"

    if not exists(parameters_path):
        print("fatal: No parameters.json file")
        exit(1)

    parameters = None
    try:
        with open(parameters_path, "r") as parameters_file:
            parameters = loads(parameters_file.read())
    except:
        print("fatal: file parameters.json is not a well formed json file")
        exit(1)
        
    if not "gist_index" in parameters:
        print('fatal: no parameter named "gist_index" in file parameters.json')
        exit(1)

    index = parameters["gist_index"]
    print(index)