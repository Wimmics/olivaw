from .git_info import (
    SRC_URL,
    PLATFORM_URL,
    DEV_USERNAME,
    PROFILE_CHECK_URI,
    OLIVAW_EARL_DATASET
)

from .uris import EARL_PREFIX

DEV_PROFILE = f"{PLATFORM_URL}/{DEV_USERNAME}"

EARL_NAMESPACE = None
SRC_NAMESPACE = None
TEST_NAMESPACE = None
OLIVAW_EARL_NAMESPACE = None
PREFIX_ERROR = None

try:
    from rdflib import Namespace
    from regex import compile as regex_compile

    EARL_NAMESPACE = Namespace(EARL_PREFIX)
    SRC_NAMESPACE = Namespace(SRC_URL)
    TEST_NAMESPACE = Namespace(PROFILE_CHECK_URI)
    OLIVAW_EARL_NAMESPACE = Namespace(OLIVAW_EARL_DATASET)

    PREFIX_ERROR = regex_compile('Prefix "[^"]+:" not bound')
except:
    pass