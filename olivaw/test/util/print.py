from tqdm import tqdm
from olivaw.constants import QUIET

def print_title(title):
    if QUIET:
        return
    title = "== " + title + " =="
    border = "=" * len(title)
    print("\n" * 2)
    print(border)
    print(title)
    print(border)


def smart_print(message):
    if QUIET:
        return
    print(message)

def progress_bar(array):
    return tqdm(array, disable=QUIET)