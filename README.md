# Olivaw

This repository is a python library meant for providing tool in an Acimov ontology development context.
Anyone can use it as a python library as follows:

```shell
pip install git+https://github.com/Wimmics/olivaw
```

The repository should soon be used also as a Github Actions

## Getting started

This projet is whole new so expect more features and documentation later

In a repository respecting the Acimov architecture, model tests can be launched to evaluate the quality of your ontology using this command:

```shell
olivaw test model
```

Tests powered by [Corese](https://project.inria.fr/corese/) will be run

Two files will be generated in the folder .acimov/output of your project:
* a *.ttl* file containing a test report written with the [EARL](https://www.w3.org/WAI/ER/EARL10/WD-EARL10-Guide-20120125) ontology
* a version of this test report converted into a *markdown* format that is human readable

More is about to come soon!