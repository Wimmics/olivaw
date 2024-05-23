from .git_info import (
    SRC_URL,
    PLATFORM_URL,
    DEV_USERNAME,
    OLIVAW_EARL_DATASET
)

from .uris import EARL_PREFIX

DEV_PROFILE: str = f"{PLATFORM_URL}/{DEV_USERNAME}"
"""Link to the developper GitHub profile"""

EARL_NAMESPACE = None
"""Rdflib object representing EARL namespace"""

SRC_NAMESPACE = None
"""Rdflib object representing repository src folder namespace"""

OLIVAW_EARL_NAMESPACE = None
"""Rdflib object representing the olivaw-earl namespace"""

PREFIX_ERROR = None
"""Regex detecting the rdflib prefix error"""

try:
    from rdflib import Namespace
    from regex import compile as regex_compile, Pattern

    EARL_NAMESPACE: Namespace = Namespace(EARL_PREFIX)
    SRC_NAMESPACE: Namespace = Namespace(SRC_URL)
    OLIVAW_EARL_NAMESPACE: Namespace = Namespace(OLIVAW_EARL_DATASET)

    PREFIX_ERROR: Pattern = regex_compile('Prefix "[^"]+:" not bound')
    BACKSLASH_IN_URI: Pattern = regex_compile("<[^>]*>")
except:
    pass