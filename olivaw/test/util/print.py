"""Module providing a print function that will behave depending on the execution mode (manual/actions/precommit)"""

from tqdm import tqdm
from olivaw.constants import QUIET

def print_title(title: str) -> None:
    """Prints the title if olivaw execution mode allows it

    :param title: The title to print
    :type title: `str`
    """
    if QUIET:
        return
    title = "== " + title + " =="
    border = "=" * len(title)
    print("\n" * 2)
    print(border)
    print(title)
    print(border)


def smart_print(message: str) -> None:
    """Prints the provided message if olivaw execution mode allows it
    
    :param message: The message to print
    :type message: `str`
    """
    if QUIET:
        return
    print(message)

def progress_bar(array: list) -> tqdm:
    """Provides a visible progress bar for a list if olivaw execution mode allows it

    :param array: The list
    :type array: `list`
    
    :returns: A progress bar
    :rtype: `tqdm.tqdm`
    """
    return tqdm(array, disable=QUIET)