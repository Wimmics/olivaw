# MUNC report examples

Here are examples of reports generated by olivaw on the [PWKSO ontology](https://ns.inria.fr/pwkso). The ontology version that was used was the [PWKSO ontology](./pwkso.ttl) stored in this folder.

These reports have been generated by a development version of olivaw that corresponds to version `v0.0.5`.

In order to run this test, the [PWKSO ontology turtle file](https://ns.inria.fr/pwkso/pwkso.ttl) was put into an acimov repository with nothing but this file into the `src/` folder.

Here is the `parameters.json` used for the test:

```json
{
    "ontology_prefix": "pwkso",
    "ontology_namespace": "http://ns.inria.fr/pwkso/",
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
    "skip_for_subject": {}
}
```

Subjects `all-modules` and `all-fragments` are decided to be skipped here because it would be redundant since there is only one module here.

The command that was run to launch the tests was `olivaw test model`.

Check the [PWKSO turtle model report](./model-test-manual-NicoRobertIn-2024-06-06T14-38-00.ttl) and the [PWKSO markdown model report](./model-test-manual-NicoRobertIn-2024-06-06T14-38-00.md).