# Parameters documentation

This framework uses repository specific parameters to run. These parameters are stored in the `.acimov/parameters.json` file.

A `parameters.json` file can be generated using this command:

```shell
olivaw init repo
```

Check the [command line documentation](./commands.md#olivaw-init-repo) for more details.

These parameters will be explained in this page in case you would like to modify it.

# Parameters

The `.acimov/parameters.json` file is a json file containing a dictionary with some fields that will be detailed in this section.

## ontology_prefix

This field is mandatory and provides a string containing the preferred prefix for the ontology.

This prefix will be used when generating the turtle code snippets that will be provided in the test reports.

## ontology_namespace

This field is mandatory and provides a string containing the namespace of the ontology.

This is used in the tests because it can determine if a URI in the ontology or the datasets are meant to belong to the ontology that is under development.

## term_distance_threshold

This field is mandatory ad represents the threshold about the minimum Levenshtein distance that are allowed between a pair of ontology terms.

The levenshtein distance between 2 strings is the minimum number of modifications (add/remove/update of a character) between these 2 strings.

It is a good pratice to have terms that are all different enough.

The default value is 3.

## blocking_errors

This field is mandatory and provides a list of error identifiers that will be considered as blocking.

The list of error identifiers can be found in the [error resource file](../olivaw/constants/error-resources.json).

Most of the errors are considered by default as `MinorFail` except the `prefix-typo` error that is considered a `CannotTell`. If a error is considered as blocking, it will always be mentionned as a `MajorFail` outcome if integrated to a test report.

See the [outcome documentation](./tests.md#115-the-outcomes), the [prefix validity test documentation](./tests.md#224-prefix-validity) and the [error resource file](../olivaw/constants/error-resources.json) for more details.

## gist_index

This field is mandatory and contains a string representing a gist index containing the data for all the gist files of your badges.

The command `olivaw init repo` will automatically create a gist initialized with all the files your project need from the personnal access token you provide it.

## skipped_errors

This field is not mandatory and provides a list of error ids that can be found in the [test documentation](./tests.md#2-available-tests) and in the [test resources file](../olivaw/constants/tests-resources.json)

If an error id is in this list, this error should not appear in any test report, in the markdown files as well as in the turtle files

If not provided, olivaw considers that all errors should appear.

## skipped_tests

This field is not mandatory and provides list of strings representing test ids that can be found in the [test documentation](./tests.md#2-available-tests) and in the [test resources file](../olivaw/constants/tests-resources.json)

If a test id is in this list, this test should not be run neither appear in any test report, in the markdown files as well as in the turtle files

If not provided, olivaw considers that all tests should be run

## skipped_subjects

This field is not mandatory and provides a list of string representing either relative paths from the repository folder to a given file, or a subject identifier that can be found in a test report.

The provided subjects should not be tested by olivaw

If not provided, olivaw considers that all files should be tested

## skip_for_test

This field is not mandatory and provides a dictionary. The keys are string representing test identifier. The values are lists of strings representing either relative paths from the repository folder to a given file or a subject identifier that can be found in a test report.

For each test identifier provided, the different subjects provided in the list should be skipped during the tests.

If not provided, olivaw skips no subject for any given test.

Check the [test documentation](./tests.md#2-available-tests) for more details about the available test and error identifiers.

## skip_for_subject

This field is not mandatory and provides a dictionary. The keys are either relative paths from the repository folder to a given file or a subject identifier that can be found in a test report. The values are lists of strings representing string representing test identifier

For each test subject provided, the different tests providd in the list should be skipped during the tests.

If not provided, olivaw skips no test for any given subject.

Check the [test documentation](./tests.md#2-available-tests) for more details about the available test and error identifiers.