# Pre-commit

Pre-commit is a tool that allows code to be executed on git event trigger, on client side.

It can be used in many ways, including automatic file formatting or automatic tests processed before pushing code into the server.

This tool can help a project to keep code quality standards during the whole lifetime of a project.

Pre-commit also allow developers to implement custom hooks that can be used in many other projects.

For more details about pre-commit, read the [documentation](https://pre-commit.com/).

Olivaw repository contains a pre-commit hook that can be used in an acimov project.

## How to use the pre-commit hook

* create a new python environment ([python 3.11 or higher](https://www.python.org/downloads/release/python-3110/))
* install pre-commit in this environment using the command `pip install pre-commit`
* add a `.pre-commit-config.yaml` file at the root of your repository (we will see later what to write inside)
* use the command `pre-commit install` command at the root of your repository to set up the hooks

## The .pre-commit-config.yaml file

Inside the `.pre-commit-config.yaml` file this can be written

```yaml
default_language_version:
  python: python3
repos:
- repo: https://github.com/Wimmics/olivaw
  rev: v0.0.3
  hooks:
    - id: check-fragments
```

Now, each time a commit is done the olivaw pre-commit hook will trigger.

The first time this hook trigger, the olivaw repository will be cloned to a virtual environment that will be reused each time the hook will trigger in the future.

In this yaml file:

* the `repo` field is just the url of the olivaw repository to clone
* the `rev` field is the tag to checkout the repository to
* the `id` field is the name of the olivaw pre-commit hook within the repository

Then some code will be executed based on the [olivaw pre-commit hook configuration file](../.pre-commit-hooks.yaml)

The [syntax tests](tests.md#211-syntax) and the [owl rl constraint violation tests](./tests.md#212-owl-rl-constraint) will be run.

If one of these tests raise an error, the commit or push will be blocked and some error will be outputed.