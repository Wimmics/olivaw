"""Module providing constants related to rdflib"""

from rdflib import Namespace

from .git_info import (
    SRC_URL,
    PLATFORM_URL,
    DEV_USERNAME,
    OLIVAW_ONTOLOGY
)

from .uris import EARL_PREFIX

DEV_PROFILE: str = f"{PLATFORM_URL}/{DEV_USERNAME}"
"""Link to the developper GitHub profile"""

PLATFORM_NAMESPACE: Namespace = Namespace(PLATFORM_URL)
"""Rdflib object representing the git platform namespace"""

EARL_NAMESPACE: Namespace = Namespace(EARL_PREFIX)
"""Rdflib object representing EARL namespace"""

SRC_NAMESPACE: Namespace = Namespace(SRC_URL)
"""Rdflib object representing repository src folder namespace"""

OLIVAW_NAMESPACE: Namespace = Namespace(OLIVAW_ONTOLOGY)
"""Rdflib object representing the olivaw namespace"""