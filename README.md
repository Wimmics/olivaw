# Olivaw

An Agile methodology for ontology development named [ACIMOV](https://www.emse.fr/~zimmermann/Papers/mk2023.pdf) has been proposed on 2023.

This methodology is an extension of [SAMOD](https://essepuntato.it/samod/) with some improvements, including:

* the possibility to develop modular ontologies
* ensuring alignment to selected reference ontologies
* a wider collaboration between product owners, domain experts and ontology developpers

This repository is a python library meant for providing tools in an Acimov ontology development context.

Olivaw proposes:

* command lines that makes an Acimov development easier
* composite actions that can directly be called in workflows from any Acimov project
* a pre-commit hook that should prevent the biggest mistakes that could be pushed in an Acimov repository

This tool proposes different test tools all powered by Corese, check their [website](https://project.inria.fr/corese/) and [repository](https://github.com/Wimmics/corese)

The test reports are then represented using the [EARL vocabulary](https://www.w3.org/TR/EARL10-Schema/)

All the functional documentation concerning olivaw can be found in [the docs/ folder](./docs/)

There is also technical docuùentation that can be followed from [there](./olivaw/)

If a bug is to be found don't hesitate to create an [issue](https://github.com/Wimmics/olivaw/issues)

# Getting started

## Installing olivaw in a project

First prepare a python environment version 3.8 or greater.

Then install the python library using this command:

```shell
pip install git+https://github.com/Wimmics/olivaw@v0.0.3
```

## Intializing a repository

### Acimov repository structure

This tool is meant to work on an Acimov structured repository.

This repository constains:

* the folders:
  * `.acimov/`
  * `src/`
  * `domains/`
  * `use-cases/`
*  a `README.md` at the root

A template repository ready to fork should be provided soon.

### Getting a personnal access token with gist scope

This framework proposes automatically updated badges at the top of the README.md on each branch.

To make this work a personnal access token with the `gist` scope is required.

* First go to the [Github webpage dedicated to access token generation](https://github.com/settings/tokens)
* Then create a personnal access token with only the `gist` scope. Copy/paste this token somewhere because it will never be shown again.
* Then go to `{repository_url}/settings/secrets/actions`, create a new repository secret named `GIST_SECRET` and paste the key

### Initialize repository parameters

Finally this library needs a `parameters.json` file in the `.acimov/` folder that should contain parameters related to the repository.

You can use this command to generate one:

```shell
olivaw init repo
```

Just follow the instructions (the personnal access token with `gist` scope will be asked again).

After the execution of the command file named `parameters.json` in the `.acimov/` folder should have appeared and also badges added to the top of the repository `README.md` file.

You can enventually customize this parameters using the [parameters documentation](./docs/parameters.md).

You are now ready to use all the commands of olivaw inside this repository!

# Basics about olivaw

## The command line

Here is only a short overview of the main commands. Check the [olivaw command line documentation](./docs/commands.md) for more details about the available commands.

Also more is about to come.

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

Here is an overview of the actions available. For more details see the [olivaw Github Actions documentation](./docs/actions.md).

Each actions of this chapter involve to create a `.yaml` file located in `{repository_path}/.github/workflows/`.

### Automatic tests on push

In `worflows/` folder, add a `test.yaml` file containing this:

```yaml
name: test
on: push

jobs:
  test:
    permissions:
      contents: write
    runs-on: ubuntu-latest
    steps:
    - run: |
        REF=${{ github.ref }}
        echo "github.ref: $REF"
        IFS='/' read -ra PATHS <<< "$REF"
        BRANCH_NAME="${PATHS[1]}_${PATHS[2]}"
        echo $BRANCH_NAME
        echo "MAIN=main" >> $GITHUB_ENV
        echo "BRANCH=$(echo ${BRANCH_NAME})" >> $GITHUB_ENV
    - uses: Wimmics/olivaw/test-actions@v0.0.3
      with:
        repository: ${{ github.repository }}
        ref: ${{ github.ref }}
        gist-secret: ${{ secrets.GIST_SECRET }}
        model-test: true
        data-test: true
        query-test: true
        commit-report: ${{ env.BRANCH == env.MAIN }}
        archive-report: true
```

Then, after each push on the repository an actions will be triggered and after some time, in the `.acimov/output/` folder should have appeared:

* RDF files written in the turtle format representing the result of the test, written with the EARL vocabulary
* markdown files representing in a human readable way the previous turtle files

### Badges branch initialization

In `worflows/` folder, add a `init-branch.yaml` file containing this:

```yaml
name: init-branch
on: create

jobs:
  model-test:
    permissions:
      contents: write
    runs-on: ubuntu-latest
    steps:
    - name: Parsing repo ref data
      shell: bash
      run: |
        REF=${{ inputs.ref }}
        echo "github.ref: $REF"
        IFS='/' read -ra PATHS <<< "$REF"

        REF_TYPE="${PATHS[1]}"
        echo $REF_TYPE
        echo "REF_TYPE=$(echo ${REF_TYPE})" >> $GITHUB_ENV
    - uses: Wimmics/olivaw/init-branch@test-actions-18
      if: ${{ env.REF_TYPE != 'tags' }}
      with:
        repository: ${{ github.repository }}
        ref: ${{ github.ref }}
        gist-secret: ${{ secrets.GIST_SECRET }}
```

Then on each time a branch is published, the actions should create new gists and update the badges in the README.md without anything left to do for the developper.

## The pre-commit hook

A pre-commit hook is available in this repository to prevent the developper to push big mistakes on the server.

To use it should need first need to install pre-commit. I strongly advise to create a fresh new python 3.11 environment for the tool to work properly.

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
  rev: v0.0.3
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

Now, each time a commit is made, the staged files will be tested and the commit will be blocked if any blocking error is to be found in those files.

The test takes a few seconds and pre-commit needs a moment to prepare the hook on the very first use.