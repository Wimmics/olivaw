# Util folder

Provides function that can be used anywhere in the [test](../) subpackage.

Each subfolder of this project should provide explanations of the usage of each file and folder.

The files that can be found here:

* [__init__.py](./__init__.py): Executed code when the package is imported
* [draft.py](./draft.py): Provides a class that will store all the needed temporary data when preparing a test
* [encoding.py](./encoding.py): Provides some function responsible of saving a file in a way that utf-8 characters can be preserved
* [nlp.py](./nlp.py): Provides the levenshtein distance function that is used during the model test (see the [terms differenciation test](../../../docs/tests.md#215-terms-differenciation))
* [namespace.py](./namespace.py): Provides an algorithm that will compare a namespace to an index and return the most similar that can be found in the index (see the [namespace validity documentation](../../../docs/tests.md#224-namespace-validity))
* [print.py](./print.py): Provides a print function that will only print if execution mode is not GitHub Actions (see the [GitHub Actions](../../../docs/actions.md))
* [skip.py](./skip.py): Provides a function responsible of stating if the current test should be skipped or not given the project parameters (see the [parameters documentation](../../../docs/parameters.md)) 