from py4j import java_gateway

from olivaw.test.corese import (
    gateway,
    Query,
    Binding,
    Source,
    Service,
    Graph,
    QueryProcess
)

def retrieveFromMathExpression(term):
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
            
def retrieveFromLeaf(leaf):
    if leaf.isURI():
        return [ leaf.getLongName() ]
    else:
        return []
        
def retrieveFromBody(body):
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

def retrieveURIFromQuery(query):
    graph = Graph()
    query_process = QueryProcess.create(graph)
    ast = query_process.ast(query)

    return list(set(retrieveFromBody(ast.getBody())))