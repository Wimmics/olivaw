"""Module providing useful functions for saving files with proper encodings"""

from codecs import open as copen
from datetime import datetime
from os import makedirs
from os.path import exists

from olivaw.constants import MODE,  DEV_USERNAME, PWD_TO_OUTPUT_FOLDER

def datetime_id() -> None:
    """Generate a datetime part for a file generation"""
    return ".".join(
            datetime\
            .now()\
            .isoformat()\
            .split(".")[:-1]
        ).replace(":", "-")


def file_name(test_type: str) -> str:
    """Returns the file name for a file generation

    :param test_type: The test type
    :type test_type: `str`, one of `"model"`, `"data"` or `"query"`

    :returns: A file name
    :rtype: `str`
    """
    suffix = MODE.lower() if not MODE == "manual" else f"{MODE}-{DEV_USERNAME}-{datetime_id()}"
    name = f"{test_type}-test-{suffix}"
    return name

def save(path: str, content: str) -> None:
    """Save the provided content with proper codec, in the provided path

    :param path: The file path
    :type path: `str`

    :param content: The file content
    :type content: `str`
    """
    if not exists(PWD_TO_OUTPUT_FOLDER):
        makedirs(PWD_TO_OUTPUT_FOLDER)
    with copen(f"{path}", "w", "utf-8") as f:
        f.write(content)

def save_reports(name: str, turtle: str, markdown: str) -> None:
    """Saves the provided turtle and markdown reports

    :param name: The desired report file path
    :type name: `str`

    :param turtle: The turtle report
    :type turtle: `str`

    :param markdown: The markdown report
    :type markdown: `str`
    """
    path = f"{PWD_TO_OUTPUT_FOLDER}{name}"
    save(f"{path}.ttl", turtle)
    save(f"{path}.md", markdown)