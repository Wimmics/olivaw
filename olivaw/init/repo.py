"""Module managing the "olivaw init repo" command"""

import requests
from json import dumps, loads
from dotenv import load_dotenv, set_key

from os import getenv
from os.path import sep, exists

from .readme import update_readme

from olivaw.constants import (
    REPO_URI,
    REF,
    PWD_TO_OVILAW,
    PWD_TO_ROOT_FOLDER,
    REPO_NAME,
    GITHUB_API,
    BADGE_LIST
)

ref = "_".join(REF.split("/")[1:])

def init_gist(key: str) -> str:
    """Initialize the gist that will store the badges data
    
    :param key: GitHub secret with the `gist` scope authorized
    :type key: `string`

    :return: Gist ID that stores the badges data
    :rtype: `str`
    """

    #form a request URL
    url=GITHUB_API+"/gists"
    
    #print headers,parameters,payload
    headers={'Authorization':'token %s' % key}
    params={'scope':'gist'}
    payload={
        "description": f"Badges for {REPO_NAME}",
        "public": False,
        "files": {
            f"{ref}_{badge}.json":{
                "content": dumps({
                    key: BADGE_LIST[badge][key]
                    for key in BADGE_LIST[badge]
                })
            }
            for badge in BADGE_LIST.keys()
        }
    }

    #make a requests
    res=requests.post(
        url,
        headers=headers,
        params=params,
        data=dumps(payload)
    )

    if not res.status_code == 201:
        print(f"Status code: {res.status_code}")
        print(res.text)

    return loads(res.text)['id']

def init_repo() -> None:
    """Executes the `olivaw init repo` command"""

    print("Let's initialize the repository")

    gist_secret = None
    gist_id = None
    if exists(f"{PWD_TO_OVILAW}{sep}.env"):
        load_dotenv(f"{PWD_TO_OVILAW}{sep}.env")
        gist_secret = getenv("GIST_SECRET")
        try:
            print("Creating gist...")
            gist_id = init_gist(gist_secret)
            update_readme(gist_id)
            print("Gists initialized")
        except:
            pass

    while gist_id is None:
        try:
            print("Please create a key on https://github.com/settings/tokens and create a key (only gist scope is required)")
            print("Key for gist access:")
            gist_secret = input()
            print("Creating gist...")
            gist_id = init_gist(gist_secret)
            update_readme(gist_id=gist_id)
            set_key(f"{PWD_TO_OVILAW}{sep}.env", "GIST_SECRET", gist_secret)
        except Exception as e:
            print(f"Provided key seems to be invalid: {str(e)}")

    print("First input the preferred prefix of the ontology:")
    prefix = input()
    print("First input the ontology namespace:")
    deploy_url = input()
    print("Then input the minimum Levenshtein threshold allowed between each of the future ontology terms:")
    print("Press enter for default value (3)")
    levenshtein_threshold = None
    while levenshtein_threshold is None:
        try:
            levenshtein_input = input()
            if levenshtein_input == '':
                levenshtein_input = "3"
            levenshtein_threshold = int(levenshtein_input)
        except Exception as e:
            print(e)
            return
    
    with open(f"{PWD_TO_ROOT_FOLDER}.acimov{sep}parameters.json", "w") as params:
        params.write(dumps({
            "ontology_prefix": prefix,
            "ontology_namespace": deploy_url,
            "term_distance_threshold": levenshtein_threshold,
            "project_prefixes": {},
            "blocking_errors": [
                "syntax-error",
                "owl-rl-constraint-violation"
            ],
            "gist_index": gist_id,
            "skipped_errors": [],
            "skipped_tests": [],
            "skipped_subjects": [],
            "skip_for_test": {},
            "skip_for_subject": {}
        }, indent=4))

    print("The repository is initialized!")
    print("The Gist access token is still required to Github so that the future Github Actions can be able to update the badges")
    print(f"Just go to {REPO_URI}/settings/secrets/actions and set a secret named 'GIST_SECRET' to the value of the access token")