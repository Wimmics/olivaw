from codecs import open as copen
from datetime import datetime

from olivaw.constants import MODE,  DEV_USERNAME, PWD_TO_OUTPUT_FOLDER

def datetime_id():
    return ".".join(
            datetime\
            .now()\
            .isoformat()\
            .split(".")[:-1]
        ).replace(":", "-")


def file_name(test_type):
    suffix = MODE if not MODE == "manual" else f"{MODE}-{DEV_USERNAME}-{datetime_id()}"
    name = f"{test_type}-test-{suffix}"
    return name

def save(path, content):
    with copen(f"{path}", "w", "utf-8") as f:
        f.write(content)

def save_reports(name, turtle, markdown):
    path = f"{PWD_TO_OUTPUT_FOLDER}{name}"
    save(f"{path}.ttl", turtle)
    save(f"{path}.md", markdown)