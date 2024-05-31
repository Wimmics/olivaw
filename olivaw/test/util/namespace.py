"""Module providing functions for indexing namespace and exploring similar namespaces through these indexes"""

from json import dumps, loads
from os import sep
from ssl import CERT_NONE, create_default_context
from urllib.request import urlopen

from olivaw.constants.paths import PWD_TO_CONSTANTS
from olivaw.constants.prefixcc import PREFIX_CC_PREFIXES
from olivaw.test.util.print import smart_print

def iterate_node(node: dict) -> None:
    """Makes the children nodes of an index tree node passed in parameters
    
    :param node: The node to build the children from
    :type node: `dict`
    """
    candidates = [uri for uri in node["uris"] if len(uri[1]) > node["rank"] + 1]
    children = set([candidate[1][node["rank"] + 1] for candidate in candidates])

    node["children"] = [
        {
            "rank": node["rank"] + 1,
            "char": child,
            "children": [],
            "uris": [
                uri
                for uri in candidates
                if uri[1][node["rank"] + 1] == child
            ]
        }
        for child in children
    ]

    node["uris"] = [uri for uri in node["uris"] if len(uri[1]) == node["rank"] + 1]


def iterate(root: dict) -> None:
    """Build the recursive structure of the tree index starting from a nde
    
    :param root: The root node to start the building from
    :type root: `dict`
    """
    if len(root["children"]) > 0:
        for child in root["children"]:
            iterate(child)
        return
    iterate_node(root)


def make_namespace_tree(node: dict) -> None:
    """Launch the recursive building of the tree index starting from a node

    :param node: The node to recurse
    :type: `dict`
    """
    nb_iteration = max([len(uri[1]) for uri in node["uris"]])
    for _ in range(nb_iteration):
        iterate(node)


def fetch_namespaces(node: dict, nb_generations: int) -> list[tuple[str, str]]:
    """Returns the proper URIs that could satisfy the search requirements on the current branch

    :param node: The current index node
    :type node: `dict`

    :param nb_generations: How many generations is going to be fetched on the current branch
    :type nb_generation: `int`

    :returns: List of prefix and namespace couples that statisfy the requirements
    :rtype: `list[tuple[str, str]]`
    """
    if nb_generations < 0:
        return []

    result = []

    for child in node["children"]:
        result += fetch_namespaces(child, nb_generations - 1)

    return node["uris"] + result


def recurse_search(
        subject: str,
        node: dict,
        branch: str,
        score: int,
        threshold: int
    ) -> list[tuple[str, str]]:
    """Returns the most similar prefixes to the one passed as argument, on the node passed as parameter, only those under a given Levenshtein distance

    :param subject: Namespace to search into the node
    :type subject: `str`

    :param node: Node that is searched
    :type node: `int`

    :param branch: Current string made by the exploration of the index up to the current node
    :type branch: `str`

    :param score: Current Levenshtein distance computed so far
    :type score: `int`

    :param threshold: Maximum Levenshtein distance tolerated for the found namespaces
    :type threshold: `int`

    :returns: List of prefix and namespace couples that statisfy the requirements
    :rtype: `list[tuple[str, str]]`
    """
    if len(subject) == 0:
        nb_generations = threshold - score
        return fetch_namespaces(node, nb_generations)

    if subject[0] == node["char"]:
        if len(subject) == 1:
            nb_generations = threshold - score
            return fetch_namespaces(node, nb_generations)

        if len(node["children"]) == 0:
            return list(set(recurse_search(subject[2:], node, branch, score + 1, threshold)))

        result = []
        for child in node["children"]:
            result += recurse_search(subject[1:], child, branch + node["char"], score, threshold)
        return list(set(result))

    if score + int(threshold > 0) > threshold:
        return []

    result = []

    # if error was by adding a character
    # then remove the subject first character and proceed on same node with incremented score
    result += recurse_search(subject[1:], node, branch, score + 1, threshold)

    # if error was by removing a character
    for child in node["children"]:
        # then keep the subject and proceed on each children node with incremented score
        result += recurse_search(subject, child, branch + node["char"], score + 1, threshold)

    # if error was by updating a character
    # continue on children score with incremented score
    for child in node["children"]:
        result += recurse_search(subject[1:], child, branch + node["char"], score + 1, threshold)

    return list(set(result))


def similar_namespace_search(subject: str, index: dict, threshold: int) -> list[tuple[str, str]]:
   """Returns the most similar prefixes to the one passed as argument, with the index passed as argument, only those under a given Levenshtein distance

    :param subject: Namespace to search into the index
    :type subject: `str`

    :param index: The index to search into
    :type index: `dict`

    :param threshold: Maximum Levenshtein distance tolerated for the found namespaces
    :type threshold: `int`

    :returns: List of prefix and namespace couples that statisfy the requirements
    :rtype: `list[tuple[str, str]]`
    """
   return  [
        item
        for node in index.values()
        for item in list(set(recurse_search(subject, node, "", 0, threshold)))
        if not (item[1] == subject and threshold > 0)
    ]

def common_namespace_search(subject: str, threshold: int) -> list[tuple[str, str]]:
    """Returns the most similar prefixes to the one passed as argument from `prefix.cc` dataset, only those under a given Levenshtein distance

    :param subject: Namespace to search into the index
    :type subject: `str`

    :param threshold: Maximum Levenshtein distance tolerated for the found namespaces
    :type threshold: `int`

    :returns: List of prefix and namespace couples that statisfy the requirements
    :rtype: `list[tuple[str, str]]`
    """
    return similar_namespace_search(subject, COMMON_URIS_TREE, threshold)

def parse_node_to_tuple_leaves(node: dict) -> None:
    """Parse the given index node to set the prefix/URIs stored as tuples
    
    :param node: URI index node
    :type node: `dict`
    """
    node["uris"] = [tuple(item) for item in node["uris"]]

    for child_node in node["children"]:
        parse_node_to_tuple_leaves(child_node)


def parse_tree_to_tuple_leaves(tree: dict) -> None:
    """Parse the given index to set the prefix/URIs stored as tuples
    
    :param tree: URI index
    :type tree: `dict`
    """
    for node in tree.values():
        parse_node_to_tuple_leaves(node)

def make_index(prefix_base: list[tuple[str, str]]) -> dict:
    """Makes a URI index out of a prefix/namespace dataset

    :param prefix_base: Dataset of prefixes and their related namespaces
    :type prefix_base: `list[tuple[str, str]]`

    :returns: An index that stores all of these URIs
    :rtype: `dict`
    """
    prefix_base.sort(key=lambda x: x[1])
    last_uri = ""
    namespaces = []

    # removing homonymous prefixes
    for match in prefix_base:
        if match[1] == last_uri:
            continue
        last_uri = match[1]
        namespaces.append(match)

    namespaces.sort()

    tree = {
        char: {
            "rank": 0,
            "char": char,
            "children": [],
            "uris": [
                namespace
                for namespace in namespaces
                if namespace[1][0] == char
            ]
        }
        for char in set([namespace[1][0] for namespace in namespaces])
    }
    for node in tree.values():
        make_namespace_tree(node)
    return tree

def get_dict_from_node(node: dict, result: dict[str, str]) -> dict[str, str]:
    """Makes a dictionary linking a namespace to a prefix given a URI index node passed in parameter

    :param node: The URI index node
    :type node: `dict`

    :returns: A dictionary linking a namespace to a prefix given a namespace index pass in parameter
    :rtype: `dict[str, str]`
    """
    for (prefix, namespace) in node["uris"]:
        result[namespace] = prefix
    for child in node["children"]:
        result = get_dict_from_node(child, result)
    return result

def get_dict(index: dict) -> dict[str, str]:
    """Makes a dictionary linking a namespace to a prefix given a namespace index pass in parameter

    :param index: The URI index
    :type index: `dict`

    :returns: A dictionary linking a namespace to a prefix given a namespace index pass in parameter
    :rtype: `dict[str, str]`
    """
    result = {}
    for start in index.keys():
        result = get_dict_from_node(index[start], result)
    return result


uris = []
COMMON_URI_DICT: dict[str, str] = {}
"""Dict linking a common namespace to its preferred prefix (from `prefix.cc`)"""

COMMON_URIS_TREE: dict = None
"""Index storing the most common prefixes (from `prefix.cc`) and related namespaces for Levenshtein distance search"""

try:
    common_prefixes = None

    # This site uses self signed certificate
    myssl = create_default_context()
    myssl.check_hostname = False
    myssl.verify_mode = CERT_NONE
    
    with urlopen(PREFIX_CC_PREFIXES, context=myssl) as downloaded:
        common_prefixes = loads(downloaded.read().decode())

    common_prefixes = common_prefixes["@context"]
    uris = list(common_prefixes.items())

    for prefix, uri in uris:
        COMMON_URI_DICT[uri] = prefix

    COMMON_URIS_TREE = make_index(uris)
    with open(f"{PWD_TO_CONSTANTS}{sep}uri_index.json", "w") as f:
        f.write(dumps(COMMON_URIS_TREE))


    smart_print(" ")
    smart_print("New prefixcc index saved")
    smart_print(" ")
except:
    with open(f"{sep.join(__file__.split(sep)[:-3])}{sep}constants{sep}uri_index.json", "r") as f:
        COMMON_URIS_TREE = loads(f.read())
        parse_tree_to_tuple_leaves(COMMON_URIS_TREE)

    COMMON_URI_DICT = get_dict(COMMON_URIS_TREE)
    smart_print(" ")
    smart_print("prefixcc index loaded from disk")
    smart_print(" ")