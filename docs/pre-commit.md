# Pre-commit

Pre-commit is a tool that allows code to be executed on git event trigger, on client side.

It can be used in many ways, including automatic file formatting or automatic tests processed before pushing code into the server.

This tool can help a project to keep code quality standards during the whole lifetime of a project.

Pre-commit also allow developers to implement custom hooks that can be used in many other projects.

For more details about pre-commit, read the [pre-commit documentation](https://pre-commit.com/).

Olivaw repository contains a pre-commit hook that can be used in an acimov project.

## How to use the pre-commit hook

* create a new python environment ([python 3.11 or higher](https://www.python.org/downloads/release/python-3110/))
* install pre-commit in this environment using the command `pip install pre-commit`
* add a `.pre-commit-config.yaml` file at the root of the repository (we will see later what to write inside)
* use the command `pre-commit install` command at the root of the repository to set up the hooks

## The .pre-commit-config.yaml file

Inside the `.pre-commit-config.yaml` file this can be written

```yaml
default_language_version:
  python: python3
repos:
- repo: https://github.com/Wimmics/olivaw
  rev: v0.0.6
  hooks:
    - id: olivaw-test
```

Now, each time a commit is done, the olivaw pre-commit hook will trigger. It works using git cli as well as GitHub Desktop.

The first time this hook trigger, the olivaw repository will be cloned to a virtual environment that will be reused each time the hook will trigger in the future.

In this yaml file:

* the `repo` field is the url of the olivaw repository to clone
* the `rev` field is the tag to checkout the repository to
* the `id` field is the name of the olivaw pre-commit hook within the repository

Then, during each event trigger, some code will be executed based on the [olivaw pre-commit hook configuration file](../.pre-commit-hooks.yaml)

For each file that is staged for commit, the accurate test (model, data or query) suite will be applied.

Check the [olivaw tests documentation](./tests.md#2-available-tests) for more details.

If one of these tests raise an error, the commit or push will be blocked and some error summaries will be outputed.