#!/usr/bin/env python

from typing import Sequence
from pre_commit import output
from os.path import sep, relpath

from olivaw.constants import PWD_TO_ROOT_FOLDER, GET_MAJOR_FAILS
from olivaw.test.corese import safe_load, check_OWL_constraints
from olivaw.test.turtle import prepare_graph, make_assertor

from olivaw.test.model.testing import modules_tests, modelets_tests
from olivaw.test.data.testing import data_tests
from olivaw.test.query.testing import question_tests

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

def main(files: Sequence[str] | None = None):
    if files is None or len(files) == 0:
        return 0

    paths = [
        relpath(file, PWD_TO_ROOT_FOLDER)
        for file in files
    ]

    for abs_file_path, rel_file_path in zip(files, paths):

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

        report = prepare_graph()
        assertor = make_assertor(
            report,
            test_type,
            f"https://github.com/Wimmics/olivaw/blob/main/olivaw/test/{test_type}/suite.py"
        )

        for suite in test_dict.keys():
            files = test_dict[suite]
            suite(
                files,
                report,
                assertor,
                skip_pass=True,
                tested_only=True
            )
        
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
        output.write_line("Error:")
        output.write_line(f"\tSubject: {error['subject_title']}")
        output.write_line(f"\tCriterion: {error['criterion']}")
        output.write_line(f"\tError title: {error['error_title']}")
        output.write_line(f"\tError description: {error['error_description']}")
        output.write_line(" ")
    
    return int(len(errors) > 0)

def run(line):
    raise SystemExit(main(line))
