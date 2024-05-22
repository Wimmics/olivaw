# Hook folder

Package responsible of managing the pre-commit hook (see the [pre-commit documentation](../docs/pre-commit.md)).

Each subfolder of this project should provide explanations of the usage of each file and folder.

The files that can be found here:

* [__init__.py](./__init__.py): Executed code when the package is imported
* [test.py](./test.py): Script that will be executed by the entry point when the pre-commit hook triggers (see the [pre-commit hook documentation](../../docs/pre-commit.md))