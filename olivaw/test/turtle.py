from datetime import datetime
from itertools import zip_longest

from rdflib import (
    Graph,
    BNode,
    Literal,
    URIRef,
    Namespace
)

from rdflib.namespace import (
    RDF,
    RDFS,
    FOAF,
    DCTERMS,
    SDO,
    XSD
)

from olivaw.constants import (
    DEV_USERNAME,
    DEV_PROFILE,
    DOMAINS_URL,
    EARL_NAMESPACE,
    ONTOLOGY_PREFIX,
    ONTOLOGY_NAMESPACE,
    SRC_NAMESPACE,
    TEST_NAMESPACE,
    OLIVAW_EARL_NAMESPACE,
    ONTOLOGY_RDFLIB_NAMESPACE,
    ERROR_RESOURCES,
    BRANCH,
    USECASES_URL,
    SKIPPED_ERRORS,
    EXTRACT_STATEMENT,
    OLIVAW_TEST_BLOB_URI,
    BLOCKING_ERRORS,
    MODE,
    SKIP_PASS,
    TESTED_ONLY,
    CRITERION_DATA
)

from olivaw.constants.sparql import (
    ADD_DESCRIPTION_LINKS,
    GET_GRAPH_NAMESPACES,
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

from olivaw.test.util import COMMON_URI_DICT

def new_report(test_type):
    report = Graph()

    report.bind("earl", EARL_NAMESPACE)
    report.bind("", ONTOLOGY_RDFLIB_NAMESPACE)
    report.bind("src", SRC_NAMESPACE)
    report.bind("profile-test", TEST_NAMESPACE)
    report.bind("olivaw-earl", OLIVAW_EARL_NAMESPACE)
    report.bind("dcterms", DCTERMS)

    assertor = make_assertor(report, test_type)

    return report, assertor

def make_assertor(report, test_type):
    script_uri = f"{OLIVAW_TEST_BLOB_URI}/{test_type}/suite.py"
    assertorId = f"{DEV_USERNAME}-{MODE}"
    title = f"{DEV_USERNAME} using {MODE} script"
    description = f"Test triggered by @{DEV_USERNAME} by {MODE} trigger"
    
    # Define the developper and the assertor
    assert_group = BNode(assertorId)
    developper = BNode(DEV_USERNAME)

    # Define the developper
    developper_statement = [
        (developper, RDF.type, FOAF.Person),
        (developper, SDO.mainEntityOfPage, URIRef(DEV_PROFILE))
    ]

    for triple in developper_statement:
        report.add(triple)

    # Define the developper using the software
    assertor_statement = [
        (assert_group, RDF.type, FOAF.OnlineAccount),
        (assert_group, DCTERMS.title, Literal(title, lang="en")),
        (assert_group, DCTERMS.description, Literal(description, lang="en")),
        (assert_group, EARL_NAMESPACE.mainAssertor, developper),
        (assert_group, FOAF.member, URIRef(script_uri)),
        (assert_group, DCTERMS.date, Literal(datetime.now(), datatype=XSD.dateTime))
    ]

    for triple in assertor_statement:
        report.add(triple)

    return assert_group

def make_subject_id_part(fragment_list):
    modules = [item for item in fragment_list if item.startswith("src/")]
    modules = ['module-' + '.'.join(item[4:].split('.')[:-1]) for item in modules]
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

    subject_id_part = '-'.join(modules + modelets + datasets + questions + usecases)
    return subject_id_part

def make_subject_id(heart, appendix=[]):
    result = [make_subject_id_part(heart)]

    if len(appendix):
        appendix_id = make_subject_id_part(appendix)
        result.append(appendix_id)

    subject_id = "-".join(result).replace("/", "-")
    return subject_id

def make_subject(
        draft,
        heart,
        appendix=[],
        name="",
        custom_title=""
):
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
        SRC_NAMESPACE[item[4:-4]]
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

def remove_prefixes(statement, is_literal=False):
    if is_literal:
        return statement

    statement = [
        line
        for line in statement.split("\n")
        if len(line.strip()) > 0
    ]
        
    for i in range(len(statement)):
        if not statement[i].startswith("@"):
            statement = "\n".join(statement[i:])
            break
    
    return statement

def parse_statement(raw_statement):
    rdf = f"{CORESE_PREFIX_TEXT}\n{raw_statement}"
    if not rdf.strip().endswith("."):
        rdf = f"{rdf} ."
    isolated_graph = Graph()
    isolated_graph.parse(data=rdf, format="ttl")

    result = Graph()
    for triple in isolated_graph.query(SHORTEN_LITERALS):
        result.add(triple)
    return remove_prefixes(result.serialize(format="ttl"))

def extract_statement(graph, pointer):
    graph.query(ADD_DESCRIPTION_LINKS.replace("TERM", pointer))
    statement = graph.query(EXTRACT_STATEMENT.replace("TERM", pointer), format=TURTLE).strip()
    graph.query(REMOVE_DESCRIPTION_LINKS)

    if len(statement) == 0:
        statement = graph.query(GET_PREDICATE_USAGE.replace("TERM", pointer), format=TURTLE).strip()

    if len(statement) == 0:
        statement = graph.query(GET_OBJECT_USAGE.replace("TERM", pointer), format=TURTLE).strip()

    if len(statement) == 0:
        return Literal(str(pointer))
    
    namespaces = graph.query(GET_GRAPH_NAMESPACES)

    binds = []

    pointer_separator = [i for i in range(len(pointer)) if pointer[i] in ["#", "/", "="]]
    pointer_namespace = pointer[:pointer_separator[-1]+1]
    binds.append(("", Namespace(pointer_namespace)))

    for namespace in namespaces:
        namespace = namespace[1:-1] if namespace[0] == '"' else namespace
        if namespace == ONTOLOGY_NAMESPACE:
            binds.append((ONTOLOGY_PREFIX, ONTOLOGY_RDFLIB_NAMESPACE))
            continue

        if namespace in COMMON_URI_DICT:
            prefix = COMMON_URI_DICT[namespace]
            binds.append((prefix, Namespace(namespace)))
            continue

        corese_matches = [item for item in CORESE_NAMESPACES if item[1] == namespace]

        if len(corese_matches) == 0:
            continue

        corese_match = corese_matches[0]
        binds.append((corese_match[0], Namespace(corese_match[1])))

    rdflib_graph = Graph()
    rdflib_graph.parse(
        data=f"{CORESE_PREFIX_TEXT}\n{statement}",
        format="ttl"
    )
    
    for bind in binds:
        rdflib_graph.bind(*bind)

    return Literal(
        remove_prefixes(
            rdflib_graph\
                .serialize(format="ttl", encoding="utf-8")\
                .decode(encoding="utf-8")
            )
        )

def make_pointer(draft, pointer_string):
    statement_subject = pointer_string.split(" ")[0]
    is_statement = " " in pointer_string

    if statement_subject[0] == "<" and not is_statement:
        pointer = extract_statement(draft.graph, URIRef(statement_subject[1:-1]))
    elif statement_subject[0] == '"':
        pointer = Literal(remove_prefixes(pointer_string.strip()[1:-1], is_literal=True))
    elif statement_subject[0] != "[" and not is_statement:
        normalizedUri = Namespace(
            [
                namespace for prefix, namespace in draft.report.namespaces()
                if prefix == pointer_string.split(":")[0]
            ][0]
        )[pointer_string.split(":")[1]]
        pointer = URIRef(normalizedUri)
    elif pointer_string.strip()[0] == "@":
        pointer = Literal(remove_prefixes(pointer_string))
    else:
        pointer = Literal(parse_statement(pointer_string))

    return pointer

def make_outcome(draft):
    if draft.should_skip():
        return None
        
    test_name = draft.criterion.split('/')[-1].split('#')[0]
    test_name = '.'.join(test_name.split('.')[:-1])
    outcome_title = f"Test {test_name} passed" if draft.outcome_type == "Pass" else f"Error on custom test {test_name}"
    outcome_description = f"The custom test {test_name} passed" if draft.outcome_type == "Pass" else f"Error occured while running custom test {test_name}"
    
    if draft.error in ERROR_RESOURCES:
        outcome_ressources = ERROR_RESOURCES[draft.error][draft.outcome_type]
        outcome_title = outcome_ressources["title"]
        outcome_description = draft.description if (draft.has_field("description") and len(draft.description) > 0) else outcome_ressources["description"]
    
    parsed_pointers = [
        make_pointer(draft, pointer)
        for pointer in draft.pointers
        if len(pointer) > 0
    ]

    outcome_type_namespace = OLIVAW_EARL_NAMESPACE if draft.outcome_type.endswith("Fail") else EARL_NAMESPACE

    outcome_statement = [
        (RDF.type, outcome_type_namespace[draft.outcome_type]),
        (DCTERMS.title, Literal(outcome_title, lang="en")),
        (DCTERMS.description, Literal(outcome_description, lang="en"))
    ]
    outcome_statement += [(RDFS.seeAlso, pointer) for pointer in parsed_pointers]

    outcome = BNode()
    draft.reporting(outcome, outcome_statement)

    return outcome

def make_outcomes(draft):
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

def make_result(draft, outcomes):
    # When pass, there is a pass outcome, when no outcome, then it is a skipped error
    if outcomes is None or len(outcomes) == 0:
        return None

    result_statement = [
        (RDF.type, EARL_NAMESPACE.TestResult)
    ] + [
        (EARL_NAMESPACE.outcome, outcome)
        for outcome in outcomes
        if not (make_outcome_type(draft.report, outcome) == "Pass" and SKIP_PASS) and
           not (make_outcome_type(draft.report, outcome) == "NotTested" and TESTED_ONLY)
    ]

    result = BNode()
    draft.reporting(result, result_statement)

    return result

def make_outcome_type(report, result):
    outcome = report.value(result, EARL_NAMESPACE.outcome)
    outcomeType = report.value(outcome, RDF.type)
    earl_separator = str(EARL_NAMESPACE)[-1]
    return str(outcomeType).split(earl_separator)[-1]

def assemble_assertion(draft, result):
    # if result is None, then it is a skipped error
    if result is None:
        return
    
    criterion = URIRef(draft.criterion_uri) \
                if draft.has_field("criterion_uri") else \
                OLIVAW_EARL_NAMESPACE[draft.criterion]
    
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

def make_assertion(draft):
    assemble_assertion(
        draft,
        make_result(
            draft, 
            make_outcomes(draft)
        )
    )

def make_not_tested(draft, *criterions):
    if len(criterions) > 0:
        for criterion in criterions:
            make_not_tested(draft(criterion=criterion))
        return

    if TESTED_ONLY or draft.should_skip():
        return

    errors = CRITERION_DATA[draft.criterion]["errors"]

    for error in errors:
        error = make_outcome(draft(outcome_type="NotTested"))
        assemble_assertion(draft, make_result(draft, [error]))
