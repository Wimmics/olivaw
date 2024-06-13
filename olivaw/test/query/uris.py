"""Module providing the functions needed for exploring a Corese SPARQL request AST"""

from py4j import java_gateway
from py4j.java_gateway import JavaObject

from olivaw.test.corese import (
    gateway,
    Query,
    Binding,
    Source,
    Service,
    Graph,
    QueryProcess
)

def retrieveFromMathExpression(term: JavaObject) -> list[str]:
    """Retrieves the URIs form a Corese Sparql request AST math expression

    :param term: Corese SPARQL AST math expression
    :type term: `py4j.java_gateway.JavaObject` referencing an instance of `fr.inria.corese.sparql.triple.parser.Expression`

    :returns: A list of URIs
    :rtype: `list[str]`
    """
    if term.isExist():
        return [
            element
            for i in range(term.getExist().size())
            for element in retrieveFromBody(term.getExist().get(i))
        ]
    else:
        return [
            element
            for i in range(term.getArity())
            for element in retrieveFromMathExpression(term.getArg(i))
        ]
            
def retrieveFromLeaf(leaf: JavaObject) -> list[str]:
    """Retrieve the URIs from a Corese SPARQL request AST Atom

    :param leaf: The Corese SPARQL request AST Atom
    :type leaf: `py4j.java_gateway.JavaObject` referencing an instance of `fr.inria.corese.sparql.triple.parser.Atom`

    :returns: A list of URIs
    :rtype: `list[str]`
    """
    if leaf.isURI():
        return [ leaf.getLongName() ]
    else:
        return []
        
def retrieveFromBody(body: JavaObject) -> list[str]:
    """Retrieve the URIs from a Corese SPARQL request AST Exp iterable

    :param leaf: The Corese SPARQL request AST Exp iterable
    :type leaf: `py4j.java_gateway.JavaObject` referencing an instance of `Iterable<fr.inria.corese.sparql.triple.parser.Exp>`

    :returns: A list of URIs
    :rtype: `list[str]`
    """
    if java_gateway.is_instance_of(gateway, body, Query):
        return retrieveFromBody(body.getBody())

    retrievedValues = []
    for i in range(body.size()):
        item = body.get(i)
        if item.isTriple():
            
            triple = item.getTriple()

            retrievedValues += retrieveFromLeaf(triple.getSubject()) + \
                    retrieveFromLeaf(triple.getPredicate()) + \
                    retrieveFromLeaf(triple.getObject())

        elif item.isBGP() or item.isQuery():
            retrievedValues += retrieveFromBody(item)
        elif item.isUnion():
            retrievedValues += [
                element
                for i in range(item.size())
                for element in retrieveFromBody(item.get(i))
            ]

        elif item.isMinus() or item.isOptional():
            retrievedValues += retrieveFromBody(item.get(0)) + retrieveFromBody(item.get(1))

        elif item.isFilter():
            retrievedValues += retrieveFromMathExpression(item.getFilter())

        elif java_gateway.is_instance_of(gateway, item, Binding):
            retrievedValues += retrieveFromLeaf(item.getVariable()) + retrieveFromMathExpression(item.getFilter())

        elif java_gateway.is_instance_of(gateway, item, Source) or java_gateway.is_instance_of(gateway, item, Service):
            retrievedValues += retrieveFromLeaf(item.getSource()) + retrieveFromBody(item.getBody())
    return retrievedValues

def retrieveURIFromQuery(query: str) -> list[str]:
    """Retrieve the URIs from a Corese SPARQL request

    :param leaf: The Corese SPARQL request
    :type leaf: `str`

    :returns: A list of URIs
    :rtype: `list[str]`
    """
    graph = Graph()
    query_process = QueryProcess.create(graph)
    ast = query_process.ast(query)

    return list(set(retrieveFromBody(ast.getBody())))