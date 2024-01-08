from rdflib import Graph, Literal
from datetime import datetime
from sys import argv

from .corese import smartPrint
from olivaw.constants import (
    SEVERITY_RANGE,
    COLOR_BOX_TEMPLATE,
    ERROR_TABLE_HEADER,
    GET_ASSERTOR_DETAILS,
    PWD_TO_MODEL_TEST_ONTO,
    GET_CRITERION_DATA,
    GET_DETAILED_ASSERTIONS,
    GET_ASSERTION_PARTS,
    GET_ASSERTION_POINTERS,
    MODULE_URL_FORMAT,
    MODELET_URL_FORMAT,
    IS_OWL_EL_COMPATIBLE,
    IS_OWL_QL_COMPATIBLE,
    IS_OWL_RL_COMPATIBLE
)

def parse_assertions(report):
    assertions = [assertion for assertion in report.query(GET_DETAILED_ASSERTIONS)]
    severities = set([str(severity[0]) for severity in SEVERITY_RANGE])
    assertions = {
        severity: [
            assertion
            for assertion in assertions
            if str(assertion[4]).split("#")[-1] == severity
        ]
        for severity in severities
    }

    all_parts = report.query(GET_ASSERTION_PARTS)
    subjectIds = set([str(line[0]) for line in all_parts])
    partsDict = {
        subjectId: [
            str(line[1]) for line in all_parts
            if str(line[0]) == subjectId
        ]
        for subjectId in subjectIds
    }

    all_pointers = report.query(GET_ASSERTION_POINTERS)
    outcomeIds = set([str(line[0]) for line in all_pointers])
    pointersDict = {
        outcomeId: [
            line[1] for line in all_pointers
            if str(line[0]) == outcomeId
        ]
        for outcomeId in outcomeIds
    }
    return assertions, partsDict, pointersDict

def parseCriterions():
    criterions = Graph()
    criterions.parse(PWD_TO_MODEL_TEST_ONTO)
    criterions = criterions.query(GET_CRITERION_DATA)
    criterions = {
        str(criterion[0]): {
            "title": str(criterion[1]),
            "description": str(criterion[2])
        }
        for criterion in criterions
    }
    return criterions

def title_to_id(title):
    start = 0
    while(title[start] == "#"): start += 1
    while(title[start] == " "): start += 1
    return f"#{title[start:].lower().replace(' ', '-')}"

def make_assertor_chapter(report):
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

    description = description.replace(f"@{dev}", f"[@{dev}]({page})")
    script_name = script.split("/")[-1]

    result.append(f"|Assertor|[{dev}]({page})|")
    result.append("|----|-----|")
    result.append(f"|Title|{title}|")
    result.append(f"|Description|{description}|")
    result.append(f"|Script|[{script_name}]({script})")
    result.append(f"|Date|{date}|")

    result.append("")
    result.append("***")
    result.append("")

    return result

def get_criterions_data(criterions, id):
    data = criterions.query(GET_CRITERION_DATA.replace("ID", id))
    title, description = [x for x in data][0]
    return title, description

def subject_part_to_markdown(part):
    module_search = MODULE_URL_FORMAT.findall(part)
    if len(module_search) > 0:
        return f"[Module {module_search[0][4:]}]({part})"
    
    modelet_search = MODELET_URL_FORMAT.findall(part)
    if len(modelet_search) > 0:
        return f"[Modelet {modelet_search[0][8:]}]({part})"
    
    return part

def make_details_table(
    chapter,
    assertionInfo,
    partsDict,
    pointersDict,
    severity,
    assertion_counter,
    emoji,
    criterions
):
    _, _, _, outcome, _, subjectId, subjectTitle, criterionUri, outcomeTitle, outcomeDescription = assertionInfo
    subjectId = str(subjectId)
    outcome = str(outcome)

    parts = [part for part in partsDict.get(subjectId, [])]
    parts = [part + ("" if part.endswith(".ttl") else ".ttl") for part in parts]
    parts = [subject_part_to_markdown(part) for part in parts]
    parts = "<br/>".join([f"- {part}" for part in parts])

    criterionId = criterionUri.split('#')[-1]
    criterionTitle = criterions[criterionId]["title"]
    criterionDescription = criterions[criterionId]["description"]

    chapter += [
        f"### {severity} Assertion number {assertion_counter}",
        "",
        f"[Jump to summary definition](#summary-{severity}-{str(assertion_counter)})",
        "",
        f"{emoji}{severity} assertion"
        "",
        "#### Subject detail",
        f"|Name|{subjectId}|",
        "|----|----|",
        f"|Title|{subjectTitle}|",
        f"|Composition|{parts}|",
        "",
        "#### Criterion detail",
        f"|Identifier|[{criterionId}]({criterionUri})|",
        "|----|----|",
        f"|Title|{criterionTitle}|",
        f"|Description|{criterionDescription}|",
        "",
        "#### Outcome Detail",
        f"|Type|{emoji}{severity}|",
        "|----|----|",
        f"|Title|{outcomeTitle}|",
        f"|Description|{outcomeDescription}|"
    ]

    for rdfPointer in pointersDict.get(outcome, []):
        mdPointer = str(rdfPointer).replace("\n", "&#10;").replace("&#10;&#60", " &#10; &#60")
        beforePointer = '<pre lang="Turtle"><code>' if isinstance(rdfPointer, Literal) else ""
        afterPointer = "</code></pre>" if isinstance(rdfPointer, Literal) else ""
        chapter.append(f"|Pointer|{beforePointer}{mdPointer}{afterPointer}|")

    chapter.append("")
    chapter.append("***")

def make_severity_detail(assertions, criterions, severity, emoji, partsDict, pointersDict):
    result = []
    severity_assertions = assertions[severity]

    if len(severity_assertions) == 0:
        return []

    result += [
        f"## {severity} Assertion Details",
        "",
        f"This subchapter gives more details to the {emoji}{severity} assertions",
        "",
    ]

    for i, assertionInfo in enumerate(severity_assertions):
        make_details_table(
            result,
            assertionInfo,
            partsDict,
            pointersDict,
            severity,
            i + 1,
            emoji,
            criterions
        )
    return result

def make_severity_summary(assertions, severity, emoji):
    severity_assertions = assertions[severity]
    table_length = len(severity_assertions)
    title = f"## {severity} Assertions Summary"
    id = title_to_id(title)
    
    summary = [
        title,
        "",
        f"[Jump to statistic summary](#statistic-summary)"
        "",
        "",
        f"{emoji}{str(len(severity_assertions))} {severity} assertions",
        ""
    ] + ERROR_TABLE_HEADER + [
        "|".join([
            '',
            f"[Table top]({id})",
            f'<div id="summary-{severity}-{str(i + 1)}">{str(i+1)}/{str(table_length)}</div>',
            COLOR_BOX_TEMPLATE
                .replace('EMOJI', emoji)
                .replace('TEXT', severity),
            f"`{str(subjectId)}`",
            f"[{criterionId.split('#')[-1]}]({criterionId})",
            str(errorTitle),
            f"[Jump](#{severity.lower()}-assertion-number-{str(i+1)})",
            ''
        ])
        for i, (_, _, _, _, _, subjectId, _, criterionId, errorTitle, _) in enumerate(severity_assertions)
    ] + ["", "***", ""]
    
    return summary

def make_severity_chapter(assertions, partsDict, pointersDict, criterions, severity, emoji):
    result = []
    assertion_number = len(assertions[severity])
    result += [
        "",
        f"# {severity} Assertions",
        "",
        f"Here is the chapter related to the {severity} assertion",
        "",
        f"{emoji}{assertion_number} {severity} assertions",
        "",
        "<details>",
        f"<summary>Fold/Unfold the {assertion_number} summary and details</summary>",
        ""
    ] + make_severity_summary(
        assertions,
        severity,
        emoji
    ) + make_severity_detail(
        assertions,
        criterions,
        severity,
        emoji,
        partsDict,
        pointersDict
    ) + [
        "",
        "</details>",
        "",
        "***",
        ""
    ]
    return result

def make_stat_chapter(assertions):
    assertions_stats = [len(assertions[key]) for key, _, _ in SEVERITY_RANGE]
    nb_assertions = sum(assertions_stats)

    rates = []
    for nb in assertions_stats:
        rate = nb/nb_assertions * 100 if nb_assertions > 0 else 0
        rate = int(max(1, rate)) if rate > 0 else 0
        rates.append(rate)

    rates[-1] = 100 - sum(rates[:-1])

    bar = '<div  style="border-radius: 12px; height: 25px; overflow: hidden">'
    count_line = []
    for i in range(len(SEVERITY_RANGE)):
        count_line.append(f"{SEVERITY_RANGE[i][1]}{str(assertions_stats[i])} {SEVERITY_RANGE[i][0]}")
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
        f"{str(nb_assertions)} Assertions",
        "",
        count_line,
        "",
        bar,
        "",
        "<br/>",
        "",
        "According to the [EARL](https://www.w3.org/TR/EARL10-Schema/) vocabulary, each outcome type means:",
        "* :x: Fail: The subject failed the test. ",
        "* :warning: CannotTell: It is unclear if the subject passed or failed the test. This happens when an automated test requires human judgement to make a definite decision.",
        "* :grey_question: NotTested:  The test has not been carried out. Here this is because a previous test that was mandatory to be passed did not end up as Pass.",
        "* :white_check_mark: Pass: The subject passed the test.",
        "",
        "***",
        ""
    ]

def make_turtle_page(report, file_name) -> str:

    md = []

    assertions, partsDict, pointersDict = parse_assertions(report)
    criterions = parseCriterions()

    md += [
        "# Test Report Markdown export",
        "",
        "This file is an export of the RDF test report made out of [EARL vocabulary](https://www.w3.org/TR/EARL10/)",
        "",
        "This test is powered by Corese, check the [website](https://project.inria.fr/corese/) and the [repository](https://github.com/Wimmics/corese)",
        "",
        f"The original test report is available in turtle syntax [here](./{file_name}.ttl).",
        ""
    ]
    md += make_assertor_chapter(report)
    md += make_stat_chapter(assertions)
    
    for severity, emoji, _ in SEVERITY_RANGE:
        if len(assertions[severity]) == 0:
            continue
        md += make_severity_chapter(
            assertions,
            partsDict,
            pointersDict,
            criterions,
            severity,
            emoji
        )

    md = "\n".join(md)

    el_compatible = [x for x in report.query(IS_OWL_EL_COMPATIBLE)][0]
    el_label = "compatible" if el_compatible else "incompatible"
    el_color = "green" if el_compatible else "red"

    ql_compatible = [x for x in report.query(IS_OWL_QL_COMPATIBLE)][0]
    ql_label = "compatible" if ql_compatible else "incompatible"
    ql_color = "red" if ql_compatible else "red"

    rl_compatible = [x for x in report.query(IS_OWL_RL_COMPATIBLE)][0]
    rl_label = "compatible" if rl_compatible else "incompatible"
    rl_color = "green" if rl_compatible else "red"

    badgesData = [
        f"Pass\t\t: {len(assertions['Pass'])}",
        f"NotTested\t: {len(assertions['NotTested'])}",
        f"CannotTell\t: {len(assertions['CannotTell'])}",
        f"MinorFail\t: {len(assertions['MinorFail'])}",
        f"MajorFail\t: {len(assertions['MajorFail'])}",
        f"EL_label\t: {el_label}",
        f"EL_color\t: {el_color}",
        f"QL_label\t: {ql_label}",
        f"QL_color\t: {ql_color}",
        f"RL_label\t: {rl_label}",
        f"RL_color\t: {rl_color}"
    ]
    if "--is-action" in argv:
        for badgeData in badgesData:
            print(badgeData)

    return md