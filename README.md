# Olivaw

This repository is a python library meant for providing tool in an Acimov ontology development context.
Anyone can use it as a python library as follows:

```shell
pip install git+https://github.com/Wimmics/olivaw
```

The repository should soon be used also as a Github Actions

## Getting started

This projet is whole new so expect more features and documentation later.

### Initialize the repository

This tools can only operate on a acimov architectured github repository with at least:

* `src/` folder
* `domains/` folder with at least one subfolder
* `.acimov/` folder
* a `README.md` file at the root folder

It will also need a personal access token with the gist scope. To obtain one:

* Go to on this github web page: [https://github.com/settings/tokens](github.com/settings/tokens)
* Create a token
* Select the `gist` scope
* Copy the generated token (it will not be possible to see it later)

Your repository will need to know this token in a secret. You can follow these steps:

* Go to `{you_repository_url}/settings/secrets/actions`
* Click on `New repository secret`
* Type `GIST_SECRET` as the secret name and the personal access token as value

Now in your repository folder you can type the following command:

```shell
olivaw init repo
```

You will be asked the personal access token, the url of your ontology and finally the Levenshtein threshold distance you want between each of your terms.

You can see:

* The README has been edited to contain some badges at the the top
* A file named `parameters.json` has been create in the `.acimov/` folder
* A gist has been created in `https://gist.github.com/{your_username}` with some files meant for badges in you repository

### Launch model tests manually

In a repository respecting the Acimov architecture, model tests can be launched to evaluate the quality of your ontology using this command:

```shell
olivaw test model
```

Tests powered by [Corese](https://project.inria.fr/corese/) will be run

Two files will be generated in the folder .acimov/output of your project:
* a *.ttl* file containing a test report written with the [EARL](https://www.w3.org/WAI/ER/EARL10/WD-EARL10-Guide-20120125) ontology
* a version of this test report converted into a *markdown* format that is human readable

These options can also be used:

* `--skip-pass` to ignore in the report all the *Pass* outcomes
* `--tested-only` to ignore in the report all the *NotTested* outcomes

More is about to come soon!