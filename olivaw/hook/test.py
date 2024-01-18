#!/usr/bin/env python

from typing import Sequence
from pre_commit import output
from os.path import sep

from olivaw.test.corese import safe_load, check_OWL_constraints

current_folder = sep.join(__file__.split(sep)[:-1])

def test(files):
    report = []

    for file in files:
        graph = safe_load(file, disable_import=True)

        if isinstance(graph, list):
            report += [
                {
                    "subject": file,
                    "title": "Syntax error",
                    "description": error
                }
                for error in graph
            ]
            continue

        report += [
            {
                "subject": file,
                "title": "OWL RL violation",
                "description": error
            }
            for error in [
                error.replace("&#60;", "<").replace("&#10;", "\n")
                for error in check_OWL_constraints(graph)
            ]
        ]

    return report

def main(files: Sequence[str] | None = None):
    if files is None or len(files) == 0:
        return 0
    
    report = test(files)

    for error in report:
        output.write_line("Error:")
        output.write_line(f"\tFile: {error['subject']}")
        output.write_line(f"\tError: {error['title']}")
        output.write_line(f"\tDescription: {error['description']}")
        output.write_line(" ")
    
    return int(len(report) > 0)

def run(line):
    raise SystemExit(main(line))
