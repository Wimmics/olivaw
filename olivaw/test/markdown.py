from rdflib import Graph, Literal
from datetime import datetime
from sys import argv

from olivaw.constants import (
    SEVERITY_RANGE,
    COLOR_BOX_TEMPLATE,
    ERROR_TABLE_HEADER,
    GET_ASSERTOR_DETAILS,
    PWD_TO_MODEL_TEST_ONTO,
    GET_CRITERION_DATA,
    GET_DETAILED_OUTCOMES,
    GET_OUTCOMES_PARTS,
    GET_OUTCOME_POINTERS,
    MODULE_URL_FORMAT,
    MODELET_URL_FORMAT,
    DATASET_URL_FORMAT,
    USECASE_URL_FORMAT,
    IS_OWL_EL_COMPATIBLE,
    IS_OWL_QL_COMPATIBLE,
    IS_OWL_RL_COMPATIBLE,
    MODE
)

def parse_outcomes(report):
    outcomes = [outcome for outcome in report.query(GET_DETAILED_OUTCOMES)]
    severities = set([str(severity[0]) for severity in SEVERITY_RANGE])
    outcomes = {
        severity: [
            outcome
            for outcome in outcomes
            if str(outcome[4]).split("#")[-1] == severity
        ]
        for severity in severities
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
    
    dataset_search = DATASET_URL_FORMAT.findall(part)
    if len(dataset_search) > 0:
        return f"[Dataset {dataset_search[0][8:]}]({part})"
    
    usecase_search = USECASE_URL_FORMAT.findall(part)
    if len(usecase_search) > 0:
        return f"[Use case {usecase_search[0][10:]}]({part})"
    
    return part

def make_details_table(
    chapter,
    outcomeInfo,
    partsDict,
    pointersDict,
    severity,
    outcome_counter,
    emoji,
    criterions
):
    _, _, _, outcome, _, subjectId, subjectTitle, criterionUri, outcomeTitle, outcomeDescription = outcomeInfo
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
        f"### {severity} Outcome number {outcome_counter}",
        "",
        f"[Jump to summary definition](#summary-{severity}-{str(outcome_counter)})",
        "",
        f"{emoji}{severity} outcome"
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

def make_severity_detail(outcomes, criterions, severity, emoji, partsDict, pointersDict):
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
            criterions
        )
    return result

def make_severity_summary(outcomes, severity, emoji):
    severity_outcomes = outcomes[severity]
    table_length = len(severity_outcomes)
    title = f"## {severity} Outcomes Summary"
    id = title_to_id(title)
    
    summary = [
        title,
        "",
        f"[Jump to statistic summary](#statistic-summary)"
        "",
        "",
        f"{emoji}{str(len(severity_outcomes))} {severity} outcomes",
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
            f"[Jump](#{severity.lower()}-outcome-number-{str(i+1)})",
            ''
        ])
        for i, (_, _, _, _, _, subjectId, _, criterionId, errorTitle, _) in enumerate(severity_outcomes)
    ] + ["", "***", ""]
    
    return summary

def make_severity_chapter(outcomes, partsDict, pointersDict, criterions, severity, emoji):
    result = []
    outcome_number = len(outcomes[severity])
    result += [
        "",
        f"# {severity} Outcomes",
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
        emoji
    ) + make_severity_detail(
        outcomes,
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

def make_stat_chapter(outcomes):
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

def make_turtle_page(report, file_name) -> str:

    md = []

    outcomes, partsDict, pointersDict = parse_outcomes(report)
    criterions = parseCriterions()

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
    
    for severity, emoji, _ in SEVERITY_RANGE:
        if len(outcomes[severity]) == 0:
            continue
        md += make_severity_chapter(
            outcomes,
            partsDict,
            pointersDict,
            criterions,
            severity,
            emoji
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
        el_compatible = [x for x in report.query(IS_OWL_EL_COMPATIBLE)][0]
        el_label = "compatible" if el_compatible else "incompatible"
        el_color = "green" if el_compatible else "red"

        ql_compatible = [x for x in report.query(IS_OWL_QL_COMPATIBLE)][0]
        ql_label = "compatible" if ql_compatible else "incompatible"
        ql_color = "red" if ql_compatible else "red"

        rl_compatible = [x for x in report.query(IS_OWL_RL_COMPATIBLE)][0]
        rl_label = "compatible" if rl_compatible else "incompatible"
        rl_color = "green" if rl_compatible else "red"

        badgesData += [
            f"EL_label\t: {el_label}",
            f"EL_color\t: {el_color}",
            f"QL_label\t: {ql_label}",
            f"QL_color\t: {ql_color}",
            f"RL_label\t: {rl_label}",
            f"RL_color\t: {rl_color}"
        ]

    if MODE == "actions":
        for badgeData in badgesData:
            print(badgeData)

    return md