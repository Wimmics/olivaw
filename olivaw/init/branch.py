"""Module managing the "olivaw init branch" command"""

from olivaw.constants import PWD_TO_ROOT_FOLDER, BADGE_URL_FORMAT, REF

def init_branch() -> None:
    """Function that will execute the "olivaw init branch" command"""

    readme_text=""

    with open(f"{PWD_TO_ROOT_FOLDER}README.md", "r") as f:
        readme_text = f.read()

    new_readme_text=readme_text

    for match in BADGE_URL_FORMAT.findall(readme_text):
        new_readme_text=new_readme_text.replace(
            match[0],
            match[0].replace(
                match[1],
                '_'.join(REF.split('/')[1:])
            )
        )

    with open(f"{PWD_TO_ROOT_FOLDER}README.md", "w") as f:
        f.write(new_readme_text)