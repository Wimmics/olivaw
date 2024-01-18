# Olivaw

An Agile methodology for ontology development named [ACIMOV](https://www.emse.fr/~zimmermann/Papers/mk2023.pdf) has been proposed on 2023.

This methodology is an extension of [SAMOD](https://essepuntato.it/samod/) with some improvements, including:

* the possibility to develop modular ontologies
* ensuring alignment to selected reference ontologies
* a wider collaboration between product owners, domain experts and ontology developpers

This repository is a python library meant for providing tools in an Acimov ontology development context.

In this repository you will find:

* command lines that should help you to make your Acimov development easier
* composite actions that you can directly call in workflows from your Acimov project
* a pre-commit hook that should prevent the biggest mistakes that could be pushed in your Acimov repository

This tool proposes different test tools all powered by Corese, you can check their [website](https://project.inria.fr/corese/) and [repository](https://github.com/Wimmics/corese)

The test reports are then represented using the [EARL vocabulary](https://www.w3.org/TR/EARL10-Schema/)

This project is very young so if a bug is to be found don't hesitate to create an [issue](https://github.com/Wimmics/olivaw/issues)

# Getting started

## Installing olivaw in your project

First you will need a python environment version 3.8 or greater.

Then install the python library using this command:

```shell
pip install git+https://github.com/Wimmics/olivaw
```

## Intializing a repository

### Acimov repository structure

In order to use this tool properly you need an Acimov structured repository.

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

To make this work you will need a personnal access token with the `gist` scope.

* First go to the [Github webpage dedicated to access token generation](https://github.com/settings/tokens)
* Then create a personnal access token with only the `gist` scope. Copy/paste this token somewhere because it will never be shown to you again.
* Then go to `{your_repository_url}/settings/secrets/actions`, create a new repository secret named `GIST_SECRET` and paste the key

### Initialize repository parameters

Finally this library needs a `parameters.json` file in the `.acimov/` folder that should contain parameters related to the repository.

You can use this command to generate one:

```shell
olivaw init repo
```

Just follow the instructions (you will be asked again the personnal access token with `gist` scope).

After the execution of the command you should see a file named `parameters.json` in the `.acimov/` folder and also badges added to the top of your repository.

You can enventually customize this parameters using the [parameters documentation](./docs/parameters.md).

You are now ready to use all the commands of olivaw inside this repository!

# Basics about olivaw

## The command line

Here is only a short overview of the main commands. If you want to see the documentation related to all of the commands and their options see the [olivaw command line documentation](./docs/commands.md).

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

## The Github actions

Here is an overview of the actions available. For more details see the [olivaw Github Actions documentation](./docs/actions.md).

Each actions of this chapter involve to create a `.yaml` file located in `{your_repository_path}/.github/workflows/`.

### Automatic tests on push

In your `worflows/` folder, add a `test.yaml` file containing this:

```yaml
name: test
on: push

jobs:
  test:
    permissions:
      contents: write
    runs-on: ubuntu-latest
    steps:
    - uses: Wimmics/olivaw/test-actions@v0.0.3
      with:
        repository: ${{ github.repository }}
        ref: ${{ github.ref }}
        gist-secret: ${{ secrets.GIST_SECRET }}
        model-test: true
        data-test: true
```

Then, after each push on the repository an actions will be triggered and after one minute you should see in the `.acimov/output/` folder:

* RDF files written in the turtle format representing the result of the test, written with the EARL vocabulary
* markdown files representing in a human readable way the previous turtle files

### Badges branch initialization

In your `worflows/` folder, add a `init-branch.yaml` file containing this:

```yaml
name: init-branch
on: create

jobs:
  init-branch:
    permissions:
      contents: write
    runs-on: ubuntu-latest
    steps:
    - uses: Wimmics/olivaw/init-branch@v0.0.3
      with:
        repository: ${{ github.repository }}
        ref: ${{ github.ref }}
        gist-secret: ${{ secrets.GIST_SECRET }}
```

Then on each time a branch is published, the actions should create new gists and update the badges in the README.md without anything left to do for the developper.

## The pre-commit hook

A pre-commit hook is available in this repository to prevent the developper to push big mistakes on the server.

To use it you should need first need to install pre-commit. I strongly advise you to create a fresh new python 3.11 environment for the tool to work properly.

Once your new environment set, you can install pre-commit with this command:

```shell
pip install pre-commit
```

Then you should add a file named `.pre-commit-config.yaml` at the root of you repository containing this:

```yaml
default_language_version:
  python: python3
repos:
- repo: https://github.com/Wimmics/olivaw
  rev: v0.0.3
  hooks:
    - id: check-fragments
```

Then you just have to use this command at the root of the repository:

```shell
pre-commit install
```

Finally add the `.pre-commit-config.yaml` file to the commit.

Now, each time you commit, the staged files will be tested and the commit will be blocked if a syntax error or a owl constraint violation is present in these files.

The test takes a few seconds and obviously pre-commit needs a moment to prepare the hook in at the very first use of this hook.

More is about to come soon!
