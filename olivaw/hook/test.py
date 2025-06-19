#!/usr/bin/env python
"""Module providing the reusable pre-commit hook"""

from typing import Sequence
from pre_commit import output
from rdflib import Graph
from os.path import sep, relpath, exists, abspath

from olivaw.test.corese import export_graph

from olivaw.test.query.testing import question_tests
from olivaw.test.turtle import new_report
from olivaw.test.model.testing import (
    modules_tests,
    modelets_tests,
    shape_tests as model_shape_tests
)

from olivaw.test.data.testing import (
    data_tests,
    shape_tests as data_shape_tests
)

from olivaw.constants import (
    PWD_TO_ROOT_FOLDER,
    GET_MAJOR_FAILS,
    OLIVAW_ONTOLOGY,
    PWD_TO_OLIVAW_ONTOLOGY,
    GET_CRITERION_SUMMARY,
    TESTED_MODULES,
    TESTED_MODELETS,
    TESTED_DATASETS,
    TESTED_USE_CASES,
    TESTED_QUERIES
)

sorted_files = {
    "model": {
        modules_tests: [],
        modelets_tests: []
    },
    "data": {
        data_tests: []
    },
    "query": {
        question_tests: []
    }
}

olivaw_earl_graph = Graph()
olivaw_earl_graph.parse(PWD_TO_OLIVAW_ONTOLOGY)

custom_tests_base = [export_graph(graph) for graph in model_shape_tests] + [export_graph(graph) for graph in data_shape_tests]
custom_tests_base = "\n".join(custom_tests_base)
custom_tests = Graph()
custom_tests.parse(data=custom_tests_base, format="ttl")

def main(files: Sequence[str] | None = None) -> int:
    """Function embedding the business logic behind a pre-commit worker
    
    :param files: List of options sent to the pre-commit worker through the command line, defaults to `None`
    :type files: `list[str] | None`, optional

    :return: The error code that will return the pre-commit worker
    :rtype: `int`
    """
    if files is None:
        return 0

    abspaths = [abspath(file) for file in files]

    if len(files) == 0:
        return 0
    
    sorted_files["model"][modules_tests] = [
        item
        for item in TESTED_MODULES
        if item["file"] in abspaths
    ]

    sorted_files["model"][modelets_tests] = [
        item
        for item in TESTED_MODELETS
        if item["file"] in abspaths
    ]

    sorted_files["data"][data_tests] = [
        item
        for item in TESTED_DATASETS + TESTED_USE_CASES
        if item["file"] in abspaths
    ]

    sorted_files["query"][question_tests] = [
        item
        for item in TESTED_QUERIES
        if item["file"] in abspaths
    ]
        
    errors = []
        
    for test_type in sorted_files.keys():
        test_dict = sorted_files[test_type]

        nb_files = sum([
            len(test_dict[suite])
            for suite in test_dict.keys()
        ])

        if nb_files == 0:
            continue

        for suite in test_dict.keys():
            
            files = test_dict[suite]
            report, assertor = new_report(test_type)
            suite(files, report, assertor)

            errors += [
                {
                    "subject_title": str(subject_title),
                    "criterion": str(criterion),
                    "error_title": str(error_title),
                    "error_description": str(error_description)
                }
                for (subject_title, criterion, error_title, error_description)
                in report.query(GET_MAJOR_FAILS)
            ]

    for error in errors:
        standard_criterion = error["criterion"].startswith(str(OLIVAW_ONTOLOGY))
        criterion_title, criterion_description = [
            (str(title), str(description))
            for title, description in (
                olivaw_earl_graph
                if standard_criterion
                else custom_tests
            ).query(
                GET_CRITERION_SUMMARY.replace(
                    "CRITERION",
                    f"<{error['criterion']}>"
                )
            )
        ][0]

        error["criterion_title"] = criterion_title
        error["criterion_description"] = criterion_description

    for error in errors:
        output.write_line("\nError:")
        output.write_line(f"\tSubject: {error['subject_title']}")
        output.write_line(f"\n\tCriterion title: {error['criterion_title']}")
        output.write_line(f"\tCriterion description: {error['criterion_description']}")
        output.write_line(f"\n\tError title: {error['error_title']}")
        output.write_line(f"\tError description: {error['error_description']}")
    
    return int(len(errors) > 0)

def run(line: list[str]) -> None:
    """Entry point of the `olivaw test precommit` command

    :param line: list of parameters sent to the pre-commit worker through the command line
    :type line: `list[str]`
    """
    raise SystemExit(main(line))
