# Olivaw tests actions

This actions does the following:

* Launching the model tests and generate reports if asked
* Launching the data tests and generate reports if asked
* Launching the query tests and generate reports if asked
* Commit the report in the `.acimov/output` folder if asked
* Uploading Github Artifacts for the markdown reports, if asked. The Actions menu can be accessed for a month
* Updating the badges values

Each test step can generate both turtle file report and markdown files, see the [turtle format documentation](../docs/tests.md#11-turtle-format) and the [markdown format documentation](../docs/tests.md#12-markdown-format)

Create a file named `test.yaml` in the `.github/workflows/` folder. That file should contain this:

```yaml
name: test
on: push

jobs:
  test:
    permissions:
      contents: write
    runs-on: ubuntu-latest
    steps:
    - uses: Wimmics/olivaw/test-actions@v0.0.7
      with:
        gist-secret: ${{ secrets.GIST_SECRET }}
```

Here is a summary of the available parameters:

|Parameter|Type|Required|Default|Description|Example|
|---------|----|--------|-------|-----------|-------|
|`gist-secret`|string|false||personnal access token with the `gist` scope to update the gist files|`${{ secrets.GIST_SECRET }}`|
|`model-test`|boolean|false|true|should model tests be run, check the [test documentation](../docs/tests.md#21-model-tests)|true|
|`data-test`|boolean|false|true|should data tests be run, check the [test documentation](../docs/tests.md#22-data-tests)|true|
|`query-test`|boolean|false|true|should query tests be run[test documentation](../docs/tests.md#23-query-tests)|true|
|`commit-report`|boolean|false|true|should the reports be pushed in `.acimov/output` folder|true|
|`archive-report`|boolean|false|true|should the reports be uploaded as GitHub Artifacts in `Actions` menu|true|

Here is a second example where a the test reports are pushed only if the actions branch is `main`:

```yaml
name: model-test
on: push

env:
jobs:
  model-test:
    permissions:
      contents: write
    runs-on: ubuntu-latest
    steps:
    - run: |
        IFS='/' read -ra PATHS <<< "${{ github.ref }}"
        echo "BRANCH=$(echo ${PATHS[2]})" >> $GITHUB_ENV
    - uses: Wimmics/olivaw/test-actions@v0.0.7
      with:
        gist-secret: ${{ secrets.GIST_SECRET }}
        commit-report: ${{ env.BRANCH == github.event.repository.default_branch }}
```
