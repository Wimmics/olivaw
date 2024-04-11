# SparQL request listing all the ontology terms not linked to a moduled by a rdfs:isDefinedBy property
NOT_REFERENCED = """
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

SELECT DISTINCT ?s where {
  ?s ?p ?o .
  FILTER(strstarts(str(?s), "ONTOLOGY_URL"))
  FILTER NOT EXISTS { ?s rdfs:isDefinedBy [] . }
  FILTER NOT EXISTS { ?s rdf:type owl:Ontology . }
  FILTER NOT EXISTS { ?s rdf:type skos:Concept . }
  FILTER NOT EXISTS { FILTER ( str(?s) =  "ONTOLOGY_URL" ) }
}
"""

# SparQL request to get all the triples with their related modules, using the rdfs:isDefinedBy property 
GET_BY_MODULE = """
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

SELECT DISTINCT ?m where {
  ?s ?p ?o .
  ?s rdfs:isDefinedBy ?m .
  FILTER(strstarts(str(?s), "ONTOLOGY_URL"))
}
ORDER BY ?m
"""

TRIPLES_FOR_MODULE = """
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

construct {
  ?s ?p ?o .
} where {
  ?s ?p ?o .
  ?s rdfs:isDefinedBy MODULE .
}
"""

# SparQL request to get all the properties with a domain linking to a term not defined in the ontology
DOMAIN_OUT_Of_VOCABULARY = """
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

SELECT DISTINCT ?suffix ?domain WHERE {
  # Get all the properties with a defined domain
  ?property rdf:type owl:ObjectProperty ;
    rdfs:domain ?domain ;
    rdfs:isDefinedBy [] .

  # Get only the most specialized domains for each property
  FILTER NOT EXISTS {
    ?property rdfs:domain ?domain2 .
    ?domain2 owl:subClassOf ?domain .
  }

  # Ignore the owl:Thing domains
  FILTER NOT EXISTS {
    FILTER (?domain = owl:Thing)
  }
  
  # Ignore the domains in the ontology
  FILTER NOT EXISTS {
    #?domain rdf:type ?o .
    FILTER(strstarts(str(?domain), "ONTOLOGY_URL"))
  }
  
  # Ignore the properties out of the ontology
  FILTER(strstarts(str(?property), "ONTOLOGY_URL"))

  # Format the result
  BIND (SUBSTR(str(?property), STRLEN("ONTOLOGY_URL") + 1) as ?suffix)
}
"""

# SparQL request to get all the properties with a range linking to a term not defined in the ontology
RANGE_OUT_OF_VOCABULARY = DOMAIN_OUT_Of_VOCABULARY.replace("domain", "range")

# Gets all the imports in a graph
GET_IMPORTS = """
SELECT DISTINCT ?i WHERE {
  ?s rdf:type owl:Ontology ;
  owl:imports ?i .
  FILTER(strstarts(str(?i), "ONTOLOGY_URL"))
}
"""

# Not used for now... a LDScript implementation of the Levenshtein distance
# Works on Corese command but not on GUI
LEVENSHTEIN_FUNCTION = """
function fun:levenshtein(x, y) {
  if (strlen(x) = 0) {
    return (strlen(y))
  }
  else {
    if (strlen(y) = 0) {
      return (strlen(x))
    }
    else {
      let (
        x0 = substr(x, 1, 1),
        y0 = substr(y, 1, 1),
        indicator = if(x0 = y0, 0, 1),
        subx = substr(x, 2),
        suby = substr(y, 2)
      ) {
        return (
          fun:min(
            xt:list (
              fun:levenshtein(subx, y) + 1,
              fun:levenshtein(suby, x) + 1,
              fun:levenshtein(subx, suby) + indicator
            ),
            0,
            0
          )
        )
      }
    }
  }
}

function fun:min(list, i, currentMin) {
  if (i = 0) {
    return (
      fun:min(list, i + 1, xt:get(list, 0))
    )
  }
  else {
    if (i >= xt:size(list)) {
      return (currentMin)
    }
    else {
      let (currentElement = xt:get(list, i)) {
        if (currentElement < currentMin) {
          return (fun:min(list, i + 1, currentElement))
        }
        else {
          return (fun:min(list, i + 1, currentMin))
        }
      }
    }
  }
}
"""

# SparQL request getting all the pairs of suffixes from the ontology in a given graph
# Gets rid of the duplicates (ab and ba) and the auto pairs (aa)
GET_TERM_PAIRS = """
SELECT DISTINCT ?suffix1 ?suffix2 WHERE {
  ?s1 ?p1 [] .
  ?s2 ?p2 [] .
  FILTER(strstarts(str(?s1), "ONTOLOGY_URL"))
  FILTER(strstarts(str(?s2), "ONTOLOGY_URL"))
  FILTER(str(?s1) > str(?s2))
  BIND (SUBSTR(str(?s1), STRLEN("ONTOLOGY_URL") + 1) as ?suffix1)
  BIND (SUBSTR(str(?s2), STRLEN("ONTOLOGY_URL") + 1) as ?suffix2)
  FILTER(strlen(?suffix1) > 0)
  FILTER(strlen(?suffix2) > 0)
} ORDER BY ?suffix1
"""

# Not used for now
# Gets the pairs of suffixes in the given graph and gives all the pairs of terms that are too similar
GET_TOO_CLOSED_PAIRS = """
SELECT ?suffix1 ?suffix2 ?distance WHERE {
  {
    GET_TERM_PAIRS
  }
  BIND(fun:levenshtein(?suffix1, ?suffix2) AS ?distance)
  FILTER(?distance > TERM_DISTANCE_THRESHOLD)
}
""".replace(
    "GET_TERM_PAIRS",
    GET_TERM_PAIRS
  ) + LEVENSHTEIN_FUNCTION

NOT_LABELED = """
select distinct ?suffix where {
  ?term ?p [] .
  FILTER(strstarts(str(?term), "ONTOLOGY_URL"))
  FILTER NOT EXISTS {
    ?term rdfs:label ?label .
    FILTER(lang(?label) = "en")
  }
  BIND(substr(str(?term), strlen("ONTOLOGY_URL") + 1) AS ?suffix)
  FILTER(strlen(?suffix) > 0)
}
"""

FAIL_ASSERTIONS = """
select ?n ?c ?t ?d where {
  ?a a earl:Assertion ;
  earl:subject ?s ;
  earl:test ?c ;
  earl:result ?r .

  ?s dcterms:title ?n .

  ?r a earl:TestResult ;
  earl:outcome ?o .

  ?o a earl:Fail ;
  dcterms:title ?t ;
  dcterms:description ?d .
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
    filter (strstarts(str(?s), "ONTOLOGY_URL"))
    bind (SUBSTR(str(?s), STRLEN("ONTOLOGY_URL") + 1) as ?term)
  }
  union
  {
    ?s ?p ?o .
    filter (strstarts(str(?p), "ONTOLOGY_URL"))
    bind (SUBSTR(str(?p), STRLEN("ONTOLOGY_URL") + 1) as ?term)
  }
  union
  {
    ?s ?p ?o .
    filter (strstarts(str(?o), "ONTOLOGY_URL"))
    bind (SUBSTR(str(?o), STRLEN("ONTOLOGY_URL") + 1) as ?term)
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

GET_CRITERION_IDENTIFIER = """
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix earl: <http://www.w3.org/ns/earl#> .

select ?id where {
  _:ns a earl:TestCriterion ;
  dcterms:identifier ?id
}
"""

GET_CRITERION_URI = """
@prefix earl: <http://www.w3.org/ns/earl#> .

select ?tc where {
    ?tc a earl:TestCriterion
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

?outcome a olivaw-earl:MinorFail ;
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

IS_OWL_QL_COMPATIBLE = IS_OWL_EL_COMPATIBLE.replace("OWL EL", "OWL QL")
IS_OWL_RL_COMPATIBLE = IS_OWL_EL_COMPATIBLE.replace("OWL EL", "OWL RL")