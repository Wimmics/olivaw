"""Module responsible for the "olivaw show badges" command"""

from os.path import sep
from requests import get
from json import loads

from olivaw.constants import ROOT_FOLDER
from olivaw.constants.git_info import REF

def show_badges() -> None:
    """Executes the `olivaw show badges` command"""

    readme = None
    with open(f"{ROOT_FOLDER}{sep}README.md", "r") as readmeFile:
        readme = readmeFile.readlines()

    first_title = [
        i for i in range(len(readme))
        if readme[i].startswith("# ")
    ][0]

    badges_base_url = [
        line.strip().split("?url=")[1][:-1]
        for line in readme[:first_title]
        if len(line.strip()) > 0 and
        "?url=" in line
    ][0]

    old_ref = "_".join(badges_base_url.split("/")[-1].split(".")[0].split("_")[:-1])

    if old_ref.endswith("MODEL") or old_ref.endswith("DATA") or old_ref.endswith("QUERY"):
        old_ref = "_".join(old_ref.split("_")[:-1])

    badges_base_url = "/".join(badges_base_url.split("/")[:-1])

    badge_names = [
        f"{test_type}_{severity}"
        for test_type in ["MODEL", "DATA", "QUERY"]
        for severity in ["PASS", "NOTTESTED", "CANNOTTELL", "MINORFAIL", "MAJORFAIL"]
    ] + ["EL", "QL", "RL"]

    badges_data = [
        loads(get(f"{badges_base_url}/{old_ref}_{badge}.json").text)
        for badge in badge_names
    ]

    for name, data in zip(badge_names, badges_data):
        print(f"{name}_COLOR\t=\t{data['color']}")
        print(f"{name}_LABEL\t=\t{data['message']}")