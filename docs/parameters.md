# Parameters documentation

This framework uses repository specific parameters to run. These parameters are stored in the `.acimov/parameters.json` file.

A `parameters.json` file can be generated using this command:

```shell
olivaw init repo
```

These parameters will be explained on this page in case you would like to modify it.

# Parameters

## ontology_url

This is basically the deployment URL of your ontology.

This parameter is used for the model tests and data tests.

Since all the terms in the ontology have URIs, this is useful to search into fragments for terms from the ontology.

## term_distance_threshold

This is a threshold about the minimum Levenshtein distance you want your terms to have between them.

The levenshtein distance between 2 strings is the minimum number of modifications (add a character, remove a character, update a character) between these 2 strings.

It is a good pratice to have terms that are all different enough.

The default value is 3.

## blocking_errors

This is a list of errors that are considered as blocking in the context of your project.

The error list can be found in the [test documentation](./tests.md) and the [test resources file](../olivaw/constants/tests-resources.json).

This file represents for each test the different errors that can occur and for each of them what to write in the report depending on the outcome status.

In a generated `parameters.json` file the default value is to consider blocking the *syntax-error* and the *owl-rl-constraint-violation*

## gist_index

The gist index containing the data for all the gist files of your badges

The command `olivaw init repo` will automatically create a gist initialized with all the files your project need from the personnal acces token you provide it

## skipped_errors

A list of error ids that can be found in the [test documentation](./tests.md) and in the [test resources file](../olivaw/constants/tests-resources.json)

If an error id is in this list, this error should not appear in any test report, in the markdown files as well as in the turtle files

If not provided, olivaw considers that all errors should appear

## skipped_tests

A list of test ids that can be found in the [test documentation](./tests.md) and in the [test resources file](../olivaw/constants/tests-resources.json)

If a test id is in this list, this test should not be run neither appear in any test report, in the markdown files as well as in the turtle files

If not provided, olivaw considers that all tests should be run

## skipped_files

A list of files that could be found and tested in your Acimov project

These paths should be formatted as a relative path from your repository root up to the file itself

The provided files should not be tested by olivaw

If not provided, olivaw considers that all files should be tested