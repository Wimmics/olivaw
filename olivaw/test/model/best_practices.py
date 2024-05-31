"""Package managing all the default model tests that are related to best practices"""

from py4j.java_gateway import JavaObject

from olivaw.constants import (
    GET_TERM_PAIRS,
    NOT_LABELED,
    NOT_REFERENCED,
    ONTOLOGY_NAMESPACE,
    RANGE_OUT_OF_VOCABULARY,
    TERM_DISTANCE_THRESHOLD,
    DOMAIN_OUT_OF_VOCABULARY
)

from olivaw.test.corese import query_graph
from olivaw.test.turtle import make_assertion, uri_pointer
from olivaw.test.util import levenshtein
from olivaw.test.util.draft import AssertDraft
from olivaw.test.util.skip import should_skip


def best_practices_test(
        draft: AssertDraft,
        fragment_no_import: JavaObject,
        fragment_no_owl: JavaObject,
    ) -> None:
    """Test the best practices mistakes that do not break the RDF syntax neither the OWL reasoning

    :param draft: The assertion draft containing the useful information for reporting
    :type draft: `olivaw.test.AssertDraft`

    :param fragment_no_import: Corese graph containing the fragment with `owl:imports` clauses ignored
    :type fragment_no_owl: `py4j.java_gateway.JavaObject` referencing an instance of `fr.inria.corese.core.Graph`

    :param fragment_no_owl: Corese graph containing the fragment without any owl reasoning
    :type fragment_no_owl: `py4j.java_gateway.JavaObject` referencing an instance of `fr.inria.corese.core.Graph`
    """

    # Check for terms not linked to an ontology
    if not should_skip(draft, criterion="term-referencing"):
        unlinked_subjects = query_graph(fragment_no_owl, NOT_REFERENCED)
        unlinked_subjects_pointers = [
            [
                uri_pointer(draft(graph=fragment_no_owl), pointer)
                for pointer in unlinked_subjects
            ]
        ] if len(unlinked_subjects) else []
        unlinked_subject_messages = [f"Subject terms not linked to a module by a rdfs:isDefinedBy property"] if len(unlinked_subjects) else []
        make_assertion(
            draft,
            error="no-reference-module",
            messages=unlinked_subject_messages,
            pointers=unlinked_subjects_pointers
        )

    if not should_skip(draft, criterion="domain-and-range-referencing"):
        # Checking for domain property out of the vocabulary
        dov = query_graph(fragment_no_import, DOMAIN_OUT_OF_VOCABULARY)
        dov = [[
            uri_pointer(draft(graph=fragment_no_import), uri)
            for line in dov
            for uri in line.split("\t")
        ]] if len(dov) > 0 else []
        dov_messages = ["Some properties have a domain out of the ontology"] if len(dov) > 0 else []

        make_assertion(
            draft,
            error="domain-out-of-vocabulary",
            messages=dov_messages,
            pointers=dov
        )

        # Checking for range property out of the vocabulary
        rov = query_graph(fragment_no_import, RANGE_OUT_OF_VOCABULARY)
        rov = [[
            uri_pointer(draft(graph=fragment_no_import), uri)
            for line in rov
            for uri in line.split("\t")
        ]] if len(rov) > 0 else []
        rov_messages = ["Some properties have a range out of the ontology"] if len(rov) > 0 else []

        make_assertion(
            draft,
            criterion="domain-and-range-referencing",
            error="range-out-of-vocabulary",
            messages=rov_messages,
            pointers=rov
        )

    # Checking for too close terms
    if not should_skip(draft, criterion="terms-differenciation"):
        term_pairs = query_graph(fragment_no_owl, GET_TERM_PAIRS)
        term_pairs = [
            [uri[1:-1] for uri in line.strip().split("\t")]
            for line in term_pairs
        ]
        term_pairs = [[
            uri_pointer(draft(graph=fragment_no_owl), f"<{ONTOLOGY_NAMESPACE}{uri}>")
            for pair in term_pairs
            for uri in pair
            if levenshtein(*pair) < TERM_DISTANCE_THRESHOLD
        ]]

        term_pairs = [] if len(term_pairs[0]) == 0 else term_pairs
        messages = ["Some terms are too similar"] if len(term_pairs) > 0 else []

        make_assertion(
            draft,
            error="too-close-terms",
            messages=messages,
            pointers=term_pairs
        )

    if not should_skip(draft, criterion="labeled-terms"):
        not_labeled_terms = query_graph(fragment_no_owl, NOT_LABELED)
        not_labeled_pointers = [] if len(not_labeled_terms) == 0 else [
            [
                uri_pointer(draft(graph=fragment_no_owl), uri)
                for uri in not_labeled_terms
            ]
        ]
        not_labeled_messages = [] if len(not_labeled_terms) == 0 else ["The following terms have no rdfs:label to define it in natural language"]
        make_assertion(
            draft,
            error="not-labeled-term",
            messages=not_labeled_messages,
            pointers=not_labeled_pointers
        )