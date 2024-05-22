# Olivaw folder

The technical documentation of the project begins there.

Each subfolder of this project should provide explanations of the usage of each file and folder.

The files that can be found here:

* [__init__.py](./__init__.py): Executed code when the package is imported
* [main.py](./main.py): Entry point of the program. The `run()` method will be execution each time a command beggning by `olivaw` will be type in the terminal

The folders that can be found here:

* [constants](./constants/): Package aggregating the constants from the framework itself and the parameters from the `.acimov/parameters.json` (check the [parameters.json documentation](../docs/parameters.md)) to provide constants that can be used anywhere in the framework
* [hook](./hook/): Package responsible of managing the pre-commit hook (see the [pre-commit documentation](../docs/pre-commit.md))
* [init](./init/): Package responsible of managing any command starting with `olivaw init` (see the [related command line documentation](../docs/commands.md#olivaw-init))
* [show](./show/): Package responsible of managing any command starting with `olivaw show` (see the [related command line documentation](../docs/commands.md#olivaw-show))
* [test](./test/): Package responsible of managing any command starting with `olivaw test` (see the [related command line documentation](../docs/commands.md#olivaw-test))