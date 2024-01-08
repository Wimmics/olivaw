from rdflib import Namespace
from regex import compile as regex_compile

from .git_info import (
    SRC_URL,
    PLATFORM_URL,
    DEV_USERNAME,
    PROFILE_CHECK_URI,
    ACIMOV_MODEL_TEST_URI
)

DEV_PROFILE = f"{PLATFORM_URL}/{DEV_USERNAME}"

EARL_URL = "https://www.w3.org/ns/earl#"

EARL_NAMESPACE = Namespace(EARL_URL)
SRC_NAMESPACE = Namespace(SRC_URL)
TEST_NAMESPACE = Namespace(PROFILE_CHECK_URI)
ACIMOV_MODEL_NAMESPACE = Namespace(f"{ACIMOV_MODEL_TEST_URI}#")

PREFIX_ERROR = regex_compile('Prefix "[^"]+:" not bound')