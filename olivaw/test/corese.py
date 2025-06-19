"""Module providing features to support Corese-python use all over olivaw.test package"""

from queue import Queue, Empty
from threading  import Thread
from atexit import register
from subprocess import Popen, PIPE, DEVNULL
from time import sleep
from os.path import exists, sep
from typing import IO, Union, List

from py4j.java_gateway import (
    launch_gateway,
    JavaGateway,
    JavaClass,
    JavaObject,
    JavaMember
)

# Only in order to fix the not detected unbound prefix corese bug
from rdflib import Graph as RdflibGraph

from olivaw.constants import (
    GET_IMPORTS,
    CORESE_LOCAL_PATH,
    ONTOLOGY_PREFIX,
    ONTOLOGY_NAMESPACE,
    ON_POSIX,
    MODULES_TTL_GLOB_PATH,
    AST_ERROR_FORMAT,
    URI_FORMAT,
    URI_PATTERN,
    GET_DECLARED_ONTOLOGIES
)
from olivaw.test.util.print import print_title, smart_print

#####################################################
# Start the java server & capture the stderr output #
#####################################################

# Capturing the stderr in an OS-agnostic way
# From https://stackoverflow.com/questions/375427/a-non-blocking-read-on-a-subprocess-pipe-in-python

def enqueue_output(out: IO[bytes], queue: Queue) -> str:
    """Get an element of the queue containing the java console output without blocking in Windows OS

    :param out: The program standard output to capture
    :type out: `IO[bytes]`

    :param queue: The queue capturing the output
    :type queue: `Queue`

    :returns: An element of the queue
    :rtype: `str`
    """
    for line in iter(out.readline, b''):
        queue.put(line)
    out.close()


error_queue = Queue()

def get_error_line() -> str:
    """Get an output line of the java console without blocking (OS-agnotstic)

    :returns: The first line of the java console output
    :rtype: `str`
    """
    # read line without blocking
    try:
        return error_queue.get_nowait()
    except Empty:
        return ""


def get_error_output() -> str:
    """Returns The total output of the java console without blocking (OS-agnostic)

    :returns: The total output
    :rtype: `str`
    """
    total_output = []
    current_line = "a"

    while len(current_line) > 0:
        current_line = get_error_line()
        if isinstance(current_line, bytes):
            current_line = current_line.decode('utf-8')
        total_output.append(current_line)

    return "\n".join(total_output).strip()

print_title("Launching Corese")
# Start java gateway
graph_db_port = launch_gateway()
graph_db_process = Popen(
    f"java -jar -Dfile.encoding=UTF-8 -p {str(graph_db_port)}".split(" ") + [CORESE_LOCAL_PATH],
    stdout=PIPE,
    stderr=DEVNULL,
    close_fds=ON_POSIX
)
reader_thread = Thread(target=enqueue_output, args=(graph_db_process.stdout, error_queue))
reader_thread.daemon = True # thread dies with the program
reader_thread.start()

# Waiting for the java server to start up
sleep(1)
gateway = JavaGateway(
    # java process port set dynamically
    # gateway_parameters=GatewayParameters(port=launch_gateway()),
    # python call back port set dynamically
    # callback_server_parameters=CallbackServerParameters(port=0),
    # gateway to the instance of the graph DB
    java_process=graph_db_process
)
register(gateway.shutdown)

# retrieve the port on which the python callback server was bound to.
#python_port = gateway.get_callback_server().get_listening_port()

# tell the Java side to connect to the python callback server with the new
# python port. Note that java_gateway_server attribute is used and
# retrieves the GatewayServer instance.
# gateway.java_gateway_server.resetCallbackClient(
#    gateway\
#        .java_gateway_server\
#        .getCallbackClient()\
#        .getAddress(),
#    graph_db_port
#)

# Import of class
OWLProfile: JavaClass = gateway.jvm.fr.inria.corese.core.logic.OWLProfile
"""Python reference to Corese Java Class `fr.inria.corese.core.logic.OWLProfile`"""

Graph: JavaClass = gateway.jvm.fr.inria.corese.core.Graph
"""Python reference to Corese Java Class `fr.inria.corese.core.Graph`"""

Load: JavaClass = gateway.jvm.fr.inria.corese.core.load.Load
"""Python reference to Corese Java Class `fr.inria.corese.core.load.Load`"""

QueryProcess: JavaClass = gateway.jvm.fr.inria.corese.core.query.QueryProcess
"""Python reference to Corese Java Class `fr.inria.corese.core.query.QueryProcess`"""

RuleEngine: JavaClass = gateway.jvm.fr.inria.corese.core.rule.RuleEngine
"""Python reference to Corese Java Class `fr.inria.corese.core.rule.RuleEngine`"""

ResultFormat: JavaClass = gateway.jvm.fr.inria.corese.core.print.ResultFormat
"""Python reference to Corese Java Class `fr.inria.corese.core.print.ResultFormat`"""

NSManager: JavaClass = gateway.jvm.fr.inria.corese.sparql.triple.parser.NSManager
"""Python reference to Corese Java Class `fr.inria.corese.sparql.triple.parser.NSManager`"""

Property: JavaClass = gateway.jvm.fr.inria.corese.core.util.Property
"""Python reference to Corese Java Class `fr.inria.corese.core.util.Property`"""

DISABLE_OWL_AUTO_IMPORT: JavaMember = gateway.jvm.fr.inria.corese.core.util.Property.Value.DISABLE_OWL_AUTO_IMPORT
"""Python reference to Corese Java Enum Value `fr.inria.corese.core.util.Property.Value.DISABLE_OWL_AUTO_IMPORT`"""

TEXT_CSV: int = 14
"""Python reference to Corese Java Enum Value `fr.inria.corese.command.utils.format.EnumResultFormat.TEXT_CSV`"""

TEXT_TSV: int = 15
"""Python reference to Corese Java Enum Value `fr.inria.corese.command.utils.format.EnumResultFormat.TEXT_TSV`"""

TURTLE: int = 2
"""Python reference to Corese Java Enum Value `fr.inria.corese.command.utils.format.EnumResultFormat.TURTLE`"""

STD: int = gateway.jvm.fr.inria.corese.core.rule.RuleEngine.STD
"""Python reference to `public static final int fr.inria.corese.core.rule.RuleEngine.STD`"""

OWL_RL: int = gateway.jvm.fr.inria.corese.core.rule.RuleEngine.OWL_RL
"""Python reference to `public static final int fr.inria.corese.core.rule.RuleEngine.OWL_RL`"""

OWL_RL_LITE: int = gateway.jvm.fr.inria.corese.core.rule.RuleEngine.OWL_RL_LITE
"""Python reference to `public static final int fr.inria.corese.core.rule.RuleEngine.OWL_RL_LITE`"""

OWL_RL_FULL: int = gateway.jvm.fr.inria.corese.core.rule.RuleEngine.OWL_RL_FULL 
"""Python reference to `public static final int fr.inria.corese.core.rule.RuleEngine.OWL_RL_FULL`"""

RDFS_RL: int = gateway.jvm.fr.inria.corese.core.rule.RuleEngine.RDFS_RL
"""Python reference to `public static final int fr.inria.corese.core.rule.RuleEngine.RDFS_RL`"""

Query: JavaClass = gateway.jvm.fr.inria.corese.sparql.triple.parser.Query
"""Python reference to Corese Java Class `fr.inria.corese.sparql.triple.parser.Query`"""

Binding: JavaClass = gateway.jvm.fr.inria.corese.sparql.triple.parser.Binding
"""Python reference to Corese Java Class `fr.inria.corese.sparql.triple.parser.Binding`"""

Source: JavaClass = gateway.jvm.fr.inria.corese.sparql.triple.parser.Source
"""Python reference to Corese Java Class `fr.inria.corese.sparql.triple.parser.Source`"""

Service: JavaClass = gateway.jvm.fr.inria.corese.sparql.triple.parser.Service
"""Python reference to Corese Java Class `fr.inria.corese.sparql.triple.parser.Service`"""

Shacl: JavaClass =  gateway.jvm.fr.inria.corese.core.shacl.Shacl
"""Python reference to Corese Java Class `fr.inria.corese.core.shacl.Shacl`"""

TripleFormat: JavaClass = gateway.jvm.fr.inria.corese.core.print.TripleFormat
"""Python reference to Corese Java Class `fr.inria.corese.core.print.TripleFormat`"""

# A java object resolving prefixes into URIs and the other way
prefix_manager: JavaObject = NSManager.create()
"""JavaObject that is an instance of Corese Java Class `NSManager`"""

CORESE_NAMESPACES: list[tuple[str, str]] = []
"""List of Corese default prefixes and their related namespaces"""

for field in dir(NSManager):
    try:
        CORESE_NAMESPACES.append(getattr(NSManager, field))
    except:
        pass

CORESE_NAMESPACES = [
    (prefix_manager.getPrefix(uri), uri)
    for uri in CORESE_NAMESPACES
    if isinstance(uri, str)
    and len(URI_FORMAT.findall(uri)) > 0
    and not prefix_manager.getPrefix(uri) is None
] + [
    ("ex", "http://example.org/ns#")
]
CORESE_NAMESPACES = list(set(CORESE_NAMESPACES))
CORESE_NAMESPACES.sort(key=lambda item: item[0])
CORESE_NAMESPACES = {
    prefix: namespace
    for prefix, namespace in CORESE_NAMESPACES
}
CORESE_PREFIX_TEXT: str = "\n".join(
    [
        f"@prefix {prefix}: <{namespace}> ."
        for prefix, namespace in CORESE_NAMESPACES.items()
    ]
) + f"\n@prefix {ONTOLOGY_PREFIX}: <{ONTOLOGY_NAMESPACE}> ."
"""Turtle prefix definition of all the default set prefixes of Corese"""

def to_rdflib(graph: JavaObject) -> RdflibGraph:
    """Exports a Corese graph to a rdflib.Graph instance

    :param graph: The Corese Graph
    :type graph: `py4j.java_gateway.JavaObject` referencing an instance of `fr.inria.corese.core.Graph`

    :return: The rdflib equivalent Graph
    :rtype: `rdflib.Graph`
    """
    content = f"{CORESE_PREFIX_TEXT}\n{TripleFormat.create(graph).toString()}"
    g = RdflibGraph()
    g.parse(data=content, format="ttl")
    return g

def load(
        path: Union[str, list[str]],
        extras: str="",
        import_from_src: bool=True,
        disable_owl: bool=False,
        disable_import: bool=False,
        graph: JavaObject=None,
        already_imported: list[str]=[],
        ontologies: dict[str, str]={},
        profile=STD
    ) -> JavaObject:
    """Load a graph from one to several local files and/or a string.

    :param path: local path or a URL or a list of these
    :type path: `Union[str, list[str]]`

    :param extras: Some extra turtle data, default to empty string
    :type extras: `str`, optional

    :param import_from_src: Should the turtle URIs should be loaded from local project if possible, defaults to `True`
    :type import_from_src: `bool`, optional

    :param disable_owl: Should the OWL RL reasoning be disabled, defaults to `False`
    :type disable_owl: `bool`, optional

    :param disable_import: Should the loading process ignore all the `owl:imports` clauses, defaults to `False`
    :type disable_import: `bool`, optional

    :param graph: Optional graph that will be injected the turtle content, defaults to `None` and creates a new graph if not specified
    :type graph: `py4j.java_gateway.JavaObject` referencing an instance of `fr.inria.corese.core.Graph`

    :param already_imported: List of resources that already have been injected into the passed `graph` parameter, defaults to `[]`
    :type already_imported: `list[str]`

    :param ontologies: Dictionary a project ontology URI `str` to an absolute file path as `str` where to find the given ontology
    :type ontologies: `dict[str, str]`

    :param profile: Reasoning profile to apply to the graph, defaults to `STD`(0) which stands for no reasoning
    :type profile: `int`, one of `STD`(0) / `OWL_RL`(1) / `OWL_LR_LITE`(2) / `OWL_RL_EXT`(3) / `OWL_RL_TEST`(4) / `RDFS_RL`(5)

    :returns: Java Object (instance of Java Class `fr.inria.corese.core.Graph`)
    :rtype: `py4j.java_gateway.JavaObject` referencing an instance of `fr.inria.corese.core.Graph`
    """

    if isinstance(path, str):
        path = [path]

    if graph is None:
        graph = Graph()
        graph.query = query_graph.__get__(graph)
        
    if disable_owl:
        engine = RuleEngine.create(graph)
        engine.setProfile(RDFS_RL)
        engine.processWithoutWorkflow()
        engine.process()
        engine.getErrorList()

    disable_owl_import = import_from_src or disable_import or disable_owl
    Property.set(DISABLE_OWL_AUTO_IMPORT, disable_owl_import)

    ld = Load.create(graph)

    for file in path:
        if not exists(file):
            smart_print(f"File not found: {file}")
            continue
        ld.parse(file)
    
    if isinstance(extras, str):
        extras = [extras]
    
    for extra in extras:
        if len(extra) == 0:
            continue
        ld.loadString(extra, TURTLE)

    should_import_from_src = import_from_src and not disable_import and not disable_owl

    if should_import_from_src:
        imports = [
            ontologies[uri[1:-1].replace("\\/", "/")]
            if uri in ontologies else None
            for uri in query_graph(graph, GET_IMPORTS)
        ]
        imports = [
            subfile
            for subfile in imports
            if not (
                subfile is None or
                subfile in already_imported
            )
        ]
        if len(imports) == 0:
            Property.set(DISABLE_OWL_AUTO_IMPORT, False)
            return graph
        graph = load(
            imports,
            import_from_src=True,
            graph=graph,
            already_imported=already_imported + imports,
            profile=profile
        )

    if not disable_owl:
        engine = RuleEngine.create(graph)
        engine.setProfile(profile)
        engine.process()

    Property.set(DISABLE_OWL_AUTO_IMPORT, False)
    return graph

def capture_syntax_errors() -> str:
    """Captures the syntax errors that are not raised from the java console output

    :returns: A string containing the syntax errors
    :rtype: `str`
    """
    output = get_error_output()
    output_lines = output.split("\n")
    final_report = []

    for line in output_lines:
        syntax_error = AST_ERROR_FORMAT.search(line)

        if not syntax_error:
            continue

        syntax_error = syntax_error.span()
        line = line[syntax_error[1] + 3:]
        final_report.append(line)
    
    return "\n".join(final_report).strip()

def safe_load(
        fragments: Union[str, list[str]],
        extras: str="",
        import_from_src: bool=True,
        disable_import: bool=False,
        disable_owl: bool=False,
        graph=None,
        already_imported: list[str]=[],
        ontologies: dict[str, str]={},
        profile=STD
    ) -> Union[JavaObject, list[str]]:
    """Load a graph from one to several local files and/or a string.
    
    Returns a Graph if no syntax error or a list of error messages

    :param fragments: List of ontology KG resource, see `~olivaw.constants.MODULES`, `~olivaw.constants.MODELETS`, `~olivaw.constants.DATASETS`, `~olivaw.constants.USE_CASES` for more details
    :type fragments: `Union[str, list[str]]`

    :param extras: Some extra turtle data, default to empty string
    :type extras: `str`, optional

    :param import_from_src: Should the turtle URIs should be loaded from local project if possible, defaults to `True`
    :type import_from_src: `bool`, optional

    :param disable_owl: Should the OWL RL reasoning be disabled, defaults to `False`
    :type disable_owl: `bool`, optional

    :param disable_import: Should the loading process ignore all the `owl:imports` clauses, defaults to `False`
    :type disable_import: `bool`, optional

    :param graph: Optional graph that will be injected the turtle content, defaults to `None` and creates a new graph if not specified
    :type graph: `py4j.java_gateway.JavaObject` referencing an instance of `fr.inria.corese.core.Graph`

    :param already_imported: List of resources that already have been injected into the passed `graph` parameter, defaults to `[]`
    :type already_imported: `list[str]`

    :param ontologies: Dictionary a project ontology URI `str` to an absolute file path as `str` where to find the given ontology
    :type ontologies: `dict[str, str]`

    :param profile: Reasoning profile to apply to the graph, defaults to `STD`(0) which stands for no reasoning
    :type profile: `int`, one of `STD`(0) / `OWL_RL`(1) / `OWL_LR_LITE`(2) / `OWL_RL_EXT`(3) / `OWL_RL_TEST`(4) / `RDFS_RL`(5)

    :returns: Java Object (instance of Java Class `fr.inria.corese.core.Graph`) if loading process ended up successfully or a list of error messages otherwise
    :rtype: `Union[py4j.java_gateway.JavaObject, list[str]]`, the `py4j.java_gateway.JavaObject` references an instance of `fr.inria.corese.core.Graph`
    """
    
    try:
        loaded_fragments=fragments["file"] if isinstance(fragments, dict) else [fragment["file"] for fragment in fragments]
    except:
        print(fragments)
        raise

    syntax_errors = ""
    try:
        get_error_output()
        graph = load(
            loaded_fragments,
            extras=extras,
            import_from_src=import_from_src,
            disable_import=disable_import,
            disable_owl=disable_owl,
            graph=graph,
            already_imported=already_imported,
            profile=profile
        )
        syntax_errors = [
            line.strip()
            for line in capture_syntax_errors().split('\n')
            if len(line.strip()) > 0
        ]

        if len(syntax_errors) > 0:
            return syntax_errors
        
        try:
            rdflib_errors = rdflib_check(path=loaded_fragments, extras=extras)
        except:
            print(loaded_fragments)
            raise

        if len(rdflib_errors) > 0:
            return rdflib_errors
        
        return graph
    
    except Exception as e:
        return [
            message for message in [
                syntax_errors,
                " ".join(str(e).strip().split("\n")[1].split(" ")[2:]).strip()
            ]
            if len(message) > 0
        ]
    
def rdflib_check(path: Union[str, list[str]]="", extras: str="") -> list[str]:
    """Test the provided fragments into rdflib to detect some errors that Corese couldn't detect

    :param path: Local file path or list of local files, defaults to `""`
    :type path: `Union[str, list[str]]`, optional

    :param extras: Extra turtle data to also inject, defaults to `""`
    :type extras: `str`, optional

    :return: A list of error messages
    :rtype: `list[str]`
    """

    if isinstance(path, list):
        return [
            item
            for path in path
            for item in rdflib_check(path=path)
        ] + rdflib_check(extras=extras)

    rdflib_fragment = RdflibGraph()

    if isinstance(path, str) and path != "":
        try:
            rdflib_fragment.parse(path)
            return []
        except Exception as rdflib_error:
            return [rdflib_error.message]

    # Detect the last unbound prefix that corese does not detect
    try:
        rdflib_fragment.parse(data=extras, format="ttl")
        return []
    except Exception as rdflib_error:
        return [rdflib_error.message]
    
def query_graph(graph: JavaObject, query: str, format: int=TEXT_TSV) -> Union[list[str], str]:
    """Query the given Corese graph and returns the request result (`ASK` request not implemented)

    :param graph: The Corese graph to query
    :type graph: `py4j.java_gateway.JavaObject` referencing an instance of `fr.inria.corese.core.Graph`

    :param query: The SPARQL query to run
    :type query: `str`

    :param format: Expected output format, defaults to `TEXT_TSV`(15)
    :type format: `int`, optional, one of `RDFXML`(1) / `TURTLE`(2) / `TRIG`(3) / `JSONLD`(4) / `NTRIPLES`(6) / `NQUADS`(7) / `BIDING_XML`(11) / `BIDING_JSON`(13) / `TEXT_CSV`(14) / `TEXT_TSV`(15) / `TEXT_MARKDOWN`(16)  
    
    :returns: Query result, list of result lines (list[str]) or turtle data (str)
    :rtype: `Union[list[str], str]`
    """
    query_process = QueryProcess.create(graph)

    abstract_syntax_tree = query_process.compile(query).getAST()
    mappings = query_process.query(abstract_syntax_tree)

    resultFormater = ResultFormat.create(mappings)
    resultFormater.setSelectFormat(format)
    resultFormater.setConstructFormat(format)

    
    result = resultFormater.toString()
    
    if not format == TURTLE:
        result = [
            line for line in
            result.split("\n")[1:-1]
            if len(line.strip()) > 0
        ]

    return result

def export_graph(graph: JavaObject) -> str:
    """Export a Corese Graph content into RDF text

    :param graph: The Corese graph to export
    :type graph: `py4j.java_gateway.JavaObject` referencing an instance of `fr.inria.corese.core.Graph`

    :returns: RDF data (turtle syntax)
    :rtype: `str`
    """
    return  f"{CORESE_PREFIX_TEXT}\n{TripleFormat.create(graph).toString()}"

def check_OWL_constraints(graph: JavaObject) -> list[str]:
    """Detects the OWL RL logic errors from the graph (OWL RL constraint violation)

    ex: Instance of disjoint classes

    :param graph: The Corese graph to test
    :type graph: `py4j.java_gateway.JavaObject` referencing an instance of `fr.inria.corese.core.Graph`

    :returns: A list of error messages
    :rtype: `list[str]`
    """
    try:
        engine = RuleEngine.create(graph)
        engine.setProfile(OWL_RL)
        engine.processWithoutWorkflow()
        engine.process()

        # Retrieve and return the error list
        error_list = engine.getErrorList()
        return [str(error) for error in error_list]

    except Exception as e:
        # If the exception message contains 'EngineException', return the list of errors
        if 'EngineException' in str(e):
            error_list = engine.getErrorList()
            return [
                str(error_list.get(i))\
                    .replace("\n", " &#10;")\
                    .replace("<", "&#60;")\
                    .replace(">&", "> &")
                for i in range(error_list.size())
            ]
        else:
            # If the exception is of a different type, return an error message
            return [f"An error occurred while processing the graph: {e}"]

def parse_description(line: str) -> str:
    """Retrieve an error message from Corese profile detection output

    :param line: One line of Corese profile detection output
    :type line: `str`

    :returns: The error message
    :rtype: `str`
    """
    splitted = line.split('.')
    return splitted[0 if len(splitted) == 1 else 1].strip()

def profile_errors(raw_message: str) -> tuple[list[str], list[list[str]]]:
    """Parses the Corese profile detection output into error messages and turtle code snippets

    :param raw_message: The raw Corese profile detection output
    :type raw_message: `str`

    :returns: The list of different error messages and the list of their related code snippets
    :rtype: `tuple[list[str], list[list[str]]]`
    """

    descriptions = []
    pointers = []

    lines = [
        line.strip()
        for line in raw_message.split("\n")[2:]
    ]
    
    current_statement = ""
    parsing_statement = False

    for i in range(0, len(lines)):
        # Check if current statement is correct
        if parsing_statement:
            try:
                if len(current_statement) == 0 or current_statement.strip().endswith(";"):
                    raise Exception()
                if parsing_statement:
                    load([], extras=current_statement, disable_owl=True)
                    pointers.append(current_statement.strip())
                    current_statement = ""
                    parsing_statement = False
            except:
                current_statement += f"\n {lines[i]}"
                continue
        else:
                if len(current_statement) == 0:
                    current_statement = parse_description(lines[i])
                elif len(lines[i].strip()) > 0:
                    current_statement += "\n" + lines[i].strip()
                else:
                    descriptions.append(current_statement)
                    current_statement = ""
                    parsing_statement = True

    parsed = []

    for pointer in pointers:
        parsed_pointer = pointer
        for match in URI_PATTERN.findall(pointer):
            parsed_pointer = parsed_pointer.replace(match, match.replace("\\/", "/"))
        parsed.append(parsed_pointer)
        
    parsed = [[pointer + ("" if pointer.endswith(".") else " .")] for pointer in parsed]

    return descriptions, parsed