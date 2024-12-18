VERSION:str = "v0.0.7"
"""Olivaw package version"""

PIPY_OLIVAW: str = "https://pypi.org/project/olivaw"
"""Pipy base URL for an olivaw package"""

HELP_OPTION: list[str] = ["--help", "-h"]
"""Command line options to display some help"""

TEST_HELP: str = """
OLIVAW: Ontology Long-lived Integration Via ACIMOV Workflow

    Available commands: `olivaw test model`, `olivaw test data`, `olivaw test query`, `olivaw test precommit` 
              
    `olivaw test` commands are meant for testing a repository

              
    Run only in a git repository
    Repository must have been initialized with `olivaw init repo` (for more info type `olivaw init --help`)
    Tests will respect the parameters in file `PATH/.acimov.parameters.json`
    Test reports are saved in `PATH/.acimov/output/` folder, in RDF (turtle syntax) and markdown formats      
              
    For more details, see documentation about:
              
        - Command lines: https://github.com/Wimmics/olivaw/blob/main/docs/commands.md
        - Default test: https://github.com/Wimmics/olivaw/blob/main/docs/tests.md
        - Parameters file: https://github.com/Wimmics/olivaw/blob/main/docs/parameters.md
              
`olivaw test model` command
    
    Test of the project ontology fragments
              
    Following files are tested:
        
        Modules: "PATH/src/*.ttl"
        Modelets: "PATH/domains/*/*/onto.ttl"
    
    Custom model tests stored in `PATH/.acimov/custom-tests/model/` will be run
              
    Documentation about custom tests: https://github.com/Wimmics/olivaw/blob/main/docs/custom-tests.md

`olivaw test data` command
    
    Test of the project data fragments
              
    Following files are tested:
        
        Datasets: "PATH/domains/*/*/dataset.ttl"
        Use-cases: "PATH/use-cases/**/*.ttl"
    
    Custom model tests stored in `PATH/.acimov/custom-tests/data/` will be run
              
    Documentation about custom tests: https://github.com/Wimmics/olivaw/blob/main/docs/custom-tests.md
              
`olivaw test query` command
    
    Test of the project queries
              
    Following files are tested:
        
        Competency questions implementation: "PATH/domains/*/*/*.rq"

`olivaw test precommit` command

    Pre-commit hook entry point NOT meant for developpers
    
    Test the different files provided as command input depending of their resource type between:
    module, modelet, dataset, use-case, competency question
              
    Documentation about pre-commit hook: https://github.com/Wimmics/olivaw/blob/main/docs/pre-commit.md
    
"""
"""Text used as output of command `olivaw test --help`"""

INIT_HELP: str = """
OLIVAW: Ontology Long-lived Integration Via ACIMOV Workflow

    Available commands: `olivaw init repo`, `olivaw init branch`

    `olivaw init` commands initialize a repository or a branch

              
    Run only in a git repository
              
    Documentation about command lines: https://github.com/Wimmics/olivaw/blob/main/docs/commands.md
              
`olivaw init repo` command
    
    Ask some repository information to initialize the repository.

    It consists of the following:
        * Creates a `PATH/.acimov/parameters.json` file with repository information
        * Creates a gist with proper files and files content to initialize the repository badges
        * Edit the repository `README.md` file to add the badges at the top of the file
              
    Documentation about parameters file: https://github.com/Wimmics/olivaw/blob/main/docs/parameters.md

`olivaw init branch` command
    
    Update the `README.md` file to set the badges URLs to those related to the new branch


    A GitHub Composite Actions can be used to that this mechanism is performed automatically when needed

    Documentation about GitHub Composite Actions: https://github.com/Wimmics/olivaw/blob/main/docs/actions.md
"""
"""Text used as output of command `olivaw init --help`"""

SHOW_HELP: str = """
OLIVAW: Ontology Long-lived Integration Via ACIMOV Workflow

    Available commands: `olivaw show gist`, `olivaw show badges`

    `olivaw show` commands output useful information about the current repository


    These commands are meant for Olivaw GitHub Composite Actions

    Run only in a git repository
              
    For more details, see documentation about:
        * Command lines: https://github.com/Wimmics/olivaw/blob/main/docs/commands.md
        * GitHub Composite Actions: https://github.com/Wimmics/olivaw/blob/main/docs/actions.md
              
`olivaw show gist` command
    
    Show the gist id storing the badges files for the current repository that is stored in the `.acimov/parameters.json` file
              
    Documentation about the parameters file: https://github.com/Wimmics/olivaw/blob/main/docs/parameters.md

`olivaw show badges` command
    
    Show a json object containing the badges values for the current branch
"""