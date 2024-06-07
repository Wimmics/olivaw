# COSWOT-ACIMOV report examples

Here are examples of reports generated by olivaw on the [COSWOT-ACIMOV project](https://gitlab.com/coswot/coswot-acimov).

These reports have been generated by a development version of olivaw that corresponds to version `v0.0.5`.

It was tested on hash `1ea6ad8e0d2d5adb5ec4094239509b8cbac32394`.

In order to fully match the folder naming convention that was decided for olivaw frameork, these renames have been made:

* `./core/` -> `./src/`
* `./examples` -> `./use-cases/`
* `./domains/*/*/vocabulary.ttl` -> `./domains/*/*/onto.ttl`

In order to make the report viewable from github, some options have been enabled in order to make these reports short enough.

The command used was `olivaw test model --SKIP-PASS --TESTED-ONLY`

Here is the `parameters.json` used for the test:

```json
{
    "ontology_prefix": "coswot",
    "ontology_namespace": "https://w3id.org/coswot/",
    "term_distance_threshold": 3,
    "blocking_errors": [
        "syntax-error",
        "owl-rl-constraint-violation"
    ],
    "gist_index": "",
    "skipped_errors": [],
    "skipped_tests": [],
    "skipped_subjects": ["all-modules", "all-fragments"],
    "skip_for_test": {},
    "skip_for_subject": {},
    "project_prefixes": {
        "schema": "http://schema.org/"
    }
}
```

Subjects `all-modules` and `all-fragments` are decided to be skipped here so that Github markdown renderer could generate the whole visualisation of the Markdown report.

Check the [COSWOT turtle model report](./model-test-manual-NicoRobertIn-2024-06-06T11-25-56.ttl) and the [COSWOT markdown model report](./model-test-manual-NicoRobertIn-2024-06-06T11-25-56.md).