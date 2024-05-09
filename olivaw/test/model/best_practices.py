from olivaw.constants import (
    GET_TERM_PAIRS,
    NOT_LABELED,
    NOT_REFERENCED,
    ONTOLOGY_URL,
    RANGE_OUT_OF_VOCABULARY,
    TERM_DISTANCE_THRESHOLD,
    DOMAIN_OUT_Of_VOCABULARY,
    SKIPPED_TESTS
)

from olivaw.test.corese import query_graph
from olivaw.test.turtle import make_assertion
from olivaw.test.util.nlp import levenshtein


def best_practices_test(
        draft,
        fragment_wih_import,
        fragment_no_import,
        fragment_no_owl,
        skip=[]
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
        draft.make_assertion(
            error="no-reference-module",
            messages=unlinked_subject_messages,
            pointers=unlinked_subjects_pointers,
            graph=fragment_no_owl
        )

    if not draft.should_skip(criterion="domain-and-range-referencing"):
        # Checking for domain property out of the vocabulary
        dov = query_graph(fragment_no_import, DOMAIN_OUT_Of_VOCABULARY)
        dov = [line.split("\t") for line in dov]
        dov_messages = [
            f"The property :{item[0][1:-1]} has a domain out of the ontology: {item[1]}"
            for item in dov
        ]
        dov_pointers = [[f"<{ONTOLOGY_URL}{item[0][1:-1]}>" for item in dov]]
        dov_pointers = dov_pointers if len(dov_pointers[0]) > 0 else []

        draft.make_assertion(
            error="domain-out-of-vocabulary",
            messages=dov_messages,
            pointers=dov_pointers,
            graph=fragment_no_import
        )

        # Checking for range property out of the vocabulary
        rov = query_graph(fragment_no_import, RANGE_OUT_OF_VOCABULARY)
        rov = [line.split("\t") for line in rov]
        rov_messages = ["Some properties have a range out of the ontology"] if len(rov) > 0 else []
        rov_pointers = [[f"<{ONTOLOGY_URL}{item[0][1:-1]}>" for item in rov]]
        rov_pointers = rov_pointers if len(rov_pointers[0]) > 0 else []
        draft.make_assertion(
            criterion="domain-and-range-referencing",
            error="range-out-of-vocabulary",
            messages=rov_messages,
            pointers=rov_pointers,
            graph=fragment_no_import
        )

    # Checking for too close terms
    if not draft.should_skip(criterion="terms-differenciation"):
        term_pairs = query_graph(fragment_no_owl, GET_TERM_PAIRS)
        term_pairs = [[
                f"<{ONTOLOGY_URL}{item.strip()[1:-1]}>"
                for item in line.split("\t")
            ]
            for line in term_pairs
        ]
        term_pairs = [pair for pair in term_pairs if levenshtein(*pair) < TERM_DISTANCE_THRESHOLD]
        term_pairs = [[
            pair_item
            for pair in term_pairs
            for pair_item in pair
        ]]
        term_pairs = [] if len(term_pairs[0]) == 0 else term_pairs

        messages = ["Some terms are too similar"] if len(term_pairs) > 0 else []

        draft.make_assertion(
            error="too-close-terms",
            messages=messages,
            pointers=term_pairs,
            graph=fragment_no_owl
        )

    if not draft.should_skip(criterion="labeled-terms"):
        not_labeled_terms = query_graph(fragment_no_owl, NOT_LABELED)
        not_labeled_pointers = [] if len(not_labeled_terms) == 0 else [not_labeled_terms]
        not_labeled_messages = [] if len(not_labeled_terms) == 0 else [f"The following terms have no rdfs:label to define it in natural language"]
        draft.make_assertion(
            error="not-labeled-term",
            messages=not_labeled_messages,
            pointers=not_labeled_pointers,
            graph=fragment_no_owl
        )