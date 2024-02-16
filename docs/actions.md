# Actions

This repository contains actions that should help the Acimov lifecycle.

In order to make these actions available in your project, check the main [README.md](../README.md#getting-started)

Here are some details about the parameters and what the actions do.

## Branch initialization

This action is meant for updating the badges and their related gist files each time someone published a new branch

Since a branch is always created out of another branch, the README.md file will contain link to gist files that have the values from where the branch was created.

The actions will then proceed as follows:

* Read the values of the badges of the parent branch and store these values
* Update the README.md to replace the gist files URLs
* Create new gist files meant for that branch with the stored badges values

You can create a `init-branch.yaml` file in the `.github/workflows` folder containing this:

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
        model-test: true
        data-test: true
        commit-report: true
        archive-report: true
```

The parameters are:
* `repository`: a string structured like `your_organization/your_repository`. The environment variable `${{ github.repository }}` provides it
* `ref`: a string containing a reference to which branch you are pushing, for example `refs/heads/main`. The environment variable `${{ github.ref }}` is perfect for it
* `gist-secret`: a string containing the personnal access token with the `gist` scope to update the gist files. If there is this value in the `GIST_SECRET` secret that was asked at the repository initialization, then the environment variable `${{ secrets.GIST_SECRET }}` provides it
* `model-test`: an optional boolean stating if the model tests should be run. The default value is `true`
* `data-test`: an optional boolean stating if the data tests should be run. The default value is `true`
* `commit-report`: an optional boolean stating if the reports should be pushed in the related branch, the default value is `true`
* `archive-report`: an optional boolean stating if the reports should be stored as a Github artifact, the default value is `true`
* `server-url`: an optional string containing the URL of the server, in case you are not hosted on github. The default is "https://github.com"

## Automatic test on push

This actions is meant to have a regular test of the repository and have at each moment a summary of the health of a branch.

This actions does the following:

* Launching the model tests if asked
  * providing the machine readable `.ttl` report in the `.acimov/output` folder
  * providing the human readable `.md` report in the `.acimov/output` folder
* Launching the data tests if asked
  * providing the machine readable `.ttl` report in the `.acimov/output` folder
  * providing the human readable `.md` report in the `.acimov/output` folder
* Uploading Github Artifacts of the markdown report that you can access in the Actions menu for a month
* Updating the badges values

You can use this actions by creating a file named `test.yaml` in the `.github/workflows/` folder. That file should contain this:

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

The parameters are:

* `repository`: a string structured like `your_organization/your_repository`. The environment variable `${{ github.repository }}` provides it
* `ref`: a string containing a reference to which branch you are pushing, for example `refs/heads/main`. The environment variable `${{ github.ref }}` is perfect for it
* `gist-secret`: a string containing the personnal access token with the `gist` scope to update the gist files. If there is this value in the `GIST_SECRET` secret that was asked at the repository initialization, then the environment variable `${{ secrets.GIST_SECRET }}` provides it
* `model-test`: a boolean describing if the test should cover the modules and the modelets (all the files named `onto.ttl` in the `domains` folder)
* `data-test`: a boolean describing if the test should cover the datasets (all the `dataset.ttl` files in the `domains` folder) and the use-cases (the `.ttl` files in the folder `use-cases`) 
* `server-url`: an optional string containing the URL of the server, in case you are not hosted on github. The default is "https://github.com"
