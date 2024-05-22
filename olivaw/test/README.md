# Test folder

Package responsible of managing any command starting with `olivaw test` (see the [related command line documentation](../docs/commands.md#olivaw-test))

Each subfolder of this project should provide explanations of the usage of each file and folder.

The files that can be found here:

* [__init__.py](./__init__.py): Executed code when the package is imported
* [corese.py](./corese.py): Launches a Corese java virtual machine, establish a gateway to comunicate with it, and provides functions related to Corese for all the tests from the framework (see the [test documentation](../../docs/tests.md))
* [markdown.py](./markdown.py): Provides all the needed function to generate a markdown report out of a turtle test report (see the [markdown format documentation](../../docs/tests.md#12-markdown-format))
* [olivaw-earl.ttl](./olivaw-earl.ttl): RDF dataset written in turtle specifying all the criterions of the default tests, instanciating the [EARL vocabulary](https://www.w3.org/TR/EARL10-Schema/) in olivaw context and adding some extensions that were needed for this project

The folder that can be found here:

* [data](./data/): Package that manages the `olivaw test data` command
* [generic](./generic/): Package providing tests that can be used in several test suites
* [model](./model/): Package that manages the `olivaw test model` command
* [query](./query/): Package that manages the `olivaw test query` command
* [util](./util/): Provides function that can be used anywhere in the current subpackage