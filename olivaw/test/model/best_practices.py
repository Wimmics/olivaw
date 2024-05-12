from olivaw.constants import (
    GET_TERM_PAIRS,
    NOT_LABELED,
    NOT_REFERENCED,
    ONTOLOGY_NAMESPACE,
    RANGE_OUT_OF_VOCABULARY,
    TERM_DISTANCE_THRESHOLD,
    DOMAIN_OUT_Of_VOCABULARY
)

from olivaw.test.corese import query_graph
from olivaw.test.turtle import make_assertion
from olivaw.test.util import levenshtein


def best_practices_test(
        draft,
        fragment_no_import,
        fragment_no_owl,
    ):
    """Test the best practices mistakes that do not break the RDF syntax neither the OWL reasoning,
    but that should still not happen

    :param ontology: The ontology to test
    :returns: An report dictionary
    """

    # Check for terms not linked to an ontology
    if not draft.should_skip(criterion="term-referencing"):
        unlinked_subjects = query_graph(fragment_no_owl, NOT_REFERENCED)
        unlinked_subjects_pointers = [[pointer for pointer in unlinked_subjects]] if len(unlinked_subjects) else []
        unlinked_subject_messages = [f"Subject terms not linked to a module by a rdfs:isDefinedBy property"] if len(unlinked_subjects) else []
        make_assertion(
            draft(
                error="no-reference-module",
                messages=unlinked_subject_messages,
                pointers=unlinked_subjects_pointers,
                graph=fragment_no_owl
            )
        )

    if not draft.should_skip(criterion="domain-and-range-referencing"):
        # Checking for domain property out of the vocabulary
        dov = query_graph(fragment_no_import, DOMAIN_OUT_Of_VOCABULARY)
        dov = [[
            uri
            for line in dov
            for uri in line.split("\t")
        ]] if len(dov) > 0 else []
        dov_messages = ["Some properties have a domain out of the ontology"] if len(dov) > 0 else []

        make_assertion(
            draft(
                error="domain-out-of-vocabulary",
                messages=dov_messages,
                pointers=dov,
                graph=fragment_no_import
            )
        )

        # Checking for range property out of the vocabulary
        rov = query_graph(fragment_no_import, RANGE_OUT_OF_VOCABULARY)
        rov = [[
            uri
            for line in rov
            for uri in line.split("\t")
        ]] if len(rov) > 0 else []
        rov_messages = ["Some properties have a range out of the ontology"] if len(rov) > 0 else []

        make_assertion(
            draft(
                criterion="domain-and-range-referencing",
                error="range-out-of-vocabulary",
                messages=rov_messages,
                pointers=rov,
                graph=fragment_no_import
            )
        )

    # Checking for too close terms
    if not draft.should_skip(criterion="terms-differenciation"):
        term_pairs = query_graph(fragment_no_owl, GET_TERM_PAIRS)
        term_pairs = [
            [uri[1:-1] for uri in line.strip().split("\t")]
            for line in term_pairs
        ]
        term_pairs = [[
            f"<{ONTOLOGY_NAMESPACE}{uri}>"
            for pair in term_pairs
            for uri in pair
            if levenshtein(*pair) < TERM_DISTANCE_THRESHOLD
        ]]

        term_pairs = [] if len(term_pairs[0]) == 0 else term_pairs
        messages = ["Some terms are too similar"] if len(term_pairs) > 0 else []

        make_assertion(
            draft(
                error="too-close-terms",
                messages=messages,
                pointers=term_pairs,
                graph=fragment_no_owl
            )
        )

    if not draft.should_skip(criterion="labeled-terms"):
        not_labeled_terms = query_graph(fragment_no_owl, NOT_LABELED)
        not_labeled_pointers = [] if len(not_labeled_terms) == 0 else [not_labeled_terms]
        not_labeled_messages = [] if len(not_labeled_terms) == 0 else [f"The following terms have no rdfs:label to define it in natural language"]
        make_assertion(
            draft(
                error="not-labeled-term",
                messages=not_labeled_messages,
                pointers=not_labeled_pointers,
                graph=fragment_no_owl
            )
        )