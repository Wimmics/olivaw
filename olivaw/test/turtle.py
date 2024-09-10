"""Module providing functions for turtle report format generation"""

from datetime import datetime
from itertools import zip_longest
from typing import Optional

from os.path import sep, abspath

from py4j.java_gateway import JavaObject

from rdflib import (
    Graph,
    BNode,
    IdentifiedNode,
    Literal,
    URIRef,
    Namespace
)

from rdflib.namespace import (
    RDF,
    FOAF,
    DCTERMS,
    SDO,
    XSD,
    PROV
)

from olivaw.constants import (
    DEV_USERNAME,
    DEV_PROFILE,
    DOMAINS_URL,
    EARL_NAMESPACE,
    COMMIT_DATE,
    REPO_STATE,
    PLATFORM_NAMESPACE,
    ONTOLOGY_PREFIX,
    ONTOLOGY_NAMESPACE,
    PROJECT_PREFIXES,
    SRC_NAMESPACE,
    OLIVAW_NAMESPACE,
    ONTOLOGY_RDFLIB_NAMESPACE,
    ERROR_RESOURCES,
    BRANCH,
    USECASES_URL,
    SKIPPED_ERRORS,
    EXTRACT_STATEMENT,
    OLIVAW_VERSION_BLOB_URI,
    OLIVAW_TEST_BLOB_URI,
    BLOCKING_ERRORS,
    MODE,
    SKIP_PASS,
    TESTED_ONLY,
    CRITERION_DATA,
    COMMIT_HASH,
    ACTIONS,
    REPO_URI,
    VERSION,
    REPO_REF
)

from olivaw.constants.regex import PREFIX_PATTERN
from olivaw.constants.regex import URI_PATTERN
from olivaw.constants.sparql import (
    ADD_DESCRIPTION_LINKS,
    GET_OBJECT_USAGE,
    GET_PREDICATE_USAGE,
    REMOVE_DESCRIPTION_LINKS,
    SHORTEN_LITERALS
)

from olivaw.test.corese import (
    TURTLE,
    CORESE_PREFIX_TEXT,
    CORESE_NAMESPACES
)

from olivaw.test.util import AssertDraft, should_skip
from olivaw.constants.paths import PWD_TO_OUTPUT_FOLDER

def new_report(test_type: str) -> tuple[Graph, BNode]:
    """Creates a new report and add the assertor

    :param test_type: The type of test that this report will be used for
    :type test_type: `str`

    :return: The report and the assertor
    :rtype: `rdflib.BNode`
    """
    report = Graph()

    report.bind("earl", EARL_NAMESPACE)
    report.bind("", ONTOLOGY_RDFLIB_NAMESPACE)
    report.bind("olivaw", OLIVAW_NAMESPACE)
    report.bind("dcterms", DCTERMS)
    report.bind("prov", PROV)
    report.bind("git-platform", PLATFORM_NAMESPACE)

    assertor = make_assertor(report, test_type)

    return report, assertor

def make_assertor(report: Graph, test_type: str) -> BNode:
    """Writes an assertor in the report and returns the assertor

    :param report: The test report
    :type report: `rdflib.Graph`

    :return: The assertor node
    :rtype: `rdflib.BNode`
    """

    triples = []

    # Instanciate tester and its association
    tester = BNode("tester")
    triples.extend([
        (tester, RDF.type, FOAF.Person), 
        (tester, RDF.type, PROV.Agent),
        (tester, FOAF.homepage, PLATFORM_NAMESPACE[DEV_USERNAME]),
        (tester, FOAF.nick, Literal(DEV_USERNAME))
    ])

    tester_association = BNode("testerAssociation")
    triples.extend([
        (tester_association, RDF.type, PROV.Association),
        (tester_association, PROV.agent, tester),
        (tester_association, PROV.hadRole, OLIVAW_NAMESPACE.tester)
    ])

    # Instanciate tested project and its association
    tested_project = URIRef(f"{REPO_URI}/tree/{COMMIT_HASH}") if ACTIONS else BNode("intermediateSnapshot")
    triples.extend([
        (tested_project, RDF.type, OLIVAW_NAMESPACE.VersionedEntity),
        (tested_project, OLIVAW_NAMESPACE.hostedAt, URIRef(REPO_URI)),
        (tested_project, OLIVAW_NAMESPACE.isOnBranch, Literal(BRANCH)),
        (tested_project, OLIVAW_NAMESPACE.patchedBy, tester)
    ])

    if ACTIONS:
        triples.extend([
            (tested_project, DCTERMS.hasVersion, Literal(COMMIT_HASH)),
            (tested_project, DCTERMS.date, Literal(COMMIT_DATE, datatype=XSD.dateTime))
        ])
    else:
        triples.extend([
            (tested_project, DCTERMS.hasVersion, Literal(REPO_STATE)),
            (tested_project, OLIVAW_NAMESPACE.patchedFrom, Literal(COMMIT_HASH)),
            (tested_project, DCTERMS.date, Literal(datetime.now(), datatype=XSD.dateTime))
        ])

    tested_project_association = BNode("testedProjectUsage")
    triples.extend([
        (tested_project_association, RDF.type, PROV.Usage),
        (tested_project_association, PROV.entity, tested_project),
        (tested_project_association, PROV.hadRole, OLIVAW_NAMESPACE.tested_project)
    ])

    # Instanciate test suite and its association
    test_suite = URIRef(f"{OLIVAW_VERSION_BLOB_URI}/olivaw/test/{test_type}/suite.py")
    triples.extend([
        (test_suite, RDF.type, OLIVAW_NAMESPACE.VersionedEntity),
        (test_suite, OLIVAW_NAMESPACE.hostedAt, URIRef(f"{OLIVAW_TEST_BLOB_URI}/{test_type}/suite.py")),
        (test_suite, DCTERMS.hasVersion, Literal(VERSION))
    ])

    tested_suite_association = BNode("testSuiteUsage")
    triples.extend([
        (tested_suite_association, RDF.type, PROV.Usage),
        (tested_suite_association, PROV.entity, test_suite),
        (tested_suite_association, PROV.hadRole, OLIVAW_NAMESPACE.test_suite)
    ])

    # Instanciate activity
    assertor = BNode("assertor")
    triples.extend([
        (assertor, RDF.type, PROV.Activity),
        (assertor, RDF.type, EARL_NAMESPACE.Assertor),
        (assertor, PROV.wasAssociatedWith, tester),
        (assertor, PROV.qualifiedAssociation, tester_association),
        (assertor, PROV.used, test_suite),
        (assertor, PROV.qualifiedUsage, tested_suite_association),
        (assertor, PROV.used, tested_project),
        (assertor, PROV.qualifiedUsage, tested_project_association),
        (assertor, DCTERMS.title, Literal(f"{test_type.capitalize()} tests of {REPO_REF} on branch {BRANCH}")),
        (assertor, DCTERMS.description, Literal(f"{DEV_USERNAME} launch {MODE} run of {test_type} tests against {REPO_REF} on branch {BRANCH}"))
    ])
    
    for triple in triples:
        report.add(triple)
    
    return assertor

def end_activity(report: Graph, assertor: IdentifiedNode, reports_filename: str) -> None:
    """Add the extra information at the end of an activity
    
    :param report: Test report
    :type report: `rdflib.Graph`

    :param assertor: Test assertor
    :type assertor: `rdflib.IdentifiedNode`

    :param reports_filename: Report files path and file name
    :type reports_filename: `str`
    """
    reports_path = f"{PWD_TO_OUTPUT_FOLDER}{reports_filename}"
    turtle_report_uri = URIRef(f"file:///{abspath(reports_path).replace(sep, '/')}.ttl")
    markdown_report_uri = URIRef(f"file:///{abspath(reports_path).replace(sep, '/')}.md")

    turtle_generation = BNode("turtleGeneration")
    markdown_generation = BNode("markdownGeneration")

    activity_end_time = datetime.now()

    for triple in [
        # Add end time of activity and generated files
        (assertor, PROV.endedAtTime, Literal(activity_end_time, datatype=XSD.dateTime)),
        (assertor, PROV.generated, turtle_report_uri),
        (assertor, PROV.generated, markdown_report_uri),
        # Adding turtle file generation
        (turtle_report_uri, RDF.type, PROV.Entity),
        (turtle_report_uri, PROV.generatedAtTime, Literal(activity_end_time, datatype=XSD.dateTime)),
        (turtle_report_uri, PROV.qualifiedGeneration, turtle_generation),
        # Qualifying turtle file generation
        (turtle_generation, RDF.type, PROV.Generation),
        (turtle_generation, PROV.activity, assertor),
        (turtle_generation, OLIVAW_NAMESPACE.generatedAs, OLIVAW_NAMESPACE.turtle_report),
        # Adding markdown file generation
        (markdown_report_uri, RDF.type, PROV.Entity),
        (markdown_report_uri, PROV.generatedAtTime, Literal(activity_end_time, datatype=XSD.dateTime)),
        (markdown_report_uri, PROV.qualifiedGeneration, markdown_generation),
        # Qualifying markdown file generation
        (markdown_generation, RDF.type, PROV.Generation),
        (markdown_generation, PROV.activity, assertor),
        (markdown_generation, OLIVAW_NAMESPACE.generatedAs, OLIVAW_NAMESPACE.markdown_report)
    ]:
        report.add(triple)

def make_subject_id_part(fragment_list: list[str]) -> str:
    """Analyze the heart or appendix of a subject and generate the subject identifier part related to this

    :param fragment_list: List of files from the heart or appendix of a subject
    :type fragment_list: `list[str]`

    :return: Subject identifier part
    :rtype: `str`
    """

    modules = [item for item in fragment_list if item.startswith("src/")]
    modules = ['module-' + '.'.join(item.split('.')[:-1]) for item in modules]
    modules.sort()
    modelets = [item for item in fragment_list if item.startswith("domains/") and item.endswith("/onto.ttl")]
    modelets = ['modelet-' + '-'.join(item.split('/')[1:-1]) for item in modelets]
    modelets.sort()
    datasets = [item for item in fragment_list if item.startswith("domains/") and item.endswith("/dataset.ttl")]
    datasets = ['dataset-' + '-'.join(item.split('/')[1:-1]) for item in datasets]
    datasets.sort()
    questions = [item for item in fragment_list if item.startswith("domains/") and item.endswith(".rq")]
    questions = ['question-' + '-'.join(item[:-3].split('/')[1:]) for item in questions]
    questions.sort()
    usecases = [item for item in fragment_list if item.startswith("use-cases/")]
    usecases = [
        'usecase-' + '-'.join('.'.join(item.split('.')[:-1]).split('/')[1:])
        for item in usecases
    ]
    usecases.sort()

    subject_id_part = '-'.join(modules + modelets + datasets + questions + usecases).replace(".", "-").replace("_", "-")
    return subject_id_part

def make_subject_id(heart: list[str], appendix: list[str]=[]) -> str:
    """Computes the subject identifier of a subject

    :param heart: List of file paths that are the heart of the subject
    :type heart: `list[str]`

    :param appendix: List of file paths that are the appendix of the subject, defaults to `[]`
    :type appendix: `list[str]`, optional

    :return: The subject identifier
    :rtype: `str`
    """

    result = [make_subject_id_part(heart)]

    if len(appendix):
        appendix_id = make_subject_id_part(appendix)
        result.append(appendix_id)

    subject_id = "-".join(result).replace("/", "-")
    return subject_id

def make_subject(
        draft: AssertDraft,
        heart: list[str],
        appendix: list[str]=[],
        name: str="",
        custom_title: str=""
):
    """Writes the test subject in the report and returns it

    :param draft: Draft of the test
    :type draft: `olivaw.test.AssertDraft`
    
    :param heart: List of file paths that are the heart of the subject
    :type heart: `list[str]`

    :param appendix: List of file opaths that are the appendix of the subject, defaults to `[]`
    :type appendix: `list[str]`, optional

    :param name: Desired subject identifier, defaults to `""` and compute it
    :type name: `str`, optional

    :param custom_title: Desired subject title, defaults to `""` and compute it
    :type custom_title: `str`, optional

    :return: The node representing the test subject
    :rtype: `rdflib.BNode`
    """

    subject_id = make_subject_id(heart, appendix=appendix) if name == "" else name

    if len(heart) > 1:
        heart_type = "Set of fragments"
    else:
        if len(appendix) == 0:
            heart_type = "Standalone "
        else:
            heart_type = "Merged "
        
        if heart[0].startswith("src/"):
            heart_type += "module"
        elif heart[0].startswith("domains/"):
            if heart[0].endswith("/onto.ttl"):
                heart_type += "modelet"
            elif heart[0].endswith("/dataset.ttl"):
                heart_type += "dataset"
            else:
                heart_type = "competency question"
        else:
            heart_type += "use case"
    
    title = f"{heart_type} {', '.join(heart)} from branch {BRANCH}"

    if len(appendix) > 0:
        title = f"{title} with related terms from the fragments {', '.join(appendix)}"

    title = title if len(custom_title) == 0 else custom_title
    
    module_fragments = [item for item in heart + appendix if item.startswith('src/')]
    module_fragments = [
        SRC_NAMESPACE[item[4:]]
        for item in module_fragments
    ]

    modelets_fragment = [
        item
        for item in heart + appendix
        if item.startswith('domains/')
        and item.endswith('/onto.ttl')
    ]
    modelets_fragment = [
        URIRef(DOMAINS_URL + item.split("domains/")[-1])
        for item in modelets_fragment
    ]

    datasets_fragment = [
        item
        for item in heart + appendix
        if item.startswith('domains/')
        and item.endswith('/dataset.ttl')
    ]
    datasets_fragment = [
        URIRef(DOMAINS_URL + item.split("domains/")[-1])
        for item in datasets_fragment
    ]

    questions_fragment = [
        item
        for item in heart + appendix
        if item.startswith('domains/')
        and item.endswith('.rq')
    ]
    questions_fragment = [
        URIRef(DOMAINS_URL + item.split("domains/")[-1])
        for item in questions_fragment
    ]
    
    usecases_fragment = [item for item in heart + appendix if item.startswith('use-cases/')]
    usecases_fragment = [
        URIRef(USECASES_URL + item.split("use-cases/")[-1])
        for item in usecases_fragment
    ]

    test_subject = BNode(subject_id, subject_id)
    statements = [
        (DCTERMS.hasPart, part)
        for part in module_fragments + modelets_fragment + datasets_fragment + questions_fragment + usecases_fragment
    ]

    statements = [
        (RDF.type, EARL_NAMESPACE.TestSubject),
        (DCTERMS.title, Literal(title, lang="en")),
        (DCTERMS.identifier, Literal(subject_id))
    ] + statements

    draft.reporting(test_subject, statements)

    return test_subject

def separate_prefix_data(statement: str, is_literal: bool=False) -> str:
    """Remove the prefixes declaration from a code snippet

    :param statement: the code snippet
    :type statement: `str`

    :param is_literal: is the code snippet already parsed, defaults to `False`
    :type is_literal: `bool`, optional
    """
    if is_literal:
        return statement

    parsed_statement = [
        line
        for line in statement.split("\n")
        if len(line.strip()) > 0
    ]
        
    for i in range(len(parsed_statement)):
        if not parsed_statement[i].startswith("@"):
            return "\n".join(parsed_statement[:max(0, i)]), "\n".join(parsed_statement[i:len(parsed_statement)])
    
    return "\n".join(parsed_statement), ""

def parse_statement(raw_statement: str) -> str:
    """Returns a human-friendly version of a code snippet passed as input

    :param raw_statement: the code snippet
    :type raw_statement: `str`

    :return: the code snippet represented in a human friendly way
    :rtype: `str`
    """
    rdf = f"{CORESE_PREFIX_TEXT}\n{raw_statement}"
    if not rdf.strip().endswith("."):
        rdf = f"{rdf} ."
    isolated_graph = Graph()
    isolated_graph.parse(data=rdf, format="ttl")

    result = Graph()
    for triple in isolated_graph.query(SHORTEN_LITERALS):
        result.add(triple)
    return separate_prefix_data(result.serialize(format="ttl"))

def extract_statement(graph: JavaObject, pointer: URIRef) -> Literal:
    """Returns a RDF Literal of a code snippet containing all the relevant data about the URI passed as input
    
    :param graph: Corese Graph that contains the information about the required URI
    :type graph: `py4j.java_gateway.JavaObject` referencing an instance of `fr.inria.corese.core.Graph`

    :param pointer: The URI that will be defined by the code snippet
    :type pointer: `rdflib.URIRef`

    :return: Literal containing the code snippet
    :rtype: `rdflib.Literal`
    """
    graph.query(ADD_DESCRIPTION_LINKS.replace("TERM", pointer))
    statement = graph.query(EXTRACT_STATEMENT.replace("TERM", pointer), format=TURTLE).strip()
    graph.query(REMOVE_DESCRIPTION_LINKS)

    if len(statement) == 0:
        statement = graph.query(GET_PREDICATE_USAGE.replace("TERM", pointer), format=TURTLE).strip()

    if len(statement) == 0:
        statement = graph.query(GET_OBJECT_USAGE.replace("TERM", pointer), format=TURTLE).strip()

    if len(statement) == 0:
        return Literal(str(pointer))
    
    for match in URI_PATTERN.findall(statement):
        statement = statement.replace(match, match.replace("\\/", "/"))

    pointer_separator = [i for i in range(len(pointer)) if pointer[i] in ["#", "/", "="]]
    pointer_namespace = pointer[:pointer_separator[-1]+1]

    pretty_pointer = make_readable_turtle(
        statement,
        extra_prefix_declaration=[("", Namespace(pointer_namespace))]
    )
    return Literal(separate_prefix_data(pretty_pointer)[1])

def make_readable_turtle(turtle: str, extra_prefix_declaration: list[tuple[str, str]] = []) -> str:
    """Parses some turtle data to make it more human readable
    
    :param turtle: The turtle data content
    :type pointer: `str`

    :param extra_prefix_declaration: Set of extra prefix definitions with namespaces to use for the turtle data, defaults to empty `[]`
    :type extra_prefix_declaration: `list[tuple[str, str]]`, optional

    :returns: The human readable version of the pointer
    :rtype: `str`
    """
    turtle_prefixes, turtle_data = separate_prefix_data(turtle)
    total_turtle = f"{turtle_prefixes}\n{CORESE_PREFIX_TEXT}\n{turtle_data}".strip()

    prefix_declaration = [
        (
            prefix,
            namespace if isinstance(namespace, Namespace) else
            Namespace(namespace)
        )
        for prefix, namespace in
            list(CORESE_NAMESPACES.items()) + \
            [(ONTOLOGY_PREFIX, ONTOLOGY_NAMESPACE)] + \
            PREFIX_PATTERN.findall(turtle_prefixes) + \
            list(PROJECT_PREFIXES.items()) + \
            extra_prefix_declaration
    ]

    parser_graph = Graph()
    parser_graph.parse(data=total_turtle, format="ttl")

    parsed_graph = Graph()

    parsed_graph.parse(
        format="ttl",
        data=parser_graph\
            .query(SHORTEN_LITERALS)\
            .serialize(format="ttl")\
            .decode()
    )

    for prefix, namespace in prefix_declaration:
        parsed_graph.bind(prefix, namespace, replace=True)

    return parsed_graph.serialize(format="ttl")
    

def uri_pointer(draft: AssertDraft, uri: str) -> Literal:
    """Makes a pointer containing some turtle definition of a URI

    :param draft: The assertion draft containing the useful information for reporting
    :type draft: `olivaw.test.AssertDraft`
    
    :param uri: The URI
    :type uri: `str`

    :returns: The pointer node to use for the report
    :rtype: `rdlib.Literal`
    """
    if uri[0] == "<":
        return extract_statement(draft.graph, URIRef(uri[1:-1].replace("\\/", "/")))
    
    uri_prefix, uri_suffix = uri.split(":")
    if uri.split(":")[0] == "_":
        return Literal(uri)
    
    return URIRef(
        [
            namespace for prefix, namespace in draft.report.namespaces()
            if prefix == uri_prefix
        ][0] + uri_suffix
    )

def text_pointer(pointer: str) -> Literal:
    """Makes a pointer containing some text
    
    :param pointer: The text content
    :type pointer: `str`

    :returns: The pointer node to use for the report
    :rtype: `rdlib.Literal`
    """
    return Literal(pointer.strip())

def turtle_pointer(pointer: str, extra_prefix_declaration: list[tuple[str, str]] = []) -> Literal:
    """Makes a pointer containing some turtle data
    
    :param pointer: The turtle data content
    :type pointer: `str`

    :param extra_prefix_declaration: Set of extra prefix definitions with namespaces to use for the turtle data, defaults to empty `[]`
    :type extra_prefix_declaration: `list[tuple[str, str]]`, optional

    :returns: The pointer node to use for the report
    :rtype: `rdlib.Literal`
    """
    return Literal(
        separate_prefix_data(
            make_readable_turtle(
                pointer,
                extra_prefix_declaration=extra_prefix_declaration
            )
        )[1]
    )

def make_outcome(draft: AssertDraft, **kwargs) -> Optional[BNode]:
    """Makes an outcome given the information stored in the draft
    
    :param draft: The assertion draft
    :type draft: `olivaw.test.AssertDraft`

    :param **kwargs: Optional set of parameters to set to the `olivaw.test.AssertDraft` instance
    :type **kwargs: See `olivaw.test.AssertDraft` for more details

    :return: A node representing the outcome
    :rtype: `rdflib.BNode` or `NoneType` if outcome should be skipped 
    """

    draft(**kwargs)

    if should_skip(draft):
        return None
        
    test_name = draft.criterion.split('/')[-1].split('#')[0]
    test_name = '.'.join(test_name.split('.')[:-1])
    outcome_title = f"Test {test_name} passed" if draft.outcome_type == "Pass" else f"Error on custom test {test_name}"
    outcome_description = f"The custom test {test_name} passed" if draft.outcome_type == "Pass" else \
        (
            f"Custom test {test_name} could not be run because the subject could not be loaded in the engine" \
                if draft.outcome_type == "NotTested" else \
            f"Error occured while running custom test {test_name}" 
        )
    
    if draft.error in ERROR_RESOURCES:
        outcome_ressources = ERROR_RESOURCES[draft.error][draft.outcome_type]
        outcome_title = outcome_ressources["title"]
        outcome_description = draft.description if (draft.has_field("description") and len(draft.description) > 0) else outcome_ressources["description"]

    outcome_type_namespace = OLIVAW_NAMESPACE if draft.outcome_type.endswith("Fail") else EARL_NAMESPACE

    outcome_statement = [
        (RDF.type, outcome_type_namespace[draft.outcome_type]),
        (DCTERMS.identifier, Literal(draft.error)),
        (DCTERMS.title, Literal(outcome_title, lang="en")),
        (DCTERMS.description, Literal(outcome_description, lang="en"))
    ] + [
        (
            EARL_NAMESPACE["info" if isinstance(pointer, Literal) else "pointer"],
            pointer
        )
        for pointer in draft.pointers
    ]

    outcome = BNode()
    draft.reporting(outcome, outcome_statement)

    return outcome

def make_outcomes(draft: AssertDraft) -> list[BNode]:
    """Prepare outcomes in the report given the information stored in the draft

    :param draft: The test assertion draft
    :type draft: `olivaw.test.AssertDraft`

    :return: A list of Nodes representing each generated outcomes
    :rtype: `list[BNode]`
    """
    if isinstance(draft.error, list):
        return [
            outcome
            for outcome_pack in [
                make_outcomes(
                    draft(
                        outcome_type=None,
                        error=error,
                        messages=messages,
                        pointers=pointers
                    )
                )
                for error, messages, pointers
                in zip(
                    draft.error,
                    draft.messages,
                    draft.pointers
                )
            ]
            for outcome in outcome_pack
        ]

    draft.fix_pointers()
    outcomes = []

    if draft.error in SKIPPED_ERRORS:
        return []

    if len(draft.messages) == 0:
        if SKIP_PASS:
            return []
        outcomes = [make_outcome(draft(outcome_type="Pass"))]
    else:
        if not draft.has_field("outcome_type"):
            draft(outcome_type="MajorFail" if draft.error in BLOCKING_ERRORS else "MinorFail")

        outcomes = [
            make_outcome(draft(description=message, pointers=pointers))
            for message, pointers
            in zip_longest(draft.messages, draft.pointers, fillvalue=[])
        ]

    return outcomes

def make_result(draft: AssertDraft, outcomes: list[BNode]) -> BNode:
    """Prepare a Result node given the output passed in parameter
    
    :param draft: Test assertion draft
    :type draft: `olivaw.test.AssertDraft`

    :param outcomes: List of the outcome to be linked to the result
    :type outcomes: `list[BNode]`

    :return: A BNode representing the result
    :rtype: `rdflib.BNode`
    """
    # When pass, there is a pass outcome, when no outcome, then it is a skipped error
    if outcomes is None or len(outcomes) == 0:
        return None

    result_statement = [
        (RDF.type, EARL_NAMESPACE.TestResult)
    ] + [
        (EARL_NAMESPACE.outcome, outcome)
        for outcome in outcomes
        if not (get_outcome_type(draft.report, outcome) == "Pass" and SKIP_PASS) and
           not (get_outcome_type(draft.report, outcome) == "NotTested" and TESTED_ONLY)
    ]

    result = BNode()
    draft.reporting(result, result_statement)

    return result

def get_outcome_type(report: Graph, outcome: BNode) -> str:
    """Returns the outcome type of an outcome
    
    :param report: The graph containing the outcome
    :type report: `rdflib.Graph`

    :param outcome: The outcome that needs the outcome type extraction
    :type outcome: `rdflib.BNode`

    :return: The outcome type of the given outcome
    :rtype: `str`
    """

    outcome = report.value(outcome, EARL_NAMESPACE.outcome)
    outcomeType = report.value(outcome, RDF.type)
    earl_separator = str(EARL_NAMESPACE)[-1]
    return str(outcomeType).split(earl_separator)[-1]

def assemble_assertion(draft: AssertDraft, result: BNode) -> None:
    """Given the data stored in the draft and the result node passed as input, write an assertion in the report
    
    :param draft: The assertion draft
    :type draft: `olivaw.test.AssertDraft`

    :param result: The result Node
    :type result: `rdflib.BNode`
    """
    # if result is None, then it is a skipped error
    if result is None:
        return
    
    criterion = URIRef(draft.criterion_uri) \
                if draft.has_field("criterion_uri") else \
                OLIVAW_NAMESPACE[draft.criterion]
    
    statement = [
        (RDF.type, EARL_NAMESPACE.Assertion),
        (EARL_NAMESPACE.assertedBy, draft.assertor),
        (EARL_NAMESPACE.subject, draft.subject),
        (EARL_NAMESPACE.test, criterion),
        (EARL_NAMESPACE.result, result),
    ]

    assertion = BNode()
    draft.reporting(assertion, statement)
    draft.new_assertion()

def make_assertion(draft: AssertDraft, **kwargs) -> None:
    """Computes all the elements to make an assertion given the draft content and assemble it
    
    :param draft: The assertion draft
    :type draft: `olivaw.test.AssertDraft`

    :param **kwargs: Optional set of parameters to set to the `olivaw.test.AssertDraft` instance
    :type **kwargs: See `olivaw.test.AssertDraft` for more details
    """
    draft(**kwargs)
    assemble_assertion(
        draft,
        make_result(
            draft, 
            make_outcomes(draft)
        )
    )

def make_not_tested(draft: AssertDraft, *criterions: list[str], **kwargs) -> None:
    """Prepare assertions with outcome set as NotTested for the criterions identifiers passed as input, given the draft content

    :param draft: The test assertion draft
    :type draft: `olivaw.test.AssertDraft`

    :param criterions: the list of criterion identifiers that are needed to be reported as NotTested
    :type criterion: `list[str]`

    :param **kwargs: Optional set of parameters to set to the `olivaw.test.AssertDraft` instance
    :type **kwargs: See `olivaw.test.AssertDraft` for more details
    """

    draft(**kwargs)

    if len(criterions) > 0:
        custom_criterions = draft.custom_test_data if draft.has_field("custom_test_data") else None
        for criterion in criterions:
            make_not_tested(draft(criterion=criterion, custom_test_data=custom_criterions))
        return

    if TESTED_ONLY or should_skip(draft):
        return

    criterion_resources = CRITERION_DATA if draft.criterion in CRITERION_DATA else draft.custom_test_data
    errors = criterion_resources[draft.criterion]["errors"]

    for error in errors:
        error_node = make_outcome(draft, error=error, outcome_type="NotTested")
        assemble_assertion(draft, make_result(draft, [error_node]))
