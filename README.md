# Olivaw

An Agile methodology for ontology development named [ACIMOV](https://www.emse.fr/~zimmermann/Papers/mk2023.pdf) has been proposed in 2023.

This methodology is an extension of [SAMOD](https://essepuntato.it/samod/) with some improvements, including:

* the possibility to develop modular ontologies
* ensuring alignment to selected reference ontologies
* a wider collaboration between product owners, domain experts and ontology developers

This repository is a python library meant for providing tools in an Acimov ontology development context.

Olivaw proposes:

* command lines that make an Acimov development easier
* composite actions that can directly be called in workflows from any Acimov project
* a pre-commit hook that should prevent the biggest mistakes that could be pushed in an Acimov repository

This tool proposes different test tools all powered by Corese, check [Corese website](https://project.inria.fr/corese/) and [Corese repository](https://github.com/Wimmics/corese).

The test reports are first represented using the [EARL vocabulary](https://www.w3.org/TR/EARL10-Schema/) and then exported in the markdown format.

Examples of reports generated from existing ontology projects can be found in the [olivaw reports examples](https://github.com/Wimmics/olivaw/blob/main/docs/examples/) folder.

In order to get all the available features in olivaw, check the [olivaw functional documentation](https://github.com/Wimmics/olivaw/blob/main/docs/).

Moreover the project, from the project structure itself to the details about any module, function and constants, is documented, so check the [olivaw technical documentation](https://github.com/Wimmics/olivaw/blob/main/olivaw/).

If a bug is to be found or a feature to be proposed, please use [olivaw issue menu](https://github.com/Wimmics/olivaw/issues).

# Getting started

## Installing olivaw in a project

First prepare a python environment version 3.8 or greater (3.11 if pre-commit hook is meant to be used).

Then install the library from pipy:

```shell
pip install olivaw==0.0.5
```

It can also be installed using this command:

```shell
pip install git+https://github.com/Wimmics/olivaw@v0.0.5
```

## Intializing a repository

### Acimov repository structure

This tool is meant to work on an Acimov structured repository.

The [acimov olivaw repository template](https://github.com/Wimmics/Olivaw-Template) can be used to create a new project or be used to adapt an existing project to this structure.

This repository contains:

* the folders:
  * `.acimov/`
  * `resources/`
  * `primer/`
  * `src/`
  * `domains/`
  * `use-cases/`
*  a `README.md` file at the root folder

### Getting a personnal access token with gist scope

This framework proposes automatically updated badges at the top of the README.md on each branch.

To make this work a personnal access token with the `gist` scope is required.

* First go to the [Github access token generation webpage](https://github.com/settings/tokens).
* Then create a personnal access token with only the `gist` scope. Copy/paste this token somewhere because it will never be shown again.
* Then go to `{repository_url}/settings/secrets/actions`, create a new repository secret named `GIST_SECRET` and paste the key

### Initialize repository parameters

Finally this library needs a `parameters.json` file in the `.acimov/` folder that should contain parameters related to the repository.

Use this command to generate one:

```shell
olivaw init repo
```

Just follow the instructions (the personnal access token with `gist` scope will be asked again).

After the execution of the command file named `parameters.json` in the `.acimov/` folder should have appeared and also badges added to the top of the repository `README.md` file with an initialized gist on [gist website](https://gist.github.com/).

These parameters can eventually be customized using the [olivaw parameters documentation](https://github.com/Wimmics/olivaw/blob/main/docs/parameters.md).

The olivaw commands are now available inside the repository!

# Basics about olivaw

## The command line

Here is only a short overview of the main commands. Check the [olivaw command line documentation](https://github.com/Wimmics/olivaw/blob/main/docs/commands.md) for more details about the available commands.

### Model test

Anywhere in the repository use this command to launch a model test:

```shell
olivaw test model
```

### Data test

This command is for launching data test

```shell
olivaw test data
```

### Query test

This command is for launching query test

```shell
olivaw test query
```

## The Github actions

Here is an overview of the actions available. For more details see the [olivaw Github Actions documentation](https://github.com/Wimmics/olivaw/blob/main/docs/actions.md).

Each actions of this chapter involve to create a `.yaml` file located in `{repository_path}/.github/workflows/`.

### Automatic tests on push

In `./github/worflows/` folder, add a `test.yaml` file containing this:

```yaml
name: test
on: push

jobs:
  test:
    permissions:
      contents: write
    runs-on: ubuntu-latest
    steps:
    - uses: Wimmics/olivaw/test-actions@v0.0.5
      with:
        repository: ${{ github.repository }}
        ref: ${{ github.ref }}
        gist-secret: ${{ secrets.GIST_SECRET }}
```

Then, after each push on the repository an actions will be triggered and after some time, in the `.acimov/output/` folder should have appeared:

* RDF files written in the turtle format representing the result of the test, written with the EARL vocabulary
* markdown files representing in a human readable way the previous turtle files

### Badges branch initialization

In `./github/worflows/` folder, add a `init-branch.yaml` file containing this:

```yaml
name: init-branch
on: create

jobs:
  model-test:
    permissions:
      contents: write
    runs-on: ubuntu-latest
    steps:
    - uses: Wimmics/olivaw/init-branch@v0.0.5
      with:
        repository: ${{ github.repository }}
        ref: ${{ github.ref }}
        gist-secret: ${{ secrets.GIST_SECRET }}
```

Then on each time a branch is published, the actions should create new gists and update the badges in the README.md without anything left to do for the developper.

## The pre-commit hook

A pre-commit hook is available in this repository to prevent the developper to push big mistakes on the server.

To use it should need first need to install pre-commit. Create a fresh new python 3.11 environment for the tool to work properly.

Once the new environment set, install pre-commit with this command:

```shell
pip install pre-commit
```

Then add a file named `.pre-commit-config.yaml` at the root of the repository containing this:

```yaml
default_language_version:
  python: python3
repos:
- repo: https://github.com/Wimmics/olivaw
  rev: v0.0.5
  hooks:
    - id: olivaw-test
```

Then use this command at the root of the repository:

```shell
pre-commit install
```

Finally add the `.pre-commit-config.yaml` file to the commit:

```turtle
git add .pre-commit-config.yaml
```

Now, each time a commit is made, the staged files will be tested and the commit will be blocked if any blocking error is to be found in any of those files.

The test takes a few seconds and pre-commit needs a moment to prepare the hook on the very first use.

There is also the [olivaw pre-commit hook documentation](https://github.com/Wimmics/olivaw/blob/main/docs/pre-commit.md).