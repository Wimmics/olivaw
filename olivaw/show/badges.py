from os.path import sep
from requests import get
from json import loads

from olivaw.constants import ROOT_FOLDER

def show_badges():
    readme = None
    with open(f"{ROOT_FOLDER}{sep}README.md", "r") as readmeFile:
        readme = readmeFile.readlines()

    badges_urls = [
        line.strip().split("?url=")[1][:-1]
        for line in readme[:10]
        if len(line.strip()) > 0
    ]

    badges_contents = [
        loads(get(url).text)
        for url in badges_urls
    ]

    badges_contents = [
        [
            f"LABEL\t=\t{badge['label']}",
            f"COLOR\t=\t{badge['color']}",
            f"MESSAGE\t=\t{badge['message']}"
        ]
        for badge in badges_contents
    ]

    badge_list = [
        "PASS",
        "NOTTESTED",
        "CANNOTTELL",
        "MINORFAIL",
        "MAJORFAIL",
        "EL",
        "QL",
        "RL"
    ]

    badges_contents = [
        [f"{name}_{item}" for item in badge]
        for badge, name in zip(badges_contents, badge_list)
    ]

    badges_contents = [
        item
        for badge in badges_contents
        for item in badge
    ]

    for item in range(0, len(badges_contents), 3):
        print(badges_contents[item+1])
        print(badges_contents[item+2])