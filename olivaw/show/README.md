# Show folder

Package responsible of managing any command starting with `olivaw show` (see the [related command line documentation](../docs/commands.md#olivaw-show)).

Each subfolder of this project should provide explanations of the usage of each file and folder.

The files that can be found here:

* [__init__.py](./__init__.py): Executed code when the package is imported
* [badges.py](./badges.py): Script that will be executed by the entry point when command `olivaw show badges` is typed in the terminal
* [gist.py](./gist.py): Script that will be executed by the entry point when command `olivaw show gist` is typed in the terminal

The folder that can be found here:

* [util](./util/): Provides function that can be used anywhere in the current subpackage.