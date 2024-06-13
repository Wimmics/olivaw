"""Module providing SPARQL requests"""

from typing import List

NOT_REFERENCED: str = """
SELECT DISTINCT ?s where {
  ?s ?p ?o .
  FILTER(
    strstarts(str(?s), "ONTOLOGY_NAMESPACE") &&
    strlen(?s) > strlen("ONTOLOGY_NAMESPACE")
  )
  FILTER NOT EXISTS { ?s rdfs:isDefinedBy ?m . }
  FILTER NOT EXISTS { ?s rdf:type owl:Ontology . }
  FILTER NOT EXISTS { ?s rdf:type skos:Concept . }
}
"""
"""SPARQL request listing all the ontology terms not linked to a moduled by a rdfs:isDefinedBy property"""

GET_BY_MODULE: str = """
SELECT DISTINCT ?m where {
  ?s ?p ?o .
  ?s rdfs:isDefinedBy ?m .
}
ORDER BY ?m
"""
"""SPARQL request to get all the triples with their related modules, using the rdfs:isDefinedBy property """

LINK_SUBJECTS_FOR_MODULE: str = """
insert {
  ?s ex:requires_description ?o .
} where {
  ?s ?p ?o .
  filter( (isblank(?s) || exists { ?s rdfs:isDefinedBy MODULE}) && isblank(?o))
}
"""
"""Request adding links that will allow to extract the content of a modelet that is related to a given module"""

TRIPLES_FOR_MODULE: str = """
construct {
  ?s ?p ?o .
} where {
  {
    select ?s where {
      ?x rdfs:isDefinedBy MODULE ;
        ex:requires_description* ?s .
    }
  }
  ?s ?p ?o .
  filter (?p != ex:requires_description)
}
"""
"""Request extracting the content of a modelet for a given module"""

DOMAIN_OUT_OF_VOCABULARY: str = """
SELECT DISTINCT ?property ?domain WHERE {
  # Get all the properties with a defined domain
  ?property rdf:type owl:ObjectProperty ;
    rdfs:domain ?domain ;
    rdfs:isDefinedBy [] .

  # Get only the most specialized domains for each property
  FILTER NOT EXISTS {
    ?property rdfs:domain ?domain2 .
    ?domain2 owl:subClassOf ?domain .
  }

  # Ignore the owl:Thing domains and domains in the ontology
  FILTER (!(isblank(?domain) || ?domain = owl:Thing || strstarts(str(?domain), "ONTOLOGY_NAMESPACE")))
}
"""
"""SPARQL request to get all the properties with a domain linking to a term not defined in the ontology"""

RANGE_OUT_OF_VOCABULARY: str = DOMAIN_OUT_OF_VOCABULARY.replace("domain", "range")
"""SPARQL request to get all the properties with a range linking to a term not defined in the ontology"""

GET_IMPORTS: str = """
SELECT DISTINCT ?i WHERE {
  ?s rdf:type owl:Ontology ;
  owl:imports ?i .
  FILTER(strstarts(str(?i), "ONTOLOGY_NAMESPACE"))
}
"""
"""Gets all the imports in a graph"""

GET_TERM_PAIRS: str = """
SELECT DISTINCT ?suffix1 ?suffix2 WHERE {
  ?s1 rdfs:isDefinedBy ?module1 .
  ?s2 rdfs:isDefinedBy ?module2 .
  FILTER(str(?s1) > str(?s2))
  BIND (SUBSTR(str(?s1), STRLEN("ONTOLOGY_NAMESPACE") + 1) as ?suffix1)
  BIND (SUBSTR(str(?s2), STRLEN("ONTOLOGY_NAMESPACE") + 1) as ?suffix2)
} ORDER BY ?suffix1
"""
"""SPARQL request getting all the pairs of suffixes from the ontology in a given graph and 
gets rid of the duplicates (ab and ba) and the auto pairs (aa)"""

NOT_LABELED: str = """
select distinct ?term where {
  ?term rdfs:isDefinedBy ?module .
  filter not exists {
    ?term rdfs:label ?label .
    filter(lang(?label) = "en")
  }
}
"""
"""Request getting the ontology term that are not labeld with a rdfs:label property poiting to a literal in English"""

GET_DETAILED_OUTCOMES: str = """
SELECT ?assertion ?subject ?result ?outcome ?outcomeType ?subjectId ?subjectTitle ?criterionId ?outcomeTitle ?outcomeDescription ?outcomeId WHERE {
  ?assertion a earl:Assertion ;
  earl:result ?result ;
  earl:subject ?subject ;
  earl:test ?criterionId .

  ?subject dcterms:identifier ?subjectId ;
    dcterms:title ?subjectTitle .

  ?result earl:outcome ?outcome .
  
  ?outcome a ?outcomeType ;
    dcterms:identifier ?outcomeId ;
    dcterms:title ?outcomeTitle ;
    dcterms:description ?outcomeDescription .
} ORDER BY DESC(?subjectId) ?criterionId
"""
"""Get all the data that is related to each outcome"""

SEVERITY_RANGE: List[tuple[str, str, str]] = [
  ("MajorFail", ":boom:", "red"),
  ("MinorFail", ":exclamation:", "orange"),
  ("CannotTell", ":warning:", "grey"),
  ("NotTested", ":grey_question:", "white"),
  ("Pass", ":white_check_mark:", "green")
]
"""List of severities with their related emojis and colors"""

GET_OUTCOMES_PARTS: str = """
SELECT DISTINCT ?subjectId ?part WHERE {
  { GET_DETAILED_ASSERTIONS }
  ?subject dcterms:hasPart ?part .
}
""".replace("GET_DETAILED_ASSERTIONS", GET_DETAILED_OUTCOMES)
"""Retrieve the parts related to the subject of an outcome"""

GET_OUTCOME_POINTERS: str = """
SELECT DISTINCT ?outcome ?pointer WHERE {
  { GET_DETAILED_ASSERTIONS }
  ?outcome earl:info|earl:pointer ?pointer .
}
""".replace("GET_DETAILED_ASSERTIONS", GET_DETAILED_OUTCOMES)
"""Retrieve the pointers related to an outcome"""

GET_ASSERTOR_DETAILS: str = """
SELECT ?title ?description ?date ?script ?page WHERE {
  ?account a foaf:OnlineAccount ;
  dcterms:title ?title ;
  dcterms:description ?description ;
  dcterms:date ?date ;
  foaf:member ?script ;
  earl:mainAssertor _:assertor .

  _:assertor schema:mainEntityOfPage ?page .
} LIMIT 1
"""
"""Retrieve the information related to the assertor of a test report"""

GET_CRITERION_DATA: str = """
SELECT ?identifier ?title ?description {
  _:x a earl:TestCriterion ;
    dcterms:identifier ?identifier ;
    dcterms:title ?title ;
    dcterms:description ?description .
}
"""
"""Retrieve the information of the criterion of a olivaw-earl TestCriterion"""

IS_OWL_EL_COMPATIBLE: str = """
select ?parsed {
  ?assertion a earl:Assertion ;
  earl:subject ?subject ;
  earl:test olivaw-earl:profile-compatibility ;
  earl:result ?result .
  
  ?subject dcterms:identifier "all-modules"  .

  ?result earl:outcome ?outcome .

  ?outcome a ?status ;
    dcterms:title ?title .

  filter(contains(?title, "OWL EL")) .
  bind(
    replace(
      str(?status),
      "^(([^:/?#\\\\s]+):)(\\\\/\\\\/([^/?#\\\\s]*))?([^?#\\\\s]*)(\\\\?([^#\\\\s]*))?(#(.*))?#",
      ""
    ) as ?parsed
  )
}
"""
"""Check if the model test report can state if the ontology is OWL EL compatible"""

GET_ONTOLOGY_TERMS: str = """
select distinct ?term where {
  {
    ?s ?p ?o .
    filter (strstarts(str(?s), "ONTOLOGY_NAMESPACE"))
    bind (SUBSTR(str(?s), STRLEN("ONTOLOGY_NAMESPACE") + 1) as ?term)
  }
  union
  {
    ?s ?p ?o .
    filter (strstarts(str(?p), "ONTOLOGY_NAMESPACE"))
    bind (SUBSTR(str(?p), STRLEN("ONTOLOGY_NAMESPACE") + 1) as ?term)
  }
  union
  {
    ?s ?p ?o .
    filter (strstarts(str(?o), "ONTOLOGY_NAMESPACE"))
    bind (SUBSTR(str(?o), STRLEN("ONTOLOGY_NAMESPACE") + 1) as ?term)
  }
}
"""
"""Retrieve the terms from the fragments that are namespaced in the ontology"""

GET_TERM_USAGE: str = """
construct {
  ?s1 ?p1 ?o1 .
  ?s2 ?p2 ?o2 .
  ?s3 ?p3 ?o3 .
}
where {
  optional {
    ?s1 ?p1 ?o1 .
    filter (str(?s1)= "TERM")
    filter not exists { filter (?p1 = owl:sameAs) }
  }
  optional {
    ?s2 ?p2 ?o2 .
    filter (str(?p2)= "TERM")
  }
  optional {
    ?s3 ?p3 ?o3 .
    filter (str(?o3)= "TERM")
    filter not exists { filter (?p3 = owl:sameAs) }
  }
}
"""
"""Retrieve the usage of a given ontology term in the fragment"""

GET_NAMESPACE_USAGE: str = """
construct {
  ?s1 ?p1 ?o1 .
  ?s2 ?p2 ?o2 .
  ?s3 ?p3 ?o3 .
}
where {
  optional {
    ?s1 ?p1 ?o1 .
    filter (strstarts(str(?s1), "NAMESPACE"))
    filter not exists { filter (?p1 = owl:sameAs) }
  }
  optional {
    ?s2 ?p2 ?o2 .
    filter (strstarts(str(?p2), "NAMESPACE"))
  }
  optional {
    ?s3 ?p3 ?o3 .
    filter (strstarts(str(?o3), "NAMESPACE"))
    filter not exists { filter (?p3 = owl:sameAs) }
  }
}
"""
"""Retrieve the usage of a namespace in the fragment"""

GET_URIS: str = """
select ?uri where {
  {
    ?uri ?p1 ?o1 .
  }
  union
  {
    ?s2 ?uri ?o2 .
  }
  union
  {
    ?s3 ?p3 ?uri .
  }
  filter not exists { filter isblank(?uri) }
  filter not exists { filter isliteral(?uri) }
}
"""
"""Retrieve the URIs that are used in the fragment"""

GET_VIOLATION: str = """
CONSTRUCT {
  VIOLATION_URI ?p ?po
}
WHERE {
  VIOLATION_URI ?p ?o
  bind (
    if (
      isliteral(?o) && strlen(?o) > 60 && datatype(?o) != dt:triple,
      concat(substr(?o, 1, 60), "..."),
      ?o
    ) as ?po
  )
}
"""
"""Get the information related to a violation in a ShaCL report"""

GET_VIOLATIONS: str = """
select ?o ?f ?t
{
  _:r a sh:ValidationReport ;
    sh:result ?o .
  ?o sh:focusNode ?f .
  bind( datatype(?f) == dt:triple as ?t)
}
"""
"""List the violations that can be found in a ShaCL report"""

GET_CUSTOM_CRITERION_DATA: str = """
@prefix earl: <http://www.w3.org/ns/earl#> .
@prefix dcterms: <http://purl.org/dc/terms/> .

select ?tc ?identifier ?title ?description where {
  ?tc a earl:TestCriterion ;
    dcterms:identifier ?identifier ;
    dcterms:title ?title ;
    dcterms:description ?description
}
"""
"""Retrieve the criterion data in a custom test"""

GET_SHAPE_DESCRIPTION: str = """
construct {
  ?s ?p ?o
}
where {
  ?s ?p ?o
  filter not exists {
    ?s a earl:TestCriterion
  }
}
"""
"""Retrieve all the ShaCL data from a criterion"""

GET_DECLARED_ONTOLOGIES: str = """
select * where {
  ?x a owl:Ontology
  filter (isuri(?x))
}
"""
"""Retrieve the declared ontologies from a fragment"""

GET_CRITERION_VALIDITY: str = """
@prefix earl: <http://www.w3.org/ns/earl#> .
@prefix dcterms: <http://purl.org/dc/terms/> .

select 
  ?identifier
  ?unique_criterion
	?good_prefix
	?title_cardinality_check
	?title_type_check
	?description_cardinality_check
	?description_type_check
	?identifier_cardinality_check
	?identifier_type_check
	?identifier_format_check
	 where {
  {
    select distinct ?criterion (count(?criterion) as ?criterion_number) {
      ?criterion a earl:TestCriterion .
    }
  }

  {
    select ?identifier (count(?identifier) as ?nidentifier) where {
      ?criterion dcterms:identifier ?identifier
    }
  }

  {
    select ?title (count(?title) as ?ntitle) where {
      ?criterion dcterms:title ?title
    }
  }

  {
    select ?description (count(?description) as ?ndescription) where {
      ?criterion dcterms:description ?description
    }
  }

  bind(?criterion_number == 1 as ?unique_criterion)
  bind(strstarts(?criterion, "FILE_URI") as ?good_prefix)
  bind(?ntitle == 1 as ?title_cardinality_check)
  bind(?ndescription == 1 as ?description_cardinality_check)
  bind(?nidentifier == 1 as ?identifier_cardinality_check)
  bind(isliteral(?title) as ?title_type_check)
  bind(isliteral(?description) as ?description_type_check)
  bind(isliteral(?identifier) as ?identifier_type_check)
  bind(regex(?identifier, "^([a-z]+(-[a-z]+)*){1}$") as ?identifier_format_check)
}
"""
"""SPARQL request that check if a custom test was declared properly"""

GET_MAJOR_FAILS: str = """
select ?subject_title ?criterion ?error_title ?error_description  where {
  ?assertion a earl:Assertion ;
    earl:subject ?subject ;
    earl:test ?criterion ;
    earl:result ?result .

?subject dcterms:title ?subject_title .

?result a earl:TestResult ;
    earl:outcome ?outcome .

?outcome a olivaw-earl:MajorFail ;
    dcterms:title ?error_title ;
    dcterms:description ?error_description .
}
"""
"""Retrieve the information from any MajorFail outcome of a report"""

GET_CRITERION_SUMMARY: str = """
select ?title ?description where {
  CRITERION a <http://www.w3.org/ns/earl#TestCriterion> ;
    <http://purl.org/dc/terms/title> ?title ;
    <http://purl.org/dc/terms/description> ?description
}
"""
"""Retrieve the minimal data from a criterion"""

ADD_VARIABLE: str = """
DELETE {
  ?s sh:select ?request .
}
INSERT {
  ?s sh:select ?updated_request .  
}
WHERE  {
  ?s sh:select ?request . 
  FILTER (isliteral(?request))
  BIND (concat(?request, "\\nvalues ($ontology_namespace) { (\\"ONTOLOGY_NAMESPACE\\") }\\n") as ?updated_request)
}
"""
"""Update the SPARQL request in a custom test to add the variable $ontology_namespace"""

GET_ERRORS_OF_TEST: str = """
select ?o where {
    :CRITERION_ID :has-error ?o
}
"""
"""Retrieve the possible error that can occur during a given test"""

IS_OWL_QL_COMPATIBLE: str = IS_OWL_EL_COMPATIBLE.replace("OWL EL", "OWL QL")
"""SPARQL request that checks if the ontology is OWL QL compatible"""

IS_OWL_RL_COMPATIBLE: str = IS_OWL_EL_COMPATIBLE.replace("OWL EL", "OWL RL")
"""SPARQL request that checks if the ontology is OWL RL compatible"""

ADD_DESCRIPTION_LINKS: str = """
insert {
  ?x ex:requires_description ?y .
} where {
  ?x ?p ?y .
  filter ( (?x = <TERM>||isblank(?x)) && isblank(?y) )
}
"""
"""Request that adds links that are useful for creating a code snippet"""

EXTRACT_STATEMENT: str = """
construct { ?s ?p ?parsed } where {
  {
    select ?s where {
      <TERM> ex:requires_description* ?s .
    }
  }
  ?s ?p ?o
  filter (?p != ex:requires_description)
  bind(
    if(
      isliteral(?o) && strlen(?o) > 60,
       concat(substr(?o, 1, 60), "..."),
       ?o
      ) as ?parsed
  )
}
"""
"""Extract the triples that are useful to create a code snippet"""

REMOVE_DESCRIPTION_LINKS: str = """
delete where { ?x ex:requires_description ?y . }
"""
"""Remove some description links that are created for code snippet extraction"""

GET_PREDICATE_USAGE: str = """
construct {
  ?x <TERM> ?y
}
where {
  ?x <TERM> ?y
}
"""
"""Retrieve the usage of a given predicate in the fragment"""

GET_OBJECT_USAGE: str = """
construct {
  ?x ?y <TERM>
}
where {
  ?x ?y <TERM>
}
"""
"""Retrieve the usage of a given object in the fragment"""

SHORTEN_LITERALS: str = """
construct {?s ?p ?parsed}
where {
  ?s ?p ?o .
  bind(
    if(
      isliteral(?o) && strlen(?o) > 60,
       concat(substr(?o, 1, 60), "..."),
       ?o
      ) as ?parsed
  )
}
"""
"""Request to shorten the literals when creating a code snippet"""

GET_GRAPH_NAMESPACES: str = """
select distinct ?result where {
  {select ?uri where {?uri ?u ?v}}
  union {select ?uri where {?a ?uri ?c}}
  union {select ?uri where {?d ?e ?uri}}
  filter (isuri(?uri))
  bind (replace(?uri, "^(([^:/?#]+):)?(//([^/?#]*))?([^?#]*)(\\\\?([^#]*))?(#(.*))?[#/=]", "") as ?suffix)
  bind (substr(?uri, 1, strlen(?uri) - strlen(?suffix)) as ?prefix)
  bind (
    if (
      substr(?prefix, strlen(?prefix) - 2) = "://",
      str(?uri),
      ?prefix
    ) as ?result
  )
}
"""
"""Retrieve the different namespaces that are used in a fragment"""