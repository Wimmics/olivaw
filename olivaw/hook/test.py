#!/usr/bin/env python
"""Module providing the reusable pre-commit hook"""

from typing import Sequence
from pre_commit import output
from rdflib import Graph
from os.path import sep, relpath, exists

from olivaw.test.corese import export_graph

from olivaw.test.model.testing import (
    modules_tests,
    modelets_tests,
    shape_tests as model_shape_tests
)

from olivaw.test.data.testing import (
    data_tests,
    shape_tests as data_shape_tests
)

from olivaw.test.query.testing import question_tests

from olivaw.constants import (
    PWD_TO_ROOT_FOLDER,
    GET_MAJOR_FAILS,
    OLIVAW_EARL_DATASET,
    PWD_TO_MODEL_TEST_ONTO,
    GET_CRITERION_SUMMARY
)
from olivaw.test.turtle import new_report

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
olivaw_earl_graph.parse(PWD_TO_MODEL_TEST_ONTO)

custom_tests_base = [export_graph(graph) for graph in model_shape_tests] + [export_graph(graph) for graph in data_shape_tests]
custom_tests_base = "\n".join(custom_tests_base)
custom_tests = Graph()
custom_tests.parse(data=custom_tests_base, format="ttl")

def main(files: Sequence[str] | None = None) -> int:
    """Function embedding the business logic behind a pre-commit worker
    
    :param files: List of options sent to the pre-commit worker through the command line
    :type files: list[str]

    :return: The error code that will return the pre-commit worker
    :rtype: int
    """
    if files is None:
        return 0

    paths = [
        (file, relpath(file, PWD_TO_ROOT_FOLDER))
        for file in files
        if exists(file)
    ]

    if len(files) == 0:
        return 0

    for abs_file_path, rel_file_path in paths:

        if rel_file_path.startswith(f"src{sep}"):
            sorted_files["model"][modules_tests].append(abs_file_path)

        elif rel_file_path.startswith(f"domains{sep}"):

            if rel_file_path.endswith(f"{sep}onto.ttl"):
                sorted_files["model"][modelets_tests].append(abs_file_path)

            elif rel_file_path.endswith(f"{sep}dataset.ttl"):
                sorted_files["data"][data_tests].append(abs_file_path)

            elif rel_file_path.endswith(".rq"):
                sorted_files["query"][question_tests].append(abs_file_path)

            else:
                output.write_line(f"Unprocessable file: {abs_file_path}")

        elif rel_file_path.startswith(f"use-cases{sep}"):
            sorted_files["data"][data_tests].append(abs_file_path)

        else:
            output.write_line(f"Unprocessable file: {abs_file_path}")
        
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
        standard_criterion = error["criterion"].startswith(str(OLIVAW_EARL_DATASET))
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
    :type line: list[str]
    """
    raise SystemExit(main(line))
