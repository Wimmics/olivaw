# Model test suite

This folder contains some test scripts around the model testing.

* What is the subject of the test?
    * Only the ontology parts, so the modelets and the merged modules, in several ways:
        * The modules individually
        * The modelets individually
        * The modules with some merged terms from the modelets
        * The modules and the modelets put all together in the same graph
* When is is tested?
    * It is supposed to be partially or totally used on 3 stages
        * Manually, if the developper wants to launch the tests
        * During a commit using the pre-commit framework
        * During a GitHub Actions
* How it is tested?
    * Different tests are made on the subject:
        * Is the subject syntaxically correct?
        * Is there any undefined prefix?
        * Is the subject compatible with the following profiles, and if not, why?
            * OWL EL
            * OWL QL
            * OWL RL
            * OWL TC
        * Is there any best practices problem?
            * Domain defined out of vocabulary
            * Range defined out of vocabulary
            * Terms too close (using the Levenshtein distance metric)
            * Term not mapped to a module by a rdfs:isDefinedBy property

The test should return a turtle syntax RDF Graph.
According to the way the test was called the result can then be formatted to another format.

# Test criterions

## Syntax test

A test meant to check wether the test subject is syntaxically correct or not.

## OWL RL Constraint test

A test meant to check if there is any OWL RL constraint violation (for example a subclass of 2 disjoint classes)

## Profile test

A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.

## Best practices test

A test meant to check whether the test subject matches the Best Practices of the project or not.
There are different test cases documented there.

### Term referencing test

A test case from the Best Practices tests checking if each term of the test subject is referneced to a module through a rdfs:isDefinedBy property.

### Domain and range referencing test

A test case from the Best Practices tests checking if all the ranges and domains from the test subject point to terms that are defined in the vocabulary.

### Terms differenciation test

A test case from the Best Practices tests checking if all the terms are different enough from each other according to the Levenshtein distance metric.

# Errors

This part must list the different errors that may be detected by the script.
In the final report, a reference to one of these errors must be there, and also a complementary information providing more details of what raised this error.

## Syntax error

The turtle file provided has a syntax error. The complementary information should indicate where and why it happened.

## Unresolved prefix 

The turtle is using a prefix that is not defined. The complementary information should indicate which is the unresolved prefix.

## OWL RL Constraint Violation

The provided turtle file is valioating a OWL RL constraint. Check the complementary information to get the exact reson why.

## OWL profile error

The RDF engine checked whether the given graph was compatible with the profile and stated that it was not. The complementary information should indicate what profil was tested and a set of nodes indicating what are the incompatibilities and where.

## Domain out of vocabulary

An owl:ObjectProperty has a rdfs:domain defined out of the vocabulary. The complementary information should indicate which ObjectProperty we are talking about and which is the defined domain leading to the error.

## Range out of vocabulary

An owl:ObjectProperty has a rdfs:range defined out of the vocabulary. The complementary information should indicate which ObjectProperty we are talking about and which is the defined range leading to the error.

## Too close terms

The Levenshtein distance between two terms are lower than the parameter set for the project (see [constants](./constants.py)). The complementary information should indicate the terms leading to this error.

## No reference module

A term does not have a reference module linked by a rdfs:isDefinedBy property. The complementary information should provide the concerned term.
