# Constants folder

Package aggregating the constants from the framework itself and the parameters from the `.acimov/parameters.json` (check the [parameters.json documentation](../docs/parameters.md)) to provide constants that can be used anywhere in the framework

Each subfolder of this project should provide explanations of the usage of each file and folder.

The files that can be found here:

* [__init__.py](./__init__.py): Executed code when the package is imported, responsible of the aggregation between the [parameters.json file](../../docs/parameters.md) with the internal olivaw constants
* [badges.py](./badges.py): All the default content of the gist responsible of storing the badges data
* [corese_info.py](./corese_info.py): Provides constants that are useful for launching the Corese java virtual machine and parse Corese errors
* [error-resources.json](./error-resources.json): Stores all the useful constants concerning the different errors that can be detected by olivaw
* [git_info.py](./git_info.py): Provides all the needed information about the git information needed to perform all the tests properly. These information are gathered by git command lines but can be overrided if needed (check the [command line documentation](../../docs/commands.md))
* [markdown.py](./markdown.py): Provides some constants that are used during the markdown format generation (see the [markdown documentation](../../docs/tests.md#12-markdown-format))
* [olivaw.py](./olivaw.py): Some constants related to olivaw framework itself
* [paths.py](./paths.py): A set of folder and file paths that are used to search for files within the acimov project
* [prefixcc.py](./prefixcc.py): Some constants useful when preparing an index of the known web semantic namespaces known by the website prefix.cc
* [rdflib_info](./rdflib_info.py): Some constants that are usefule in order to make the turtle test report format (see the [turtle format documentation](../../docs/tests.md#11-turtle-format))
* [sparql.py](./sparql.py): A set of SPARQL requests that are useful all over the project
* [uri_index.json](./uri_index.json): An index of all the common namespaces available in prefix.cc, in order to check for namespaces that may be similar to well known other namespaces
* [uris.py](./uris.py): Some URIs that can be useful all over the project
* [regex.py](./regex.py): Some import regexes for the project