"""Module providing constants related to rdflib"""

from rdflib import Namespace
from regex import compile as regex_compile, Pattern

from .git_info import (
    SRC_URL,
    PLATFORM_URL,
    DEV_USERNAME,
    OLIVAW_EARL_DATASET
)

from .uris import EARL_PREFIX

DEV_PROFILE: str = f"{PLATFORM_URL}/{DEV_USERNAME}"
"""Link to the developper GitHub profile"""

EARL_NAMESPACE: Namespace = Namespace(EARL_PREFIX)
"""Rdflib object representing EARL namespace"""

SRC_NAMESPACE: Namespace = Namespace(SRC_URL)
"""Rdflib object representing repository src folder namespace"""

OLIVAW_EARL_NAMESPACE: Namespace = Namespace(OLIVAW_EARL_DATASET)
"""Rdflib object representing the olivaw-earl namespace"""

PREFIX_ERROR: Pattern = regex_compile('Prefix "[^"]+:" not bound')
"""Regex detecting the rdflib prefix error"""

URI_PATTERN: Pattern = regex_compile("<[^>]*>")
"""Regex detecting a URI node in some RDF data"""