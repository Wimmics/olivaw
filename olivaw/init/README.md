# Init folder

Package responsible of managing any command starting with `olivaw init` (see the [related command line documentation](../docs/commands.md#olivaw-init)).

Each subfolder of this project should provide explanations of the usage of each file and folder.

The files that can be found here:

* [__init__.py](./__init__.py): Executed code when the package is imported
* [branch.py](./branch.py): Script that will be executed by the entry point when command `olivaw test branch` is typed in the terminal
* [readme.py](./readme.py): Script responsible of updating the main `README.md` file when the commands `olivaw test repo` or `olivaw test branch` are typed in a terminal
* [repo.py](./repo.py): Script that will be executed by the entry point when command `olivaw test repo` is typed in the terminal

The folder that can be found here:

* [util](./util/): provides function that can be used anywhere in the current subpackage
