from .git_info import (
    SRC_URL,
    PLATFORM_URL,
    DEV_USERNAME,
    PROFILE_CHECK_URI,
    ACIMOV_MODEL_TEST_URI
)

from .uris import EARL_PREFIX

DEV_PROFILE = f"{PLATFORM_URL}/{DEV_USERNAME}"

EARL_NAMESPACE = None
SRC_NAMESPACE = None
TEST_NAMESPACE = None
ACIMOV_MODEL_NAMESPACE = None
PREFIX_ERROR = None

try:
    from rdflib import Namespace
    from regex import compile as regex_compile

    EARL_NAMESPACE = Namespace(EARL_PREFIX)
    SRC_NAMESPACE = Namespace(SRC_URL)
    TEST_NAMESPACE = Namespace(PROFILE_CHECK_URI)
    ACIMOV_MODEL_NAMESPACE = Namespace(f"{ACIMOV_MODEL_TEST_URI}#")

    PREFIX_ERROR = regex_compile('Prefix "[^"]+:" not bound')
except:
    pass