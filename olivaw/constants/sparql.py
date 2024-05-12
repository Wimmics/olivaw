# SparQL request listing all the ontology terms not linked to a moduled by a rdfs:isDefinedBy property
NOT_REFERENCED = """
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

# SparQL request to get all the triples with their related modules, using the rdfs:isDefinedBy property 
GET_BY_MODULE = """
SELECT DISTINCT ?m where {
  ?s ?p ?o .
  ?s rdfs:isDefinedBy ?m .
}
ORDER BY ?m
"""

LINK_SUBJECTS_FOR_MODULE = """
insert {
  ?s ex:requires_description ?o .
} where {
  ?s ?p ?o .
  filter( (isblank(?s) || exists { ?s rdfs:isDefinedBy MODULE}) && isblank(?o))
}
"""

TRIPLES_FOR_MODULE = """
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

# SparQL request to get all the properties with a domain linking to a term not defined in the ontology
DOMAIN_OUT_Of_VOCABULARY = """
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
  FILTER (!(?domain = owl:Thing || strstarts(str(?domain), "ONTOLOGY_NAMESPACE")))
}
"""

# SparQL request to get all the properties with a range linking to a term not defined in the ontology
RANGE_OUT_OF_VOCABULARY = DOMAIN_OUT_Of_VOCABULARY.replace("domain", "range")

# Gets all the imports in a graph
GET_IMPORTS = """
SELECT DISTINCT ?i WHERE {
  ?s rdf:type owl:Ontology ;
  owl:imports ?i .
  FILTER(strstarts(str(?i), "ONTOLOGY_NAMESPACE"))
}
"""

# SparQL request getting all the pairs of suffixes from the ontology in a given graph
# Gets rid of the duplicates (ab and ba) and the auto pairs (aa)
GET_TERM_PAIRS = """
SELECT DISTINCT ?suffix1 ?suffix2 WHERE {
  ?s1 rdfs:isDefinedBy ?module1 .
  ?s2 rdfs:isDefinedBy ?module2 .
  FILTER(str(?s1) > str(?s2))
  BIND (SUBSTR(str(?s1), STRLEN("ONTOLOGY_NAMESPACE") + 1) as ?suffix1)
  BIND (SUBSTR(str(?s2), STRLEN("ONTOLOGY_NAMESPACE") + 1) as ?suffix2)
} ORDER BY ?suffix1
"""

NOT_LABELED = """
select distinct ?term where {
  ?term rdfs:isDefinedBy ?module .
  filter not exists {
    ?term rdfs:label ?label .
    filter(lang(?label) = "en")
  }
}
"""

GET_DETAILED_OUTCOMES = """
SELECT ?assertion ?subject ?result ?outcome ?outcomeType ?subjectId ?subjectTitle ?criterionId ?outcomeTitle ?outcomeDescription WHERE {
  ?assertion a earl:Assertion ;
  earl:result ?result ;
  earl:subject ?subject ;
  earl:test ?criterionId .

  ?subject dcterms:identifier ?subjectId ;
    dcterms:title ?subjectTitle .

  ?result earl:outcome ?outcome .
  
  ?outcome a ?outcomeType ;
    dcterms:title ?outcomeTitle ;
    dcterms:description ?outcomeDescription .
} ORDER BY DESC(?subjectId) ?criterionId
"""

SEVERITY_RANGE = [
  ("MajorFail", ":boom:", "red"),
  ("MinorFail", ":exclamation:", "orange"),
  ("CannotTell", ":warning:", "grey"),
  ("NotTested", ":grey_question:", "white"),
  ("Pass", ":white_check_mark:", "green")
]

GET_OUTCOMES_PARTS = """
SELECT DISTINCT ?subjectId ?part WHERE {
  { GET_DETAILED_ASSERTIONS }
  ?subject dcterms:hasPart ?part .
}
""".replace("GET_DETAILED_ASSERTIONS", GET_DETAILED_OUTCOMES)

GET_OUTCOME_POINTERS = """
SELECT DISTINCT ?outcome ?pointer WHERE {
  { GET_DETAILED_ASSERTIONS }
  ?outcome rdfs:seeAlso ?pointer .
}
""".replace("GET_DETAILED_ASSERTIONS", GET_DETAILED_OUTCOMES)

GET_ASSERTOR_DETAILS = """
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

GET_CRITERION_DATA = """
SELECT ?identifier ?title ?description {
  _:x a earl:TestCriterion ;
    dcterms:identifier ?identifier ;
    dcterms:title ?title ;
    dcterms:description ?description .
}
"""

IS_OWL_EL_COMPATIBLE = """
ask {
  ?assertion a earl:Assertion ;
  earl:subject ?subject ;
  earl:result ?result .
  
  ?result earl:outcome ?outcome .
  ?outcome dcterms:title ?title .
  ?outcome a earl:Pass .
  ?subject dcterms:identifier "all-modules" .
  
  FILTER(contains(?title, "OWL EL"))
}
"""

GET_ONTOLOGY_TERMS = """
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

GET_TERM_USAGE = """
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

GET_PREFIX_USAGE = """
construct {
  ?s1 ?p1 ?o1 .
  ?s2 ?p2 ?o2 .
  ?s3 ?p3 ?o3 .
}
where {
  optional {
    ?s1 ?p1 ?o1 .
    filter (strstarts(str(?s1), "PREFIX"))
    filter not exists { filter (?p1 = owl:sameAs) }
  }
  optional {
    ?s2 ?p2 ?o2 .
    filter (strstarts(str(?p2), "PREFIX"))
  }
  optional {
    ?s3 ?p3 ?o3 .
    filter (strstarts(str(?o3), "PREFIX"))
    filter not exists { filter (?p3 = owl:sameAs) }
  }
}
"""

GET_URIS = """
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

GET_VIOLATION = """
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

GET_VIOLATIONS = """
select ?o ?f ?t
{
  _:r a sh:ValidationReport ;
    sh:result ?o .
  ?o sh:focusNode ?f .
  bind( datatype(?f) == dt:triple as ?t)
}
"""

GET_CUSTOM_CRITERION_DATA = """
@prefix earl: <http://www.w3.org/ns/earl#> .
@prefix dcterms: <http://purl.org/dc/terms/> .

select ?tc ?identifier ?title ?description where {
  ?tc a earl:TestCriterion ;
    dcterms:identifier ?identifier ;
    dcterms:title ?title ;
    dcterms:description ?description
}
"""

GET_SHAPE_DESCRIPTION = """
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

GET_DECLARED_ONTOLOGIES = """
select * where {
  ?x a owl:Ontology
  filter (isuri(?x))
}
"""

GET_CRITERION_VALIDITY = """
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

GET_MAJOR_FAILS = """
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

GET_CRITERION_SUMMARY = """
select ?title ?description where {
  CRITERION a <http://www.w3.org/ns/earl#TestCriterion> ;
    <http://purl.org/dc/terms/title> ?title ;
    <http://purl.org/dc/terms/description> ?description
}
"""

ADD_VARIABLE = """
DELETE {
  ?s sh:select ?request .
}
INSERT {
  ?s sh:select ?updated_request .  
}
WHERE  {
  ?s sh:select ?request . 
  FILTER (isliteral(?request))
  BIND (concat(?request, "\\nvalues ($ontology_url) { (\\"ONTOLOGY_NAMESPACE\\") }") as ?updated_request)
}
"""

GET_ERRORS_OF_TEST = """
select ?o where {
    :CRITERION_ID :has-error ?o
}
"""

IS_OWL_QL_COMPATIBLE = IS_OWL_EL_COMPATIBLE.replace("OWL EL", "OWL QL")
IS_OWL_RL_COMPATIBLE = IS_OWL_EL_COMPATIBLE.replace("OWL EL", "OWL RL")

ADD_DESCRIPTION_LINKS = """
insert {
  ?x ex:requires_description ?y .
} where {
  ?x ?p ?y .
  filter ( (?x = <TERM>||isblank(?x)) && isblank(?y) )
}
"""

EXTRACT_STATEMENT = """
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

REMOVE_DESCRIPTION_LINKS = """
delete where { ?x ex:requires_description ?y . }
"""

GET_PREDICATE_USAGE = """
construct {
  ?x <TERM> ?y
}
where {
  ?x <TERM> ?y
}
"""

GET_OBJECT_USAGE = """
construct {
  ?x ?y <TERM>
}
where {
  ?x ?y <TERM>
}
"""

SHORTEN_LITERALS = """
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

GET_GRAPH_NAMESPACES = """
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