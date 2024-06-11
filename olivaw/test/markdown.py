"""Module providing functions for markdown report format generation"""

from typing import Union
from rdflib import BNode, Graph, Literal, URIRef
from datetime import datetime
from sys import argv

from os.path import sep

from olivaw.constants import (
    SEVERITY_RANGE,
    ERROR_TABLE_HEADER,
    GET_ASSERTOR_DETAILS,
    GET_DETAILED_OUTCOMES,
    GET_OUTCOMES_PARTS,
    GET_OUTCOME_POINTERS,
    IS_OWL_EL_COMPATIBLE,
    IS_OWL_QL_COMPATIBLE,
    IS_OWL_RL_COMPATIBLE,
    MODE,
    OLIVAW_REF,
    PWD_TO_ROOT_FOLDER,
    CRITERION_DATA,
    DATASET_URL_FORMAT,
    MODELET_URL_FORMAT,
    MODULE_URL_FORMAT,
    NEW_BR,
    QUESTION_URL_FORMAT,
    USECASE_URL_FORMAT
)

from olivaw.olivaw.constants.regex import MULTIPLE_HTML_CHARS
from olivaw.test.generic.shacl import get_criterion_data

def html_special_chars(text: str) -> str:
    """Parse the characters from string that need to be converted into HTML special chars
    
    :param text: The unparsed text
    :type text: `str`

    :returns: The parsed text
    :rtype: `str`
    """
    result =  NEW_BR.sub(
        " &#10;",
        " &#10;".join([
            line\
                .replace("<", "&#60;")\
                .replace("_", "&lowbar;")\
                .replace("^", "&Hat;")\
                .replace(" ", "&#32;")\
                .replace("\t", "&#32;&#32;&#32;&#32;")\
                .replace("\\", "&#92;")\
                .replace('"', "&#34;")\
                .replace("[", "&#91;")
            for line in text.split("\n")
            if len(line.strip()) > 0
        ])
    )

    for char_1, char_2 in MULTIPLE_HTML_CHARS.findall(result):
        result = result.replace(f"{char_1}{char_2}", f"{char_1} {char_2}")

    return result

def profile_badge_data(report: Graph, request: str) -> tuple[str, str]:
    """Given the report and an ontology profile compatibility request, returns the proper label and colors of its related badge
    
    :param report: test report
    :type report: `rdflib.Graph`

    :param request: Request that retrieve the profile compatibility of the ontology in the report
    :type request: `str`

    :returns: The related badge label and message
    :rtype: `tuple[str, str]`
    """
    profile_statuses = [str(x[0]) for x in report.query(request)]

    if len(profile_statuses) == 0:
        return "undetermined", "grey"
    
    no_pass = [status for status in profile_statuses if status != "Pass"]

    if len(no_pass) == 0:
        return "compatible", "green"
    
    is_fail = [status for status in no_pass if "Fail" in status]

    if len(is_fail) > 0:
        return "incompatible", "red"
    
    return "undetermined", "grey"

def parse_outcomes(report: Graph) -> tuple[
    dict[ # dictionary of the outcomes information
        str, # Severity name
        tuple[
            BNode, # Assertion
            BNode, # Subject
            BNode, # Result
            BNode, # Outcome
            Literal, # Outcome type
            Literal, # Subject identifier
            Literal, # Subject title
            Literal, # Criterion identifier
            Literal, # Outcome title
            Literal, # Outcome description
            Literal # Outcome identifier
        ]
    ],
    dict[ # dictionary of the the related subject parts
        str, # Subject Identifier
        list[str] # List of file URIs
    ],
    dict[ # dictionary of the related pointers
        str, # Outcome
        list[Union[URIRef, Literal]] # List of pointers (URIs or code snippets)
    ]
]:
    """Retrieves all the outcomes information from the report

    :param report: The report graph
    :type report: `rdflib.Graph`

    :returns: A dictionary of the outcomes information, a dictionary of the the related subject parts and a dictionary of the related pointers
    :rtype:
    
    ```
    tuple[
        dict[ # dictionary of the outcomes information
            str, # Severity name
            tuple[
                BNode, # Assertion
                BNode, # Subject
                BNode, # Result
                BNode, # Outcome
                Literal, # Outcome type
                Literal, # Subject identifier
                Literal, # Subject title
                Literal, # Criterion identifier
                Literal, # Outcome title
                Literal, # Outcome description
                Literal # Outcome identifier
            ]
        ],
        dict[ # dictionary of the the related subject parts
            str, # Subject Identifier
            list[str] # List of file URIs
        ],
        dict[ # dictionary of the related pointers
            str, # Outcome
            list[Union[URIRef, Literal]] # List of pointers (URIs or code snippets)
        ]
    ]
    ```
    """
    outcomes = [outcome for outcome in report.query(GET_DETAILED_OUTCOMES)]
    found_severities = list(set([str(severity[0]) for severity in SEVERITY_RANGE]))
    severities = [severity[0] for severity in SEVERITY_RANGE if severity[0] in found_severities]
    outcomes = {
        severity: [
            outcome
            for outcome in outcomes
            if str(outcome[4]).split("#")[-1] == severity
        ]
        for severity in severities
    }

    outcomes = {
        severity: [
            (*outcome, j + sum([len(outcomes[severities[k]]) for k in range(i)]), len(outcomes[severity]), j)
            for j, outcome in enumerate(outcomes[severity])
        ]
        for i, severity in enumerate(severities)
    }

    all_parts = report.query(GET_OUTCOMES_PARTS)
    subjectIds = set([str(line[0]) for line in all_parts])
    partsDict = {
        subjectId: [
            str(line[1]) for line in all_parts
            if str(line[0]) == subjectId
        ]
        for subjectId in subjectIds
    }

    all_pointers = report.query(GET_OUTCOME_POINTERS)
    outcomeIds = set([str(line[0]) for line in all_pointers])
    pointersDict = {
        outcomeId: [
            line[1] for line in all_pointers
            if str(line[0]) == outcomeId
        ]
        for outcomeId in outcomeIds
    }
    return outcomes, partsDict, pointersDict

def title_to_id(title: str) -> str:
    """Converts a markdown title to its related CSS id

    :param title: The title line
    :type title: `str`

    :returns: The CSS id
    :rtype: `id`
    """
    start = 0
    while(title[start] == "#"): start += 1
    while(title[start] == " "): start += 1
    return f"#{title[start:].lower().replace(' ', '-')}"

def make_assertor_chapter(report: Graph) -> list[str]:
    """Generates the assertor chapter of the report
    
    :param report: The report graph
    :type graph: `rdflib.Graph`

    :returns: A list of markdown lines containing the assertor chapter
    :rtype: `list[str]`
    """
    result = []

    result.append("# Test Context")
    result.append("")
    result.append("Here is some context about under which context this test was made")
    result.append("")

    assertor_info = report.query(GET_ASSERTOR_DETAILS)
    assertor_info = [x for x in assertor_info][0]

    title, description, date, script, page = assertor_info

    date = datetime.fromisoformat(str(date)).strftime("%Y-%m-%d %H:%M:%S")
    dev = page.split('/')[-1]

    description = html_special_chars(description).replace(f"@{dev}", f"[@{dev}]({page})")
    script_name = script.split("/")[-2]

    result.append(f"|Assertor|[{dev}]({page})|")
    result.append("|----|-----|")
    result.append(f"|Title|{html_special_chars(title)}|")
    result.append(f"|Description|{description}|")
    result.append(f"|Script|[{script_name} test suite]({script})")
    result.append(f"|Date|{date}|")

    result.append("")
    result.append("***")
    result.append("")

    return result

def subject_part_to_markdown(part: str) -> str:
    """Generates a markdown link for a subject part file URI

    :param part: the subject part file URI
    :type part: `str`

    :returns: The markdown link
    :rtype: `str`
    """
    module_search = MODULE_URL_FORMAT.findall(part)
    if len(module_search) > 0:
        return f"[Module {html_special_chars(module_search[0][0][:-4])}]({part})"
    
    modelet_search = MODELET_URL_FORMAT.findall(part)
    if len(modelet_search) > 0:
        return f"[Modelet {html_special_chars(modelet_search[0][8:-9])}]({part})"
    
    dataset_search = DATASET_URL_FORMAT.findall(part)
    if len(dataset_search) > 0:
        return f"[Dataset {html_special_chars(dataset_search[0][8:-12])}]({part})"
    
    usecase_search = USECASE_URL_FORMAT.findall(part)
    if len(usecase_search) > 0:
        return f"[Use case {html_special_chars(usecase_search[0][10:][:-4])}]({part})"
    
    question_search = QUESTION_URL_FORMAT.findall(part)
    if len(question_search) > 0:
        return f"[Competency question {html_special_chars(question_search[0][8:-3])}]({part})"
    
    return part

def criterion_uri_to_file(uri: str) -> str:
    """Provides the local file path related to a custom test criterion URI
    
    :param uri: The custom test criterion URI
    :type uri: `str`

    :returns: The path to the locaw file that defines the custom test criterion
    :rtype: `str`
    """
    return f"{PWD_TO_ROOT_FOLDER}{sep.join(uri.split('#')[0].split('/')[-4:])}"

def get_criterion_details(
        uri: str,
        shape_data:
            dict[ # Dictionary about custom tests data
                str, # Custom test identifier
                dict[ # Information about a given custom test
                    str, # One of title / description / errors
                    Union[str, list[str]] # Useful data
                ]
            ]={}
    ) -> tuple[ # Criterion data
        str, # URI
        str, # Identifier
        str, # Title
        str # Description
    ]:
    """Retrieves the useful information about the given criterion URI

    :param uri: URI of the criterion that is searched for
    :type uri: `str`

    :param shape_data: dictionary providing information about eventual custom tests, defaults to `{}`
    :type shape_data: optional:\n
    
    ```
    dict[ # Dictionary about custom tests data
        str, # Custom test identifier
        dict[ # Information about a given custom test
            str, # One of title / description / errors
            Union[str, list[str]] # Useful data
        ]
    ]
    ```

    :returns: The criterion URI, identifier, title and description
    :rtype: `tuple[str, str, str, str]`
    
    """
    criterion_path = uri.split("#")[0].split("/")
    criterion_ref = "/".join(criterion_path[3:5])

    criterion_id = None
    criterion_title = None
    criterion_description = None

    if criterion_ref == OLIVAW_REF:
        criterion_id = uri.split('#')[-1]
        criterion_resource = CRITERION_DATA if criterion_id in CRITERION_DATA else shape_data
        criterion_title = criterion_resource[criterion_id]["title"]
        criterion_description = criterion_resource[criterion_id]["description"]
        return uri, criterion_id, criterion_title, criterion_description
    else:
        criterion_file = criterion_uri_to_file(uri)
        return get_criterion_data(criterion_file)

def make_details_table(
    chapter: list[str],
    outcome_info: tuple[
        BNode, # Assertion
        BNode, # Subject
        BNode, # Result
        BNode, # Outcome
        Literal, # Outcome type
        Literal, # Subject identifier
        Literal, # Subject title
        Literal, # Criterion identifier
        Literal, # Outcome title
        Literal, # Outcome description
        Literal # Outcome identifier
    ],
    partsDict: dict[ # dictionary of the the related subject parts
        str, # Subject Identifier
        list[str] # List of file URIs
    ],
    pointersDict: dict[ # dictionary of the related pointers
        str, # Outcome
        list[Union[URIRef, Literal]] # List of pointers (URIs or code snippets)
    ],
    severity: str,
    outcome_counter: int,
    emoji: str,
    shape_data: dict[ # Dictionary about custom tests data
                str, # Custom test identifier
                dict[ # Information about a given custom test
                    str, # One of title / description / errors
                    Union[str, list[str]] # Useful data
                ]
    ]={}
) -> None:
    """Generates the section related to a particular outcome detail

    :param chapter: list of the lines containing the current chapter
    :type chapter: `list[str]`

    :param outcome_info: tuple containing the useful information related to the outcome to detail
    :type outcome_info:
    
    ```
    tuple[
        BNode, # Assertion
        BNode, # Subject
        BNode, # Result
        BNode, # Outcome
        Literal, # Outcome type
        Literal, # Subject identifier
        Literal, # Subject title
        Literal, # Criterion identifier
        Literal, # Outcome title
        Literal, # Outcome description
        Literal # Outcome identifier
    ]
    ```

    :param partsDict: dictionary of all the subject parts
    :type partsDict:
    
    ```
    dict[ # dictionary of the related pointers
        str, # Outcome
        list[Union[URIRef, Literal]] # List of pointers (URIs or code snippets)
    ]
    ```

    :param pointersDict: dictionary of the related pointers
    :type pointersDict: 
    
    ```
    dict[ # dictionary of the related pointers
        str, # Outcome
        list[Union[URIRef, Literal]] # List of pointers (URIs or code snippets)
    ]
    ```

    :param severity: severity of the outcome to detail
    :type severity: `str`

    :param outcome_number: Outcome number i that severity
    :type outcome_number: `int`

    :param emoji: text for the emoji related to the outcome severity
    :type emoji: `str`

    :param shape_data: dictionary storing information about eventual custom tests
    :type shape_data: optional:\n
    
    ```
    dict[ # Dictionary about custom tests data
        str, # Custom test identifier
        dict[ # Information about a given custom test
            str, # One of title / description / errors
            Union[str, list[str]] # Useful data
        ]
    ]
    ```
    """
    _, _, _, outcome, _, subject_id, subject_title, criterion_uri, outcome_title, outcome_description, outcome_id, outcome_number, severity_list_size, severity_index = outcome_info
    subject_id = str(subject_id)
    outcome = str(outcome)

    parts = [part for part in partsDict.get(subject_id, [])]
    parts = [part + ("" if part.endswith(".ttl") else ".ttl") for part in parts]
    parts = [subject_part_to_markdown(part) for part in parts]
    parts = "<br/>".join([f"- {part}" for part in parts])

    _, criterion_id, criterion_title, criterion_description = get_criterion_details(criterion_uri, shape_data=shape_data)

    table_top = f"#{severity.lower()}-outcome-number-{outcome_counter}"

    chapter += [
        f"### {severity} Outcome number {outcome_counter}",
        "",
        f"[Jump to summary definition](#summary-{severity}-{str(outcome_counter)})" + \
            (f"\t|\tPrevious {severity} outcome" if severity_index == 0 else f"\t|\t[Previous {severity} outcome](#{severity.lower()}-outcome-number-{str(severity_index)})") + \
            (f"\t|\tNext {severity} outcome" if severity_index == severity_list_size - 1 else f"\t|\t[Next {severity} outcome](#{severity.lower()}-outcome-number-{str(severity_index + 2)})"),
        "",
        f"{emoji}{severity} outcome"
        "",
        "#### Subject detail",
        f"|Name|{subject_id}|",
        "|----|----|",
        f"|Title|{html_special_chars(subject_title)}|",
        f"|Composition|{parts}|",
        "",
        "#### Criterion detail",
        f"|Identifier|[{criterion_id}]({criterion_uri})|",
        "|----|----|",
        f"|Title|{html_special_chars(criterion_title)}|",
        f"|Description|{html_special_chars(criterion_description)}|",
        "",
        "#### Outcome Detail",
        f"|Jump|Type|{emoji}{severity}|",
        "|----|----|----|",
        f"|[Section top]({table_top})|Identifier|`{outcome_id}`|",
        f"|[Section top]({table_top})|Title|{html_special_chars(outcome_title)}|",
        f"|[Section top]({table_top})|Description|{html_special_chars(outcome_description)}|"
    ]

    for rdfPointer in pointersDict.get(outcome, []):
        mdPointer = html_special_chars(str(rdfPointer))
        beforePointer = '<pre lang="Turtle"><code>' if isinstance(rdfPointer, Literal) else ""
        afterPointer = "</code></pre>" if isinstance(rdfPointer, Literal) else ""
        chapter.append(f"|[Section top]({table_top})|Pointer|{beforePointer}{mdPointer}{afterPointer}|")

    chapter.append("")
    chapter.append("***")

def make_severity_detail(
        outcomes: list[ # List of the outcomes information related to the severity
            tuple[
                BNode, # Assertion
                BNode, # Subject
                BNode, # Result
                BNode, # Outcome
                Literal, # Outcome type
                Literal, # Subject identifier
                Literal, # Subject title
                Literal, # Criterion identifier
                Literal, # Outcome title
                Literal, # Outcome description
                Literal # Outcome identifier
            ]
        ],
        severity: str,
        emoji: str,
        partsDict: dict[ # dictionary of the the related subject parts
            str, # Subject Identifier
            list[str] # List of file URIs
        ],
        pointersDict: dict[ # dictionary of the related pointers
            str, # Outcome
            list[Union[URIRef, Literal]] # List of pointers (URIs or code snippets)
        ],
        shape_data: dict[ # Dictionary about custom tests data
            str, # Custom test identifier
            dict[ # Information about a given custom test
                str, # One of title / description / errors
                Union[str, list[str]] # Useful data
            ]
        ]={}
    ) -> list[str]:
    """Generate the outcome details section ofr all the outcomes of that severity

    :param outcomes: The list of the outcomes of that section
    :type outcomes:
    
    ```
    list[ # List of the outcomes information related to the severity
        tuple[
            BNode, # Assertion
            BNode, # Subject
            BNode, # Result
            BNode, # Outcome
            Literal, # Outcome type
            Literal, # Subject identifier
            Literal, # Subject title
            Literal, # Criterion identifier
            Literal, # Outcome title
            Literal, # Outcome description
            Literal # Outcome identifier
        ]
    ]
    ```

    :param severity: The severity of all the outcomes from the list
    :type severity: `str`

    :param emoji: The emoji associated to the severity of that chapter
    :type emoji: `str`

    :param partsDict: dictionary of all the subject parts
    :type partsDict:
    
    ```
    dict[ # dictionary of the related pointers
        str, # Outcome
        list[Union[URIRef, Literal]] # List of pointers (URIs or code snippets)
    ]
    ```

    :param pointersDict: dictionary of the related pointers
    :type pointersDict:
    
    ```
    dict[ # dictionary of the related pointers
        str, # Outcome
        list[Union[URIRef, Literal]] # List of pointers (URIs or code snippets)
    ]
    ```

    :param shape_data: dictionary storing information about eventual custom tests
    :type shape_data: optional: \n
    
    ```
    dict[ # Dictionary about custom tests data
        str, # Custom test identifier
        dict[ # Information about a given custom test
            str, # One of title / description / errors
            Union[str, list[str]] # Useful data
        ]
    ]
    ```

    :returns: The generated markdown as list of lines
    :rtype: `list[str]`
    """
    result = []
    severity_outcomes = outcomes[severity]

    if len(severity_outcomes) == 0:
        return []

    result += [
        f"## {severity} Outcomes Details",
        "",
        f"This subchapter gives more details to the {emoji}{severity} outcomes",
        "",
    ]

    for i, outcomeInfo in enumerate(severity_outcomes):
        make_details_table(
            result,
            outcomeInfo,
            partsDict,
            pointersDict,
            severity,
            i + 1,
            emoji,
            shape_data=shape_data
        )
    return result

def make_severity_summary(
        outcomes: list[ # List of the outcomes information related to the severity
            tuple[
                BNode, # Assertion
                BNode, # Subject
                BNode, # Result
                BNode, # Outcome
                Literal, # Outcome type
                Literal, # Subject identifier
                Literal, # Subject title
                Literal, # Criterion identifier
                Literal, # Outcome title
                Literal, # Outcome description
                Literal # Outcome identifier
            ]
        ],
        severity: str,
        emoji: str,
        shape_data: dict[ # Dictionary about custom tests data
            str, # Custom test identifier
            dict[ # Information about a given custom test
                str, # One of title / description / errors
                Union[str, list[str]] # Useful data
            ]
        ]={}
    ) -> list[str]:
    """For a given severity chapter, generates the summary table
    
    :param outcomes: The list of the outcomes of that section
    :type outcomes:
    
    ```
    list[ # List of the outcomes information related to the severity
        tuple[
            BNode, # Assertion
            BNode, # Subject
            BNode, # Result
            BNode, # Outcome
            Literal, # Outcome type
            Literal, # Subject identifier
            Literal, # Subject title
            Literal, # Criterion identifier
            Literal, # Outcome title
            Literal, # Outcome description
            Literal # Outcome identifier
        ]
    ]
    ```

    :param severity: The severity of all the outcomes from the list
    :type severity: `str`

    :param emoji: The emoji associated to the severity of that chapter
    :type emoji: `str`

    :param shape_data: dictionary storing information about eventual custom tests
    :type shape_data: optional: \n
    
    ```
    dict[ # Dictionary about custom tests data
        str, # Custom test identifier
        dict[ # Information about a given custom test
            str, # One of title / description / errors
            Union[str, list[str]] # Useful data
        ]
    ]
    ```

    :returns: The generated markdown section, as list of lines
    :rtype: `list[str]`
    """
    severity_outcomes = outcomes[severity]
    table_length = len(severity_outcomes)
    title = f"## {severity} Outcomes Summary"
    id = f"#{severity.lower()}-outcomes"
    
    summary = [
        title,
        "",
        f"{emoji}{str(len(severity_outcomes))} {severity} outcomes",
        ""
    ] + ERROR_TABLE_HEADER + [
        "|".join([
            '',
            f"[Chapter top]({id})",
            f'<div id="summary-{severity}-{str(i + 1)}">{str(i+1)}/{str(table_length)}</div>',
            f"{emoji}{severity}",
            f"`{str(subjectId)}`",
            f"[{html_special_chars(get_criterion_details(criterionId, shape_data=shape_data)[1])}]({criterionId})",
            str(errorTitle),
            f"[Jump](#{severity.lower()}-outcome-number-{str(i+1)})",
            ''
        ])
        for i, (_, _, _, _, _, subjectId, _, criterionId, errorTitle, *_) in enumerate(severity_outcomes)
    ] + ["", "***", ""]
    
    return summary

def make_severity_chapter(
        outcomes: list[ # List of the outcomes information related to the severity
            tuple[
                BNode, # Assertion
                BNode, # Subject
                BNode, # Result
                BNode, # Outcome
                Literal, # Outcome type
                Literal, # Subject identifier
                Literal, # Subject title
                Literal, # Criterion identifier
                Literal, # Outcome title
                Literal, # Outcome description
                Literal # Outcome identifier
            ]
        ],
        partsDict: dict[ # dictionary of the the related subject parts
            str, # Subject Identifier
            list[str] # List of file URIs
        ],
        pointersDict: dict[ # dictionary of the related pointers
            str, # Outcome
            list[Union[URIRef, Literal]] # List of pointers (URIs or code snippets)
        ],
        severity: str,
        emoji: str,
        shape_data: dict[ # Dictionary about custom tests data
            str, # Custom test identifier
            dict[ # Information about a given custom test
                str, # One of title / description / errors
                Union[str, list[str]] # Useful data
            ]
        ]={},
        previous_severity: str=None,
        next_severity: str=None
    ) -> list[str]:
    """Generates all the markdown sections related to a given outcome severity

    :param outcomes: The list of the outcomes of that section
    :type outcomes:
    
    ```
    list[ # List of the outcomes information related to the severity
        tuple[
            BNode, # Assertion
            BNode, # Subject
            BNode, # Result
            BNode, # Outcome
            Literal, # Outcome type
            Literal, # Subject identifier
            Literal, # Subject title
            Literal, # Criterion identifier
            Literal, # Outcome title
            Literal, # Outcome description
            Literal # Outcome identifier
        ]
    ]
    ```

    :param partsDict: dictionary of all the subject parts
    :type partsDict:
    
    ```
    dict[ # dictionary of the related pointers
        str, # Outcome
        list[Union[URIRef, Literal]] # List of pointers (URIs or code snippets)
    ]
    ```

    :param pointersDict: dictionary of the related pointers
    :type pointersDict:
    
    ```
    dict[ # dictionary of the related pointers
        str, # Outcome
        list[Union[URIRef, Literal]] # List of pointers (URIs or code snippets)
    ]
    ```

    :param severity: The severity of all the outcomes from the list
    :type severity: `str`

    :param emoji: The emoji associated to the severity of that chapter
    :type emoji: `str`

    :param shape_data: dictionary storing information about eventual custom tests
    :type shape_data: optional \n
    
    ```
    dict[ # Dictionary about custom tests data
        str, # Custom test identifier
        dict[ # Information about a given custom test
            str, # One of title / description / errors
            Union[str, list[str]] # Useful data
        ]
    ]
    ```

    :param previous_severity: The severity of the previous severity chapter
    :type previous_severity: `str`

    :param next_severity: The severity of the previous severity chapter
    :type next_severity: `str`

    :returns: The markdown content as list of lines
    :rtype: `list[str]`
    """
    result = []
    outcome_number = len(outcomes[severity])
    result += [
        "",
        f"# {severity} Outcomes",
        "",
        "\t|\t".join([
            link for link in [
                f"[Jump to statistic summary](#statistic-summary)",
                ("Previous section" if previous_severity is None else f"[Previous section](#{previous_severity.lower()}-outcomes)"),
                ("Next section" if next_severity is None else f"[Next section](#{next_severity.lower()}-outcomes)")
            ]
            if not link == ""
        ]),
        "",
        f"Here is the chapter related to the {severity} outcome",
        "",
        f"{emoji}{outcome_number} {severity} outcomes",
        "",
        "<details>",
        f"<summary>Fold/Unfold the {outcome_number} summary and details</summary>",
        ""
    ] + make_severity_summary(
        outcomes,
        severity,
        emoji,
        shape_data=shape_data
    ) + make_severity_detail(
        outcomes,
        severity,
        emoji,
        partsDict,
        pointersDict,
        shape_data=shape_data
    ) + [
        "",
        "</details>",
        "",
        "***",
        ""
    ]
    return result

def make_stat_chapter(outcomes: dict [ # Dictionary linking a severity to its related outcomes
        list[ # List of the outcomes information related to the severity
            tuple[
                BNode, # Assertion
                BNode, # Subject
                BNode, # Result
                BNode, # Outcome
                Literal, # Outcome type
                Literal, # Subject identifier
                Literal, # Subject title
                Literal, # Criterion identifier
                Literal, # Outcome title
                Literal, # Outcome description
                Literal # Outcome identifier
            ]
        ]
    ]) -> list[str]:
    """Generates the statistic summary markdown chapter

    :param outcomes: A dictionary storing information about all the report outcomes
    :type outcomes:
    
    ```
    dict [ # Dictionary linking a severity to its related outcomes
        list[ # List of the outcomes information related to the severity
            tuple[
                BNode, # Assertion
                BNode, # Subject
                BNode, # Result
                BNode, # Outcome
                Literal, # Outcome type
                Literal, # Subject identifier
                Literal, # Subject title
                Literal, # Criterion identifier
                Literal, # Outcome title
                Literal, # Outcome description
                Literal # Outcome identifier
            ]
        ]
    ]
    ```

    :returns: The statistic summary markdown section, as a list of lines
    :rtype: `list[str]`
    """
    outcomes_stats = [len(outcomes[key]) for key, _, _ in SEVERITY_RANGE]
    nb_outcomes = sum(outcomes_stats)

    rates = []
    for nb in outcomes_stats:
        rate = nb/nb_outcomes * 100 if nb_outcomes > 0 else 0
        rate = int(max(1, rate)) if rate > 0 else 0
        rates.append(rate)

    rates[-1] = 100 - sum(rates[:-1])

    bar = '<div  style="border-radius: 12px; height: 25px; overflow: hidden">'
    count_line = []
    for i in range(len(SEVERITY_RANGE)):
        count_line.append(f"{SEVERITY_RANGE[i][1]}{str(outcomes_stats[i])} {SEVERITY_RANGE[i][0]}")
        color = SEVERITY_RANGE[i][2]
        bar += f'<img src="../assets/{color}.png" width="{rates[i]}%" height="25px"/>'
    bar +='</div>'
    count_line = ", ".join(count_line)

    return [
        "",
        "# Statistic summary",
        "",
        "Here is a short overview for this test report",
        "",
        f"{str(nb_outcomes)} Outcomes",
        "",
        count_line,
        "",
        bar,
        "",
        "<br/>",
        "",
        "The different status types are an extension of the [EARL](https://www.w3.org/TR/EARL10-Schema/) vocabulary where the nextended terms can be found in the [olivaw-earl dataset](https://github.com/Wimmics/olivaw/blob/main/olivaw/test/olivaw-earl.ttl), each outcome type means:",
        "* :boom: MajorFail: This is an error that is critical and consider as blocking for production",
        "* :exclamation: MinorFail: This is an error that should be fixed, but it is cannot be considered as critical error",
        "* :warning: CannotTell: It is unclear if the subject passed or failed the test. This happens when an automated test requires human judgement to make a definite decision.",
        "* :grey_question: NotTested:  The test has not been carried out. Here this is because a previous test that was mandatory to be passed did not end up as Pass.",
        "* :white_check_mark: Pass: The subject passed the test.",
        "",
        "***",
        ""
    ]

def markdown_export(
        report: Graph,
        file_name: str,
        shape_data: dict[ # Dictionary about custom tests data
            str, # Custom test identifier
            dict[ # Information about a given custom test
                str, # One of title / description / errors
                Union[str, list[str]] # Useful data
            ]
        ]={}
    ) -> str:
    """Generates the markdown report format out of the turtle report format

    :param report: The turtle report
    :type report: `rdflib.Graph`

    :param file_name: The expected file name
    :type file_name: `str`

    :param shape_data: dictionary storing information about eventual custom tests
    :type shape_data: optional \n
    
    ```
    dict[ # Dictionary about custom tests data
        str, # Custom test identifier
        dict[ # Information about a given custom test
            str, # One of title / description / errors
            Union[str, list[str]] # Useful data
        ]
    ]
    ```

    :returns: A string containing the markdown report format
    :rtype: `str`
    
    """
    md = []

    outcomes, partsDict, pointersDict = parse_outcomes(report)

    md += [
        "# Test Report Markdown Export",
        "",
        "This file is an export of the RDF test report made out of [EARL vocabulary](https://www.w3.org/TR/EARL10/)",
        "",
        "This test is powered by Corese, check the [website](https://project.inria.fr/corese/) and the [repository](https://github.com/Wimmics/corese)",
        "",
        f"The original test report is available in turtle syntax [here](./{file_name}.ttl).",
        ""
    ]
    md += make_assertor_chapter(report)
    md += make_stat_chapter(outcomes)

    report_severities = [
        (severity, emoji)
        for severity, emoji, _
        in SEVERITY_RANGE
        if len(outcomes[severity]) > 0
    ]
    
    for i, (severity, emoji) in enumerate(report_severities):
        md += make_severity_chapter(
            outcomes,
            partsDict,
            pointersDict,
            severity,
            emoji,
            shape_data=shape_data,
            previous_severity=None if i == 0 else report_severities[i - 1][0],
            next_severity=None if i == len(report_severities) - 1 else report_severities[i + 1][0]
        )

    md = "\n".join(md)

    badgesData = [
        f"Pass\t\t: {len(outcomes['Pass'])}",
        f"NotTested\t: {len(outcomes['NotTested'])}",
        f"CannotTell\t: {len(outcomes['CannotTell'])}",
        f"MinorFail\t: {len(outcomes['MinorFail'])}",
        f"MajorFail\t: {len(outcomes['MajorFail'])}"
    ]

    if "model" in argv:
        el_label, el_color = profile_badge_data(report, IS_OWL_EL_COMPATIBLE)
        ql_label, ql_color = profile_badge_data(report, IS_OWL_QL_COMPATIBLE)
        rl_label, rl_color = profile_badge_data(report, IS_OWL_RL_COMPATIBLE)

        badgesData += [
            f"EL_label\t: {el_label}",
            f"EL_color\t: {el_color}",
            f"QL_label\t: {ql_label}",
            f"QL_color\t: {ql_color}",
            f"RL_label\t: {rl_label}",
            f"RL_color\t: {rl_color}"
        ]

    if MODE == "ACTIONS":
        for badgeData in badgesData:
            print(badgeData)

    return md