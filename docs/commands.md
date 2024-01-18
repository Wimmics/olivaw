# Olivaw command lines

This python package provides command lines that are useful in the context of acimov methodology.

Here is an overview of which commands are available

In order to make these commands available for your project, check the main [README.md](../README.md#getting-started)

Once done, there are options that are common between all these commands

All of these options are optional but can override the git information that are automatically retrieved

* `--mode=...`: set to *actions* if you want to make the tool think it is in an actions environment
* `--REPO-ROOT=...` set to override path to the repository root folder
* `--REPO_URI=`: set to override the repository URI
* `--BRANCH=`: set to override the actual branch
* `--REF=`: set to override the actuel ref
* `--DEV_USERNAME=`: set to override the actual git user name

# olivaw init

There are commands for initializing a repository or a branch of a already initialized repository.

## olivaw init repo

This command is meant to initialize an acimov repository. This command should require:

* the deployment URL of the repository
* a personnal access with the `gist` scope
* a minimal Levenshtein distance you expect between the terms of your ontology

Finally this command should provide:

* a `parameters.json` file in the `.acimov/output/` folder
* a gist created with files containing accurate starting value
* badges in the README.md file pointing to the files of the fresh new gist

## olivaw init branch

This command is meant for the [init-branch actions](./actions.md#branch-initialization) but can also be used locally if needed.

The command updates the URLs for the files of the badges so that these badges are functional after the next [test actions](./actions.md#automatic-test-on-push)

# olivaw test

There are several commands meant for testing the ontology fragments of your project.

An acimov project can have 3 kinds of tests about the ontology fragments:

* *model tests*: tests about the validity of the *modules* and the *modelets*. This involves testing any file that is meant for describing parts of the vocabulary.
* *data tests*: tests about the validity of the *datasets* that are developped and the *use cases*. This is basically testing not the ontology parts but anything that is an instanciation of your ontology
* *query tests*: this methodology involves to develop relevant questions that can not be formalized at some point in sparQL due to a missing term. The ontology developpers then implement these needed terms and prove that these questions can then be answered through sparQL requests. This test is meant for testing the implementation of these questions.

This project aims to provides automatic solutions for those tests.

These tests are powered by Corese, check their [website](https://project.inria.fr/corese/) and [repository](https://github.com/Wimmics/corese)
The test reports are then represented using the [EARL vocabulary](https://www.w3.org/TR/EARL10-Schema/)

According to the [EARL vocabulary](https://www.w3.org/TR/EARL10-Schema/), all the tests processed here can have one of these status:

* Pass: the test went fine
* Fail: the test went wrong
* CannotTell: the software cannot relate if this is a Fail or a Pass, a human being is needed to check
* NotTested: the test needs some prerequisites to run. However these prerequisite were not fulfilled

For the sake of being able to give a priority on a fail, like we could usually do in other tests frameworks, the Fail set was partitionned (see the [acimov dataset](../olivaw/test/test-onto.ttl)):

* MajorFail: the bug is critical and must be solved
* MinorFail: this fail is not preventing anyone to use the ontology (ex: Best Practice mistakes)

For all of these commands these two options are available on top of those mentioned in the beggining of this chapter:

* `--skip-pass` to ignore in the report all the *Pass* outcomes
* `--tested-only` to ignore in the report all the *NotTested* outcomes

## olivaw test model

This command makes a model test on the project.

The resources that are being tested are:

* The modules (the `.ttl` files located in the `src/` folder)
* The modelets (the `onto.ttl` files that can be found in depth in `domains/` folder)
* The modules with some terms merged from the modelets (the terms from the modelets have a `rdfs:isDefinedBy` property to indicate to which module it should belong after merging)
* all the modules merged together in one unique graph
* all the modules and all the modelets merged together in one graph

The tests executed on each resource are checking:

* the syntax
* the OWL constraints violation (each constraint that exists in OWL RL)
* if the resource is compatible with a given profile (OWL EL, OWL QL, OWL TC)
* if the terms of the ontology are far enough from each other on a spelling point of view
* if each term has a `rdfs:label` label property pointing to at least one litteral in English
* if each term has a `rdfs:isDefinedBy` property pointing to the module it belongs to

These differents test can have different errors. To see these errors in details, check the [test resources file](../olivaw/constants/tests-resources.json)

This command will output two files located in the `.acimov/output/` folder:

* One RDF file written in turtle format providing a report that is program-readable
* One markdown file that is the human-readable version of the previous RDF file

## olivaw test data

This command makes a data test on the project.

The resources that are being tested are:

* The datasets (the `dataset.ttl` files located in depth in the `domains/` folder)
* The use cases (any `.ttl` file located in the `use-cases/` folder)

The tests executed on each resource are checking:

* the syntax
* the OWL constraints violation (each constraint that exists in OWL RL)

These differents test can have different errors. To see these errors in details, check the [test resources file](../olivaw/constants/tests-resources.json)

This command will output two files located in the `.acimov/output/` folder:

* One RDF file written in turtle format providing a report that is program-readable
* One markdown file that is the human-readable version of the previous RDF file

## olivaw test precommit

This command line is only a entry point for olivaw precommit hook.

It is only mean to work in a precommit hook trigger.

# olivaw flush

Generating many tests can pollute a lot the `.acimov/output/` folder and you would want to empty it without touching on the files generated by Github Actions.

You can flush the `.acimov/output/` folder with the following command:

```shell
olivaw flush
```

# olivaw show

The commands of this chapter are meant to retrieve easily information from the parameters for the project.

These commands were actually meant for Github Actions but they can also be used by users on demand.

## olivaw show gist

Output the gist ID that should contain the files for the information of all the badges

## olivaw show badges

Output the values of the badges of the actual branch
