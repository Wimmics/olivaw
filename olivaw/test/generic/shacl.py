import regex as re
from glob import glob
from os.path import sep

from olivaw.test.corese import (
    safe_load,
    query_graph,
    Shacl,
    TripleFormat,
    TURTLE,
    corese_namespaces,
    corese_prefix_text,
    smartPrint
)

from olivaw.test.turtle import make_assertion

from olivaw.constants import (
    GET_VIOLATIONS,
    GET_VIOLATION,
    SKIPPED_TESTS,
    GET_CRITERION_URI,
    GET_CUSTOM_CRITERION_DATA,
    GIT_RAW,
    REPO_REF,
    BRANCH,
    EARL_NAMESPACE,
    GET_SHAPE_DESCRIPTION,
    NEW_LINES,
    GET_CRITERION_VALIDITY,
    CRITERION_IDS,
    ONTOLOGY_URL
)

from rdflib import Graph, URIRef
from rdflib.namespace import RDF, SH

test_features = [
    "Custom test graph must have one and only one criterion",
    "Criterion must be using relative paths and document base should be left non assigned",
    "Criterion must have one and only one dcterms:title property",
    "Criterion title must be a string",
    "Criterion must have one and only one dcterms:description property",
    "Criterion description must be a string",
    "Criterion must have one and only one dcterms:identifier property",
    "Criterion identifier must be a string",
    "Identifier must be composed of lowercase letters and dashes"
]

def file_to_uri(file):
    cut_path = file.split(sep)
    test_name = cut_path[-1]
    test_type = cut_path[-2]

    return f"{GIT_RAW}/{REPO_REF}/{BRANCH}/.acimov/custom-tests/{test_type}/{test_name}#"

def complete_test_content(file):
    with open(file, "r") as shape_file:
        return f"@base <{file_to_uri(file)}> .\n{corese_prefix_text}\n{shape_file.read()}".replace("ONTOLOGY_URL", ONTOLOGY_URL)

def load_valid_custom_tests(files):
    custom_tests = []
    new_criterion_identifiers = []

    files = glob(files)

    for file in files:
        content = complete_test_content(file)
        custom_test = safe_load([], extras=content, disable_owl=True)

        if isinstance(custom_test, list):
            smartPrint(f"Custom test rejected (file {file})")
            smartPrint(f"Cause: syntax error")
            for message in custom_test:
                smartPrint(f"\t{message}")
            smartPrint(" ")
            continue

        criterion_test = query_graph(custom_test, GET_CRITERION_VALIDITY.replace("FILE_URI", file_to_uri(file)))

        if len(criterion_test) != 1:
            smartPrint(f"Custom test rejected (file {file})")
            smartPrint(f"Cause: The file should contain one unique earl:TestCriterion")
            smartPrint(" ")
            continue

        identifier, *criterion_test_result = criterion_test[0].split("\t")
        identifier = identifier[1:-1]
        criterion_test_result = [item == "true" for item in criterion_test_result]

        if len(criterion_test_result) != 9:
            smartPrint(f"Custom test rejected (file {file})")
            smartPrint(f"Cause: The custom test graph should have the following features")
            for criterion in test_features:
                smartPrint(f"\t-{criterion}")
            smartPrint(" ")
            continue

        if False in criterion_test_result:
            criterions = [
                test_features[i]
                for i in range(len(criterion_test_result))
                if not criterion_test_result[i]
            ]
            smartPrint(f"Custom test rejected (file {file})")
            smartPrint(f"Cause: The custom test graph should have the following features")
            for criterion in criterions:
                smartPrint(f"\t-{criterion}")
            smartPrint(" ")
            continue

        if identifier in CRITERION_IDS:
            smartPrint(f"Custom test rejected (file {file})")
            smartPrint(f"Cause: The custom test identifier should not be the one of a default test")
            smartPrint(" ")
            continue

        if identifier in new_criterion_identifiers:
            smartPrint(f"Custom test rejected (file {file})")
            smartPrint(f"Cause: The custom test identifier should not be the one of another custom test")
            smartPrint(" ")
            continue

        custom_tests.append(custom_test)
        new_criterion_identifiers.append(identifier)

        smartPrint(f"Custom test {identifier} added (file {file})")
        smartPrint(" ")
    
    return custom_tests


def load_custom_test(file):
    shape_content = complete_test_content(file)
    return safe_load([], extras=shape_content, disable_owl=True)

def get_criterion_data(test_file):
    shape = load_custom_test(test_file) if isinstance(test_file, str) else test_file
    data = query_graph(shape, GET_CUSTOM_CRITERION_DATA)[0]
    return [item[1:-1] for item in data.split("\t")]

def indent_violation(violation):
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

def add_base(turtle, namespace):
    escaped_namespace = re.escape(namespace)
    uri_format = re.compile(f"(<{escaped_namespace})([^>]*)(>)")

    for match in uri_format.findall(turtle):
        found = "".join(match)
        turtle = turtle.replace(found, f"<#{match[1]}>")

    return f"@base <{namespace}> .\n{turtle}"

def parse_violation_focus(
    violation_summaries,
    violation_nodes,
    violation_triples
    ):

    focus = []
    summaries = []

    for i, is_triple in enumerate(violation_triples):
        if not is_triple:
            focus.append(violation_nodes[i])
            summaries.append(violation_summaries[i])
            continue

        graph = Graph()
        graph.parse(
            data=f"{corese_prefix_text}\n{violation_summaries[i]}",
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

        parsed_triple_for_turtle = parsed_triple.split("\n")
        parsed_triple_for_turtle = f"(\n\t\t{parsed_triple_for_turtle[0]}\n\t\t{parsed_triple_for_turtle[1]}\n\t\t{parsed_triple_for_turtle[2]}\n\t)"

        violation_summaries[i] = violation_summaries[i].replace(violation_nodes[i], parsed_triple_for_turtle)

        summaries.append(
            violation_summaries
        )
        focus.append(f"{corese_prefix_text}\n{parsed_triple}")

    return focus, violation_summaries

def parse_violation_triple(triple):
    triple = ">".join(triple.split(">")[1:]).strip()
    graph = Graph()
    turtle = f"{corese_prefix_text}\n{triple} ."
    
    graph.parse(data=turtle, format="ttl")
    
    triple = [
        x for x
        in graph.triples((None, None, None))
    ][0]

    parsed = []

    for item in triple:
        if isinstance(item, URIRef):
            default_prefix = False
            for key, value in corese_namespaces.items():
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
    report,
    assertor,
    subject,
    fragment_graph,
    shapes,
    skip_pass=False,
    tested_only=False
):
    
    for shape in shapes:
        criterion_uri, criterion_identifier, *_ = get_criterion_data(shape)

        if criterion_identifier in SKIPPED_TESTS:
            continue
        
        criterion_identifier = criterion_identifier[1:-1]
        criterion_namespace = "#".join(criterion_uri.split("#")[:-1]) + "#"

        if criterion_identifier in SKIPPED_TESTS:
            return
    
        shacl = Shacl(fragment_graph, shape)
        result = shacl.eval()

        shacl_report = TripleFormat.create(result).toString()
        shacl_report = safe_load([], extras=shacl_report, disable_owl=True)

        violations = query_graph(shacl_report, GET_VIOLATIONS)
        violations = [violation.split("\t") for violation in violations]
        violation_uris = [violation[0] for violation in violations]
        violation_nodes = [violation[1] for violation in violations]
        violation_triples = [violation[2] == "true" for violation in violations]

        messages = [f"Violation of constraint in the custom test '{criterion_identifier}'"] if len(violation_uris) > 0 else []

        violation_summaries = [
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
            for violation_uri in violation_uris
        ]

        violation_nodes, violation_summaries = parse_violation_focus(
            violation_summaries,
            violation_nodes,
            violation_triples
        )

        pointers = {}

        for summary, node in zip(violation_summaries, violation_nodes):
            if node in pointers:
                pointers[node].append(summary)
            else:
                pointers[node] = [summary]

        pointers = [
            pointer
            for node, summaries in pointers.items()
            for pointer in summaries + [node]
        ]

        if len(pointers) > 0:
            shape_content = TripleFormat.create(shape).toString()
            shape_content = f"{corese_prefix_text}\n{shape_content}"
            rdflib_shape = Graph()
            rdflib_shape.bind("earl", EARL_NAMESPACE)
            rdflib_shape.parse(data=shape_content, format="ttl")

            shape_description = rdflib_shape.query(GET_SHAPE_DESCRIPTION)

            shape_description = shape_description.serialize(format="ttl").decode()

            shape_description = add_base(shape_description, criterion_namespace)

            pointers = [[shape_description] + pointers]
        else:
            pointers = []

        criterion = query_graph(shape, GET_CRITERION_URI)[0][1:-1]

        make_assertion(
            report,
            assertor,
            subject,
            criterion,
            f"{criterion_identifier}-error",
            messages,
            pointers=pointers,
            graph=fragment_graph,
            skip_pass=skip_pass,
            tested_only=tested_only
        )