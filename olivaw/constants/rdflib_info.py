from .git_info import (
    SRC_URL,
    PLATFORM_URL,
    DEV_USERNAME,
    PROFILE_CHECK_URI,
    OLIVAW_EARL_DATASET
)

from .uris import EARL_PREFIX

# Link to the developper GitHub profile
DEV_PROFILE = f"{PLATFORM_URL}/{DEV_USERNAME}"

# Rdflib object representing EARL namespace
EARL_NAMESPACE = None

# Rdflib object representing repository src folder namespace
SRC_NAMESPACE = None

# Rdflib object representing the olivaw-earl namespace
OLIVAW_EARL_NAMESPACE = None

# Regex detecting the rdflib prefix error
PREFIX_ERROR = None

try:
    from rdflib import Namespace
    from regex import compile as regex_compile

    EARL_NAMESPACE = Namespace(EARL_PREFIX)
    SRC_NAMESPACE = Namespace(SRC_URL)
    OLIVAW_EARL_NAMESPACE = Namespace(OLIVAW_EARL_DATASET)

    PREFIX_ERROR = regex_compile('Prefix "[^"]+:" not bound')
    BACKSLASH_IN_URI = regex_compile("<[^>]*>")
except:
    pass