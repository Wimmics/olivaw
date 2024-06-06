# Branch initialization

The actions will then proceed as follows:

* Read the values of the badges of the parent branch and store these values
* Update the README.md to replace the gist files URLs
* Create new gist files meant for that branch with the stored badges values

Create a `init-branch.yaml` file in the `.github/workflows` folder containing this:

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

Here is a summary of the available parameters:

|Parameter|Type|Required|Default|Description|Example|
|---------|----|--------|-------|-----------|-------|
|`repository`|string|true||reference to the repository like `organization/repository`|`${{ github.repository }}`|
|`ref`|string|true||reference to which branch was pushed|`${{ github.ref }}`|
|`gist-secret`|string|true||personnal access token with the `gist` scope to update the gist files|`${{ secrets.GIST_SECRET }}`|
|`server-url`|string|false|`https://github.com`|URL of the server|`https://github.com`|