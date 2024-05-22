# Test actions

This actions does the following:

* Launching the model tests and generate reports if asked
* Launching the data tests and generate reports if asked
* Launching the query tests and generate reports if asked
* Commit the report in the `.acimov/output` folder if asked
* Uploading Github Artifacts for the markdown reports, if asked. You can access in the Actions menu for a month
* Updating the badges values

Each test step can generate both turtle file report and markdown files, see the [turtle format documentation](../docs/tests.md#11-turtle-format) and the [markdown format documentation](../docs/tests.md#12-markdown-format)

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
```

Here is a summary of the available parameters:

|Parameter|Type|Required|Default|Description|Example|
|---------|----|--------|-------|-----------|-------|
|`repository`|string|true||reference to your repository like `your_organization/your_repository`|`${{ github.repository }}`|
|`ref`|string|true||reference to which branch you are pushing|`${{ github.ref }}`|
|`gist-secret`|string|true||personnal access token with the `gist` scope to update the gist files|`${{ secrets.GIST_SECRET }}`|
|`model-test`|boolean|false|true|should model tests be run, check the [test documentation](../docs/tests.md#21-model-tests)|true|
|`data-test`|boolean|false|true|should data tests be run, check the [test documentation](../docs/tests.md#22-data-tests)|true|
|`query-test`|boolean|false|true|should query tests be run[test documentation](../docs/tests.md#23-query-tests)|true|
|`commit-report`|boolean|false|true|should the reports be pushed in `.acimov/output` folder|true|
|`archive-report`|boolean|false|true|should the reports be uploaded as GitHub Artifacts in `Actions` menu|true|
|`server-url`|string|false|`https://github.com`|URL of the server|`https://github.com`|

Here is a second example where we want a commit of the test reports only if the push was made on the `main` branch:

```yaml
name: model-test
on: push

env:
  MAIN: 'main'
jobs:
  model-test:
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
        echo "BRANCH=$(echo ${BRANCH_NAME})" >> $GITHUB_ENV
    - uses: Wimmics/olivaw/test-actions@test-actions-8
      with:
        repository: ${{ github.repository }}
        ref: ${{ github.ref }}
        gist-secret: ${{ secrets.GIST_SECRET }}
        commit-report: ${{ env.BRANCH == env.MAIN }}
```