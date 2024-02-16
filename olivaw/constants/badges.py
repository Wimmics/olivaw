from .git_info import REF

GITHUB_API="https://api.github.com"

BADGE_LIST = {
    "MODEL_PASS": {
        "label": "Pass",
        "message": "0",
        "color": "green"
    },
    "MODEL_NOTTESTED": {
        "label": "NotTested",
        "message": "0",
        "color": "white"
    },
    "MODEL_CANNOTTELL": {
        "label": "CannotTell",
        "message": "0",
        "color": "yellow"
    },
    "MODEL_MINORFAIL": {
        "label" : "MinorFail",
        "message": "0",
        "color": "orange"
    },
    "MODEL_MAJORFAIL": {
        "label": "MajorFail",
        "message": "0",
        "color": "red"
    },
    "EL": {
        "label": "OWL EL",
        "message": "compatible",
        "color": "green"
    },
    "QL": {
        "label": "OWL QL",
        "message": "compatible",
        "color": "green"
    },
    "RL": {
        "label": "OWL RL",
        "message": "compatible",
        "color": "green"
    },
    "DATA_PASS": {
        "label": "Pass",
        "message": "0",
        "color": "green"
    },
    "DATA_NOTTESTED": {
        "label": "NotTested",
        "message": "0",
        "color": "white"
    },
    "DATA_CANNOTTELL": {
        "label": "CannotTell",
        "message": "0",
        "color": "yellow"
    },
    "DATA_MINORFAIL": {
        "label" : "MinorFail",
        "message": "0",
        "color": "orange"
    },
    "DATA_MAJORFAIL": {
        "label": "MajorFail",
        "message": "0",
        "color": "red"
    }
}

def badge_url(dev, gist_id, badge):
    return f"https://img.shields.io/endpoint?url=https://gist.githubusercontent.com/{dev}/{gist_id}/raw/{'_'.join(REF.split('/')[1:])}_{badge}.json"