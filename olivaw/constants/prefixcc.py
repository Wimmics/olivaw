from os.path import sep
from requests import get
from json import dumps, loads

PREFIX_CC_PREFIXES = "https://prefix.cc/context"
PREFIX_SIMILARITY_THRESHOLD = 2

def iterate_node(node):
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

def iterate(root):
    if len(root["children"]) > 0:
        for child in root["children"]:
            iterate(child)
        return
    iterate_node(root)
    
def make_prefix_tree(node):
    nb_iteration = max([len(uri[1]) for uri in node["uris"]])
    for _ in range(nb_iteration):
        iterate(node)

def make_index(prefix_base):
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
        make_prefix_tree(node)
    return tree

def parse_tree_to_tuple_leaves(tree):
    for node in tree.values():
        parse_node_to_tupe_leaves(node)

def parse_node_to_tupe_leaves(node):
    node["uris"] = [tuple(item) for item in node["uris"]]

    for child_node in node["children"]:
        parse_node_to_tupe_leaves(child_node)

try:
    response = get(PREFIX_CC_PREFIXES)
    common_prefixes = response.json()["@context"]
    uris = list(common_prefixes.items())

    COMMON_URIS_TREE = make_index(uris)
    with open(f"{sep.join(__file__.split(sep)[:-1])}{sep}uri_index.json", "w") as f:
        f.write(dumps(COMMON_URIS_TREE))
except:
    with open(f"{sep.join(__file__.split(sep)[:-1])}{sep}uri_index.json", "r") as f:
        COMMON_URIS_TREE = loads(f.read())
        parse_tree_to_tuple_leaves(COMMON_URIS_TREE)

def fetch_prefixes(node, nb_generations):
    if nb_generations < 0:
        return []
    
    result = []
    
    for child in node["children"]:
        result += fetch_prefixes(child, nb_generations - 1)
    
    return node["uris"] + result

def recurse_search(subject, node, branch, score, threshold):
    if len(subject) == 0:
        nb_generations = threshold - score
        
        return fetch_prefixes(node, nb_generations)
    
    if subject[0] == node["char"]:        
        if len(subject) == 1:
            nb_generations = threshold - score
            return fetch_prefixes(node, nb_generations)
                
        if len(node["children"]) == 0:
            return list(set(recurse_search(subject[2:], node, branch, score + 1, threshold)))
        
        result = []
        for child in node["children"]:
            result += recurse_search(subject[1:], child, branch + node["char"], score, threshold)
        return list(set(result))
    
    if score + 1 > threshold:
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

def similar_prefix_search(subject, index, threshold):
    value =  [
        item
        for node in index.values()
        for item in list(set(recurse_search(subject, node, "", 0, threshold)))
        if not item[1] == subject
    ]
    return value