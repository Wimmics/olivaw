# Generic folder

Package providing tests that can be used in several test suites

Each subfolder of this project should provide explanations of the usage of each file and folder.

The files that can be found here:

* [__init__.py](./__init__.py): Executed code when the package is imported
* [prefix.py](./prefix.py): Responsible of running the `prefix-validity` test (see the [prefix-validity documentation](../../../docs/tests.md#224-prefix-validity))
* [shacl.py](./shacl.py): Responsible of running the custom tests (see the [custom tests documentation](../../../docs/custom-tests.md))
* [uri.py](./uri.py): Responsible of running the `uri-validity` test (see the [prefix-validity documentation](../../../docs/tests.md#233-uri-validity))