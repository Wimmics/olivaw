"""Module providing useful functions for saving files with proper encodings"""

from codecs import open as copen
from datetime import datetime
from os import makedirs
from os.path import exists, sep, abspath

from rdflib import (
    BNode,
    Graph,
    Literal,
    URIRef,
    IdentifiedNode
)

from rdflib.namespace import PROV, XSD, RDF

from olivaw.constants import (
    MODE,
    DEV_USERNAME,
    PWD_TO_OUTPUT_FOLDER,
    OLIVAW_NAMESPACE
)

def datetime_id() -> None:
    """Generate a datetime part for a file generation"""
    return ".".join(
            datetime\
            .now()\
            .isoformat()\
            .split(".")[:-1]
        ).replace(":", "-")


def file_name(test_type: str) -> str:
    """Returns the file name for a file generation

    :param test_type: The test type
    :type test_type: `str`, one of `"model"`, `"data"` or `"query"`

    :returns: A file name
    :rtype: `str`
    """
    suffix = MODE.lower() if not MODE == "manual" else f"{MODE}-{DEV_USERNAME}-{datetime_id()}"
    name = f"{test_type}-test-{suffix}"
    return name

def save(path: str, content: str) -> None:
    """Save the provided content with proper codec, in the provided path

    :param path: The file path
    :type path: `str`

    :param content: The file content
    :type content: `str`
    """
    if not exists(PWD_TO_OUTPUT_FOLDER):
        makedirs(PWD_TO_OUTPUT_FOLDER)
    with copen(f"{path}", "w", "utf-8") as f:
        f.write(content)

def save_reports(name: str, assertor: IdentifiedNode, report: Graph, markdown: str) -> None:
    """Saves the provided turtle and markdown reports

    :param name: The desired report file path
    :type name: `str`

    :param assertor: The node representing the test assertor
    :type assertor: `rdflib.IdentifiedNode`

    :param report: The RDF graph containing the test report
    :type report: `rdflib.Graph`

    :param markdown: The markdown report
    :type markdown: `str`
    """
    path = f"{PWD_TO_OUTPUT_FOLDER}{name}"

    turtle_report_uri = URIRef(f"file:///{abspath(path).replace(sep, '/')}.ttl")
    markdown_report_uri = URIRef(f"file:///{abspath(path).replace(sep, '/')}.md")

    turtle_generation = BNode("turtleGeneration")
    markdown_generation = BNode("markdownGeneration")

    activity_end_time = datetime.now()

    for triple in [
        # Add end time of activity and generated files
        (assertor, PROV.endedAtTime, Literal(activity_end_time, datatype=XSD.dateTime)),
        (assertor, PROV.generated, turtle_report_uri),
        (assertor, PROV.generated, markdown_report_uri),
        # Adding turtle file generation
        (turtle_report_uri, RDF.type, PROV.Entity),
        (turtle_report_uri, PROV.generatedAtTime, Literal(activity_end_time, datatype=XSD.dateTime)),
        (turtle_report_uri, PROV.qualifiedGeneration, turtle_generation),
        # Qualifying turtle file generation
        (turtle_generation, RDF.type, PROV.Generation),
        (turtle_generation, PROV.activity, assertor),
        (turtle_generation, OLIVAW_NAMESPACE.generatedAs, OLIVAW_NAMESPACE.turtle_report),
        # Adding markdown file generation
        (markdown_report_uri, RDF.type, PROV.Entity),
        (markdown_report_uri, PROV.generatedAtTime, Literal(activity_end_time, datatype=XSD.dateTime)),
        (markdown_report_uri, PROV.qualifiedGeneration, markdown_generation),
        # Qualifying markdown file generation
        (markdown_generation, RDF.type, PROV.Generation),
        (markdown_generation, PROV.activity, assertor),
        (markdown_generation, OLIVAW_NAMESPACE.generatedAs, OLIVAW_NAMESPACE.markdown_report)
    ]:
        report.add(triple)

    save(f"{path}.ttl", report.serialize(format="ttl"))
    save(f"{path}.md", markdown)