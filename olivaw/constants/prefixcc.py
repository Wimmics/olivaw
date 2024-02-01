from requests import get

# Checking most common prefixes
response = get("https://prefix.cc/context")
common_prefixes = response.json()["@context"]

uris = list(common_prefixes.items())
uris.sort(key=lambda x: x[1])
last_uri = ""
namespaces = []

# removing homonymous prefixes
for match in uris:
    if match[1] == last_uri:
        continue
    last_uri = match[1]
    namespaces.append(match)

namespaces.sort()

def iterate_node(node):
    candidates = [uri for uri in node["uris"] if len(uri[1]) > node["rank"] + 1]
    children = set([candidate[1][node["rank"] + 1] for candidate in candidates])
  
    for child in children:
        subnode_uris = [uri for uri in candidates if uri[1][node["rank"] + 1] == child]
        subnode = {
            "rank": node["rank"] + 1,
            "char": child,
            "children": [],
            "uris": subnode_uris
        }
        node["children"].append(subnode)
        
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

COMMON_URIS = {"rank": 0, "char": "h", "children": [], "uris": namespaces}

make_prefix_tree(COMMON_URIS)

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

def similar_prefix_search(subject, node, threshold):
    return [
        item
        for item in list(set(recurse_search(subject, node, "", 0, threshold)))
        if not item[1] == subject and
        not (
            item[1].startswith("http:") and
            item[1][len("http:"):] == subject[len("https:"):] and
            subject.startswith("https:")
        ) and
        not (
            item[1].startswith("https:") and
            item[1][len("https:"):] == subject[len("http:"):] and
            subject.startswith("http:")
        )
    ]