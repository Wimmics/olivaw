import requests
import json
from os.path import sep

from olivaw.constants import (
    ROOT_FOLDER,
    DEV_USERNAME,
    REPO_URI,
    REF
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

def create_gist(name, content='', public=False):
    #form a request URL
    url=GITHUB_API+"/gists"
    print("Request URL: %s" % url)
    
    #print headers,parameters,payload
    headers={'Authorization':'token %s'%API_TOKEN}
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

def init_gists():
    index = {}

    for gist in gist_list.keys():
        index[gist] = create_gist(gist, content=json.dumps(gist_list[gist]))

    index_id = create_gist("index", content=index)

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
    print("First input the URL where your ontology should be deployed:")
    deploy_url = input()
    print("Then input the minimum Levenshtein threshold you expect between each of the future ontology terms")
    print("Press enter for default value (3)")
    levenshtein_threshold = None
    while levenshtein_threshold is None:
        try:
            levenshtein_threshold = int(input())
        except:
            pass
    
    # Pour l'instant
    gist_index = init_gists()