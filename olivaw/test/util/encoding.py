from codecs import open as copen
from datetime import datetime

from olivaw.constants import MODE,  DEV_USERNAME, PWD_TO_OUTPUT_FOLDER
from olivaw.test.markdown import markdown_export

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
    path = f"{PWD_TO_OUTPUT_FOLDER}{name}"

    return name, path

def save(path, content):
    with copen(f"{path}", "w", "utf-8") as f:
        f.write(content)

def save_reports(test_type, report):
    name, path = file_name(test_type)
    save(f"{path}.ttl", report.serialize(format="ttl"))
    save(f"{path}.md", markdown_export(report, name))