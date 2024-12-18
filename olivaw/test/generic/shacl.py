"""Module providing the features concerning the custom tests"""

from typing import Union
import regex as re
from glob import glob
from os.path import sep

from olivaw.test.corese import (
    safe_load,
    query_graph,
    Shacl,
    TripleFormat,
    TURTLE,
    CORESE_NAMESPACES,
    CORESE_PREFIX_TEXT
)


from olivaw.constants import (
    GET_VIOLATIONS,
    GET_VIOLATION,
    GET_CUSTOM_CRITERION_DATA,
    GIT_RAW,
    REPO_REF,
    BRANCH,
    EARL_NAMESPACE,
    GET_SHAPE_DESCRIPTION,
    GET_CRITERION_VALIDITY,
    CRITERION_IDS,
    ADD_VARIABLE,
    NEW_LINES
)

from rdflib import Graph, URIRef
from rdflib.namespace import RDF, SH

from olivaw.test.turtle import make_assertion, turtle_pointer, uri_pointer
from olivaw.test.util import smart_print
from olivaw.test.util.draft import AssertDraft
from olivaw.test.util.skip import should_skip

from py4j.java_gateway import JavaObject

test_features = [
    "Custom test graph must have one and only one criterion",
    "Criterion must be using relative paths syntax and document base should be left non assigned",
    "Criterion must have one and only one dcterms:title property",
    "Criterion title must be a string",
    "Criterion must have one and only one dcterms:description property",
    "Criterion description must be a string",
    "Criterion must have one and only one dcterms:identifier property",
    "Criterion identifier must be a string",
    "Identifier must be composed of lowercase letters and dashes"
]

def file_to_uri(file: str) -> str:
    """Returns the raw GitHub URI of a given custom test file

    :param file: The file path of that custom test file
    :type file: `str`

    :returns: The raw GitHub URI of the custom test file
    :rtype: `str`
    """
    cut_path = file.split(sep)
    test_name = cut_path[-1]
    test_type = cut_path[-2]

    return f"{GIT_RAW}/{REPO_REF}/{BRANCH}/.acimov/custom-tests/{test_type}/{test_name}#"

def complete_test_content(file: str) -> str:
    """Provides the content of a custom test file, updated with the `@base` keyword and the Corese known-by-default prefixes

    :param file: The custom test file path
    :type file: `str`

    :returns: The updated custom test turtle data
    :rtype: `str`
    """
    with open(file, "r") as shape_file:
        return f"@base <{file_to_uri(file)}> .\n{CORESE_PREFIX_TEXT}\n{shape_file.read()}"

def load_valid_custom_tests(files: list[str]) -> tuple[list[JavaObject], dict[str, dict[str, Union[str, list[str]]]]]:
    """Loads the custom tests that are valid to be integrated in olivaw tests
    
    :param files: List of custom tests to load
    :type files: `list[str]`

    :returns: List of custom tests loaded as graph, and a dictionary that provides tha data of the loaded custom tests
    :rtype: 

    ```
    tuple[
        list[JavaObject], # List of `py4j.java_gateway.JavaObject` referencing an instance of `fr.inria.corese.core.Graph`
        dict[ # dict containing information about all the custom tests
            str, # A custom test criterion identifier
            dict [ # A dict contaninig the information about a given custom test
                str, # A information name
                Union[str, List[str]] # Some useful information
            ]
        ]
    ]
    ```
    """
    custom_tests = []
    custom_tests_data = []
    new_criterion_identifiers = []

    files = glob(files)

    for file in files:
        content = complete_test_content(file)
        custom_test = safe_load([], extras=content, disable_owl=True)

        if isinstance(custom_test, list):
            smart_print(f"Custom test rejected (file {file})")
            smart_print(f"Cause: syntax error")
            for message in custom_test:
                smart_print(f"\t{message}")
            smart_print(" ")
            continue

        criterion_test = query_graph(custom_test, GET_CRITERION_VALIDITY.replace("FILE_URI", file_to_uri(file)))

        if len(criterion_test) != 1:
            smart_print(f"Custom test rejected (file {file})")
            smart_print(f"Cause: The file should contain one unique earl:TestCriterion")
            smart_print(" ")
            continue

        identifier, *criterion_test_result = criterion_test[0].split("\t")
        identifier = identifier[1:-1]
        criterion_test_result = [item == "true" for item in criterion_test_result]

        if len(criterion_test_result) != 9:
            smart_print(f"Custom test rejected (file {file})")
            smart_print(f"Cause: The custom test graph should have the following features")
            for criterion in test_features:
                smart_print(f"\t-{criterion}")
            smart_print(" ")
            continue

        if False in criterion_test_result:
            criterions = [
                test_features[i]
                for i in range(len(criterion_test_result))
                if not criterion_test_result[i]
            ]
            smart_print(f"Custom test rejected (file {file})")
            smart_print(f"Cause: The custom test graph should have the following features")
            for criterion in criterions:
                smart_print(f"\t-{criterion}")
            smart_print(" ")
            continue

        if identifier in CRITERION_IDS:
            smart_print(f"Custom test rejected (file {file})")
            smart_print(f"Cause: The custom test identifier should not be the one of a default test")
            smart_print(" ")
            continue

        if identifier in new_criterion_identifiers:
            smart_print(f"Custom test rejected (file {file})")
            smart_print(f"Cause: The custom test identifier should not be the one of another custom test")
            smart_print(" ")
            continue

        query_graph(custom_test, ADD_VARIABLE)

        custom_tests.append(custom_test)
        custom_tests_data.append(get_criterion_data(custom_test))
        new_criterion_identifiers.append(identifier)

        smart_print(f"Custom test {identifier} added (file {file})")
        smart_print(" ")
    
    return custom_tests, {
        line[1]: {
            "title": line[2],
            "description": line[3],
            "errors": [line[1]]
        }
        for line in custom_tests_data
    }

def load_custom_test(file: str) -> JavaObject:
    """Loads a given custom test

    :param file: File path to the custom test
    :type file: `str`

    :returns: `py4j.java_gateway.JavaObject` referencing an instance of `fr.inria.corese.core.Graph`
    """
    shape_content = complete_test_content(file)
    return safe_load([], extras=shape_content, disable_owl=True)

def get_criterion_data(test_file: str) -> tuple[str, str, str, str]:
    """Retrieves the useful information concerning a custom test criterion

    :param test_file: File path to the custom test file
    :type test_file: `str`

    :returns: The test criterion URI, identifier, title and description
    :rtype: `tuple[str, str, str, str]`
    """
    shape = load_custom_test(test_file) if isinstance(test_file, str) else test_file
    data = query_graph(shape, GET_CUSTOM_CRITERION_DATA)[0]
    return [item[1:-1] for item in data.split("\t")]

def indent_violation(violation: str) -> str:
    """Add indent to a custom test violation node turtle data

    :param violation: Turtle data of the violation node
    :type violation: `str`

    :returns: Same turtle data of violation node, with indent
    :rtype: `str`
    """
    lines = violation.split("\n")
    uri_subjects = [
        i
        for i, line in enumerate(lines)
        if len(line) > 0 and line[0] == "<"
    ]

    lines = [
        (
            f"\t{line}"
            if i > uri_subjects[0]
            and len(line) > 0
            and not line[0].startswith(" ")
            else line
        )
        for i, line in enumerate(lines)
    ]

    return NEW_LINES.sub("\n", "\n".join(lines))

def add_base(turtle: str, namespace: str) -> str:
    """Formats all the URIs using the relative path syntax for base namespace

    :param turtle: Turtle data
    :type turtle: `str`

    :param namespace: Base namespace
    :type namespace: `str`

    :returns: The parsed turtle data
    :rtype `str`
    """
    escaped_namespace = re.escape(namespace)
    uri_format = re.compile(f"(<{escaped_namespace})([^>]*)(>)")

    for match in uri_format.findall(turtle):
        found = "".join(match)
        turtle = turtle.replace(found, f"<{match[1]}>")

    return f"@base <{namespace}> .\n{turtle}"

def parse_violation_focus(
    draft: AssertDraft,
    violation_nodes: list[str],
    violation_focuses: list[str],
    is_focus_a_triple: list[bool]
    ) -> tuple[list[str], list[str]]:
    """Prepare the useful pointers for the report and parse the summary for human reading

    :param draft: The assertion draft containing the useful information for reporting
    :type draft: `olivaw.test.AssertDraft`

    :param violation_nodes: The violation nodes that can be found in the ShaCL report graph
    :type violation_nodes: `list[str]`

    :param violation_focuses: The focus nodes or triples that lead to each ShaCL violation
    :type violation_focuses: `list[str]`

    :param is_focus_a_triple: For each violation_node element, is it a focus triple?
    :type is_focus_a_triple: `list[bool]`
    
    :returns: A list of focus node descriptions and a list of parsed violation summaries
    :rtype: `tuple[list[str], list[str]]`
    """

    focus = []
    summaries = []

    for i, is_triple in enumerate(is_focus_a_triple):
        if not is_triple:
            focus.append(uri_pointer(draft, violation_focuses[i]))
            summaries.append(violation_nodes[i])
            continue

        graph = Graph()
        graph.parse(
            data=f"{CORESE_PREFIX_TEXT}\n{violation_nodes[i]}",
            format="ttl"
        )

        violation = [
            x for x in graph.subjects(
                predicate=RDF.type,
                object=SH.ValidationResult
            )
        ][0]

        focus_triple = [
            x for x in graph.objects(
                subject=violation,
                predicate=SH.focusNode
            )
        ][0]

        parsed_triple = parse_violation_triple(str(focus_triple))

        parsed_triple_list = parsed_triple.split("\n")
        parsed_triple_for_turtle = f"(\n\t\t{parsed_triple_list[0]}\n\t\t{parsed_triple_list[1]}\n\t\t{parsed_triple_list[2]}\n\t)"

        violation_nodes[i] = violation_nodes[i].replace(violation_focuses[i], parsed_triple_for_turtle)

        summaries.append(violation_nodes)

        focus.append(turtle_pointer(f"{CORESE_PREFIX_TEXT}\n{parsed_triple} ."))

    test_uri = "#".join(draft.criterion_uri.split("#")[:-1]) + "#"

    return focus, [
        turtle_pointer(
            violation_nodes_item,
            extra_prefix_declaration=[
                (draft.criterion, test_uri),
                ("violation", "urn:uuid:")
            ]
        )
        for violation_nodes_item in violation_nodes
    ]

def parse_violation_triple(triple: str) -> str:
    """Parse the focus triple in a violation summary to make it human-readable

    :param triple: The focus triple
    :type triple: `str`

    :returns: The parsed violation focus triple
    :rtype: `str`
    """
    triple = ">".join(triple.split(">")[1:]).strip()
    graph = Graph()
    turtle = f"{CORESE_PREFIX_TEXT}\n{triple} ."
    
    graph.parse(data=turtle, format="ttl")
    
    triple = [
        x for x
        in graph.triples((None, None, None))
    ][0]

    parsed = []

    for item in triple:
        if isinstance(item, URIRef):
            default_prefix = False
            for key, value in CORESE_NAMESPACES.items():
                if item.startswith(value):
                    default_prefix = True
                    parsed.append(f"{key}:{item[len(value):]}")
                    break
            if default_prefix:
                continue
            parsed.append(f"<{item}>")
        else:
            parsed.append(item.n3())
            

    parsed = '\n'.join(parsed)
    return parsed

def custom_test(
    draft: AssertDraft,
    fragment_graph: JavaObject,
    shapes: list[JavaObject]
) -> None:
    """Executes the custom tests pas in parameter to the fragment passed in parameter

    :param draft: The assertion draft containing the useful information for reporting
    :type draft: `olivaw.test.AssertDraft`

    :param fragment_graph: The fragment to be tested
    :type fragment_graph: `py4j.java_gateway.JavaObject` referencing an instance of `fr.inria.corese.core.Graph`

    :param shapes: List of graphs containing the information of each custom tests
    :type shapes: `list[py4j.java_gateway.JavaObject]` with each `py4j.java_gateway.JavaObject` referencing an instance of `fr.inria.corese.core.Graph`
    """
    for shape in shapes:
        criterion_uri, criterion_identifier, *_ = get_criterion_data(shape)

        draft(
            graph=fragment_graph, 
            criterion=criterion_identifier,
            criterion_uri=criterion_uri
        )

        if should_skip(draft, criterion=criterion_identifier):
            continue
        
        criterion_namespace = "#".join(criterion_uri.split("#")[:-1])
    
        shacl = Shacl(fragment_graph, shape)
        result = shacl.eval()

        shacl_report = TripleFormat.create(result).toString()
        shacl_report = safe_load([], extras=shacl_report, disable_owl=True)

        violations = query_graph(shacl_report, GET_VIOLATIONS)
        violations = [violation.split("\t") for violation in violations]
        violation_nodes = [violation[0] for violation in violations]
        violation_focuses = [violation[1] for violation in violations]
        is_focus_triple = [violation[2] == "true" for violation in violations]

        messages = [f"Violation of constraint in the custom test '{criterion_identifier}'"] if len(violation_nodes) > 0 else []

        violation_nodes = [
                add_base(
                    indent_violation(
                        query_graph(
                            shacl_report,
                            GET_VIOLATION.replace("VIOLATION_URI", violation_uri),
                            format=TURTLE
                        )
                    ),
                    criterion_namespace
                )
            for violation_uri in violation_nodes
        ]

        violation_focuses, violation_nodes = parse_violation_focus(
            draft,
            violation_nodes,
            violation_focuses,
            is_focus_triple
        )

        pointers = {}

        for violation_node, focus in zip(violation_nodes, violation_focuses):
            if focus in pointers:
                pointers[focus].append(violation_node)
            else:
                pointers[focus] = [violation_node]

        pointers = [
            pointer
            for node, summaries in pointers.items()
            for pointer in summaries + [node]
        ]

        if len(pointers) > 0:
            shape_content = TripleFormat.create(shape).toString()
            shape_content = f"{CORESE_PREFIX_TEXT}\n{shape_content}"

            rdflib_shape = Graph()
            rdflib_shape.bind("earl", EARL_NAMESPACE)
            rdflib_shape.parse(data=shape_content, format="ttl")

            shape_description = rdflib_shape.query(GET_SHAPE_DESCRIPTION)
            shape_description = shape_description.serialize(format="ttl").decode()
            shape_description = add_base(shape_description, criterion_namespace)

            pointers = [[turtle_pointer(
                shape_description,
                extra_prefix_declaration=[("", f"{criterion_namespace}#")]
            )] + pointers]
        else:
            pointers = []

        make_assertion(
            draft,
            error=criterion_identifier,
            messages=messages,
            pointers=pointers,
            graph=fragment_graph
        )