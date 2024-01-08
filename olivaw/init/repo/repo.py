import requests
import json
from os import getenv
from os.path import sep, exists
from dotenv import load_dotenv, set_key

from olivaw.constants import (
    ROOT_FOLDER,
    DEV_USERNAME,
    REPO_URI,
    REF,
    PWD_TO_OVILAW,
    PWD_TO_ROOT_FOLDER
)

GITHUB_API="https://api.github.com"
API_TOKEN='TOKEN_HERE'

gist_list = {
    "PASS": {
        "label": "Pass",
        "message": "0",
        "color": "green"
    },
    "NOTTESTED": {
        "label": "NotTested",
        "message": "0",
        "color": "white"
    },
    "CANNOTTELL": {
        "label": "CannotTell",
        "message": "0",
        "color": "yellow"
    },
    "MINORFAIL": {
        "label" : "MinorFail",
        "message": "0",
        "color": "orange"
    },
    "MAJORFAIL": {
        "label": "MajorFail",
        "message": "0",
        "color": "red"
    },
    "OWL EL": {
        "label": "OWL EL",
        "message": "compatible",
        "color": "green"
    },
    "OWL QL": {
        "label": "OWL QL",
        "message": "compatible",
        "color": "green"
    },
    "OWL RL": {
        "label": "OWL RL",
        "message": "compatible",
        "color": "green"
    }
}

for key in gist_list.keys():
    gist_list[key]["schemaversion"] = "1"

def create_gist(key, name, content='', public=False):
    #form a request URL
    url=GITHUB_API+"/gists"
    print("Request URL: %s" % url)
    
    #print headers,parameters,payload
    headers={'Authorization':'token %s' % key}
    params={'scope':'gist'}
    payload={
        "description": name,
        "public": public,
        "files": {
            name:{"content": content}
        }
    }

    #make a requests
    res=requests.post(url,headers=headers,params=params,data=json.dumps(payload))

    return json.loads(res.text)['id']

def init_gists(key):
    index = {}

    for gist in gist_list.keys():
        index[gist] = create_gist(key, gist, content=json.dumps(gist_list[gist]))

    index_id = create_gist(key, "index", content=index)

    return index, index_id

def badge_uri(gist_id):
    suffix = "__".join(REF.split("/")[1:])
    return f"https://img.shields.io/endpoint?url=https://gist.githubusercontent.com/{DEV_USERNAME}/{gist_id}/raw/{REPO_URI.split('/')[-1]}__{suffix}.json"

def init_badges():
    index, index_id = init_gists()

    updated = None
    with open(f"{ROOT_FOLDER}{sep}README.md", "r") as readme:
        updated = readme.readlines()

        updated = [
            f"![{gist_list[key]['label']} Badge]({badge_uri(index[key])})"
            for key in list(gist_list.keys())[:5]
        ] + [" "] + [
            f"![{gist_list[key]['label']} Badge]({badge_uri(index[key])})"
            for key in list(gist_list.keys())[5:]
        ] + [" "] + updated

        updated = "\n".join(updated)
    
    with open(f"{ROOT_FOLDER}{sep}README.md", "r") as readme:
        readme.write(updated)

    return index_id

def init_repo():
    print("Let's initialize your repository")

    gist_secret = None
    gist_index = None
    if exists(f"{PWD_TO_OVILAW}{sep}.env"):
        load_dotenv(f"{PWD_TO_OVILAW}{sep}.env")
        gist_secret = getenv("GIST_SECRET")
        try:
            gist_index = init_gists(gist_secret)
            print("Gists initialized")
        except:
            pass

    while gist_index is None:
        try:
            print("Please create a key on https://github.com/settings/tokens and create a key (only gist scope is required)")
            print("Key for gist access:")
            gist_secret = input()
            gist_index = init_gists(gist_secret)
            set_key(f"{PWD_TO_OVILAW}{sep}.env", "GIST_SECRET", gist_secret)
        except:
            print("Provided key seems to be invalid")

    print("First input the URL where your ontology should be deployed:")
    deploy_url = input()
    print("Then input the minimum Levenshtein threshold you expect between each of the future ontology terms")
    print("Press enter for default value (3)")
    levenshtein_threshold = None
    while levenshtein_threshold is None:
        try:
            levenshtein_input = input()
            if levenshtein_input == '':
                levenshtein_input = "3"
            levenshtein_threshold = int(levenshtein_input)
        except:
            pass
    
    with open(f"{PWD_TO_ROOT_FOLDER}.acimov{sep}parameters.json", "w") as params:
        params.write(json.dumps({
            "ontology_url": deploy_url,
            "term_distance_threshold": 3,
            "blocking_errors": [
                "syntax-error",
                "owl-rl-constraint-violation"
            ]
        }))