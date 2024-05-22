# Model folder

Package that manages the `olivaw test model` command.

Each subfolder of this project should provide explanations of the usage of each file and folder.

The files that can be found here:

* [__init__.py](./__init__.py): Executed code when the package is imported
* [best_practices.py](./best_practices.py): Provides the script that will apply all hte tests related to the best practice, which are `term-referencing`, `domain-and-range-referencing`, `terms-differenciation`, `labeled-terms`(see the [available tests documentation](../../../docs/tests.md#21-model-tests))
* [suite.py](./suite.py): Script launched by the entry point when the command `olivaw test model` is type in the terminal (see the [model test documentation](../../../docs/tests.md#21-model-tests))
* [testing.py](./testing.py): Provides all the high-level functions needed to perform a model test