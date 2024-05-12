from queue import Queue, Empty
from sys import builtin_module_names
from threading  import Thread
from atexit import register
from subprocess import Popen, PIPE, DEVNULL
from time import sleep
from os.path import exists, sep
from typing import Union, List
from py4j.java_gateway import launch_gateway, JavaGateway

# Only in order to fix the not detected unbound prefix corese bug
from rdflib import Graph as RdflibGraph

from olivaw.constants import (
    AST_ERROR_FORMAT,
    GET_IMPORTS,
    ONTOLOGY_SEPARATOR,
    CORESE_LOCAL_PATH,
    PWD_TO_ROOT_FOLDER,
    URI_FORMAT,
    ONTOLOGY_PREFIX,
    ONTOLOGY_NAMESPACE
)
from olivaw.test.util.print import print_title, smart_print

#####################################################
# Start the java server & capture the stderr output #
#####################################################

# Capturing the stderr in an OS-agnostic way
# From https://stackoverflow.com/questions/375427/a-non-blocking-read-on-a-subprocess-pipe-in-python

def enqueue_output(out, queue):
    """Get an element of the queue containing the java console output
    ... Without blocking in Windows OS

    :param out: The output to capture
    :param queue: The queue capturing the output
    :returns: An element of the queue
    """
    for line in iter(out.readline, b''):
        queue.put(line)
    out.close()


ON_POSIX = 'posix' in builtin_module_names
error_queue = Queue()

def get_error_line():
    """Get an output line of the java console without blocking (OS-agnotstic)

    :returns: The first line of the java console output
    """
    # read line without blocking
    try:
        return error_queue.get_nowait()
    except Empty:
        return ""


def get_error_output():
    """Returns The total output of the java console without blocking (OS-agnotstic)

    :returns: The total output
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
    # gateway to our instance of the graph DB
    java_process=graph_db_process
)
register(gateway.shutdown)

# retrieve the port on which the python callback server was bound to.
#python_port = gateway.get_callback_server().get_listening_port()

# tell the Java side to connect to the python callback server with the new
# python port. Note that we use the java_gateway_server attribute that
# retrieves the GatewayServer instance.
# gateway.java_gateway_server.resetCallbackClient(
#    gateway\
#        .java_gateway_server\
#        .getCallbackClient()\
#        .getAddress(),
#    graph_db_port
#)

# Import of class
OWLProfile = gateway.jvm.fr.inria.corese.core.logic.OWLProfile
Graph = gateway.jvm.fr.inria.corese.core.Graph
Load = gateway.jvm.fr.inria.corese.core.load.Load
QueryProcess = gateway.jvm.fr.inria.corese.core.query.QueryProcess
RuleEngine = gateway.jvm.fr.inria.corese.core.rule.RuleEngine
ResultFormat = gateway.jvm.fr.inria.corese.core.print.ResultFormat
NSManager = gateway.jvm.fr.inria.corese.sparql.triple.parser.NSManager
property_manager = gateway.jvm.fr.inria.corese.core.util.Property
DISABLE_OWL_AUTO_IMPORT = gateway.jvm.fr.inria.corese.core.util.Property.Value.DISABLE_OWL_AUTO_IMPORT
TEXT_CSV = 14
TEXT_TSV = 15
TURTLE = 2

STD = gateway.jvm.fr.inria.corese.core.rule.RuleEngine.STD
OWL_RL = gateway.jvm.fr.inria.corese.core.rule.RuleEngine.OWL_RL
OWL_RL_LITE = gateway.jvm.fr.inria.corese.core.rule.RuleEngine.OWL_RL_LITE
OWL_RL_FULL = gateway.jvm.fr.inria.corese.core.rule.RuleEngine.OWL_RL_FULL 
RDFS = gateway.jvm.fr.inria.corese.core.rule.RuleEngine.RDFS_RL

Query = gateway.jvm.fr.inria.corese.sparql.triple.parser.Query
Binding = gateway.jvm.fr.inria.corese.sparql.triple.parser.Binding
Source = gateway.jvm.fr.inria.corese.sparql.triple.parser.Source
Service = gateway.jvm.fr.inria.corese.sparql.triple.parser.Service

Shacl =  gateway.jvm.fr.inria.corese.core.shacl.Shacl
TripleFormat = gateway.jvm.fr.inria.corese.core.print.TripleFormat

# A java object resolving prefixes into URIs and the other way
prefix_manager = NSManager.create()

CORESE_NAMESPACES = []
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
CORESE_PREFIX_TEXT = f"@prefix {ONTOLOGY_PREFIX}: <{ONTOLOGY_NAMESPACE}> .\n".join(
    [
        f"@prefix {prefix}: <{namespace}> ."
        for prefix, namespace in CORESE_NAMESPACES.items()
    ]
)

def to_rdflib(graph):
    content = f"{CORESE_PREFIX_TEXT}\n{TripleFormat.create(graph).toString()}"
    g = RdflibGraph()
    g.parse(data=content, format="ttl")
    return g

def load(
        path: Union[str, List[str], Graph],
        extras: str="",
        import_from_src: bool=True,
        disable_owl: bool=False,
        disable_import: bool=False,
        graph=None,
        already_imported: List[str]=[],
        profile=STD
    ):
    """Load a graph from a local file or a URL

    :param path: local path or a URL or a list of these
    :param extras: raw string in n3 notation containing extra triples
    :returns: the graph load
    """
    if isinstance(path, str):
        path = [path]

    if graph is None:
        graph = Graph()
        graph.query = query_graph.__get__(graph)
        
    if disable_owl:
        engine = RuleEngine.create(graph)
        engine.setProfile(RDFS)
        engine.processWithoutWorkflow()
        engine.process()
        engine.getErrorList()

    disable_owl_import = import_from_src or disable_import or disable_owl
    property_manager.set(DISABLE_OWL_AUTO_IMPORT, disable_owl_import)

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
        imports = query_graph(graph, GET_IMPORTS)
        imports = [
            f"{PWD_TO_ROOT_FOLDER}src{sep}{item.split(ONTOLOGY_SEPARATOR)[-1][:-1]}.ttl"
            for item in imports
        ]
        imports = [item for item in imports if not item in already_imported]
        if len(imports) == 0:
            property_manager.set(DISABLE_OWL_AUTO_IMPORT, False)
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

    property_manager.set(DISABLE_OWL_AUTO_IMPORT, False)
    return graph

def capture_syntax_errors():
    """Captures the syntax errors that are not raised from the java console output

    :returns: A raw string containing the syntax errors
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
        path: Union[str, List[str], Graph],
        extras: str="",
        import_from_src: bool=True,
        disable_import: bool=False,
        disable_owl: bool=False,
        graph: Graph=None,
        already_imported: List[str]=[],
        profile=STD
    ):
    """Safe method to load a graph and eventually catch the error if there is one

    :param path: local path or a URL or a list of these
    :param extras: raw string in n3 notation containing extra triples
    :returns: A graph if it succeeds, an error report if it doesn't
    """
    syntax_errors = ""
    try:
        get_error_output()
        graph = load(
            path,
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
        
        rdflib_errors = rdflib_check(path=path, extras=extras)

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
    
def rdflib_check(path="", extras=""):
    if isinstance(path, list):
        return [
            item
            for path in path
            for item in rdflib_check(path=path)
        ] + rdflib_check(extras=extras)

    file_content = ""

    if isinstance(path, str) and path != "":
        with open(path, "r") as fragment_file:
            file_content = fragment_file.read()

    content = file_content if len(file_content) > 0 else extras

    if content == "":
        return []

    # Detect the last unbound prefix that corese does not detect
    try:
        rdflib_fragment = RdflibGraph()
        rdflib_fragment.parse(data=content, format="ttl")
        return []
    except Exception as rdflib_error:
        return [rdflib_error.message]
    
def query_graph(graph, query, format=TEXT_TSV):
    """Query the given graph and return the result in TSV notation

    :param graph: The Corese graph to query
    :param query: The SparQL query
    :returns: A string containing the result in TSV notation
    """
    query_process = QueryProcess.create(graph)

    abstract_syntax_tree = query_process.compile(query).getAST()
    mappings = query_process.query(abstract_syntax_tree)

    resultFormater = ResultFormat.create(mappings)
    resultFormater.setSelectFormat(format)
    resultFormater.setConstructFormat(format)

    
    result = resultFormater.toString()
    
    if not format == TURTLE:
        result = result.split("\n")[1:-1]

    return result

def export_graph(graph):
    return  f"{CORESE_PREFIX_TEXT}\n{TripleFormat.create(graph).toString()}"

def check_OWL_constraints(graph):
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

def parse_description(line):
    splitted = line.split('.')
    return splitted[0 if len(splitted) == 1 else 1].strip()

def profile_errors(raw_message):

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

    pointers = [[pointer] for pointer in pointers]

    return descriptions, pointers