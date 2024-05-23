GITHUB_API: str="https://api.github.com"
"""Github API that allows to manage gissts"""

GIST_BADGE_PREFIX: str = "https://img.shields.io/endpoint?url=https://gist.githubusercontent.com"
"""Base URL for badges that read some gist content"""

BADGE_LIST: dict[str, dict[str, str]] = {
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
    },
    "QUERY_PASS": {
        "label": "Pass",
        "message": "0",
        "color": "green"
    },
    "QUERY_NOTTESTED": {
        "label": "NotTested",
        "message": "0",
        "color": "white"
    },
    "QUERY_CANNOTTELL": {
        "label": "CannotTell",
        "message": "0",
        "color": "yellow"
    },
    "QUERY_MINORFAIL": {
        "label" : "MinorFail",
        "message": "0",
        "color": "orange"
    },
    "QUERY_MAJORFAIL": {
        "label": "MajorFail",
        "message": "0",
        "color": "red"
    }
}
"""Set of default values for the different badges"""