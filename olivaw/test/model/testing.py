from glob import glob
from os.path import sep, relpath, abspath
from tqdm import tqdm

from olivaw.test.corese import (
    query_graph, 
    safe_load,
    prefix_manager,
    owl_profile,
    check_OWL_constraints,
    profile_errors
)
from olivaw.constants import (
    GET_BY_MODULE,
    NOT_REFERENCED,
    ONTOLOGY_SEPARATOR,
    DOMAIN_OUT_Of_VOCABULARY,
    RANGE_OUT_OF_VOCABULARY,
    GET_TERM_PAIRS,
    TERM_DISTANCE_THRESHOLD,
    DECIDABILITY_RANGE,
    ONTOLOGY_URL,
    PWD_TO_ROOT_FOLDER,
    MODEL_BEST_PRACTICES_TESTS,
    MODEL_BEST_PRACTICES_TESTS,
    NOT_LABELED,
    SKIPPED_TESTS,
    SKIPPED_FILES,
    MODE
)

from olivaw.test.turtle import (
    make_subject,
    make_not_tested,
    make_outcomes,
    make_assertion,
    assemble_assertion,
    make_result
)


def group_terms_by_module(modelet):
    """Get all the triples that has a subject included in the ontology.
    Group all of these triples by module (using rdfs:isDefinedBy property)

    :param modelet: Corese graph containing the modelet
    :returns: A dictionary of n3 for each module to be merged with the given n3
    """
    tsv = query_graph(modelet, GET_BY_MODULE)

    grouped_triples = {}

    for line in tsv:
        cut_line = line.split('\t')
        module = cut_line[0][1:-1].split(ONTOLOGY_SEPARATOR)[-1]
        triple = []

        for element in cut_line[1:]:
            uri = ""
            # Resolve the URI if the element is prefixed
            if not element[0] in ['<', '"', "'"]:
                prefix = element.split(":")[0]
                base_url = prefix_manager.getNamespace(prefix)
                uri = f"<{base_url}{element[len(prefix)+1:]}>"
            else:
                uri = element
            triple.append(uri)

        triple = " ".join(triple) + " ."

        if not module in grouped_triples:
            grouped_triples[module] = triple
        else:
            grouped_triples[module] += "\n" + triple

    return grouped_triples

def profile_check(
        fragment,
        report,
        assertor,
        subject,
        skip_pass=False,
        not_tested=False
    ):
    """Returns a report about whether an ontology is compatible with each profile and if not, why

    :param ontology: Corese graph containing the modelet
    :param extra: string in n3 notation, additional triples to add to the graph
    :returns: A dictionary with a key for each profile containing itself another dictionary
    with a key "is_reached" mapping a boolean indicating a compatibility, and a "message" justifying the result
    """

    engine = owl_profile(fragment)

    results = []

    for decidability_level in DECIDABILITY_RANGE:
        if "profile-compatibility" in SKIPPED_TESTS:
            break

        # Keeping 2 arrays containing almost the same thing was not necessary, so getattr
        profile = getattr(owl_profile, decidability_level)
        compatible = engine.process(profile)
        raw_message = engine.getMessage()
        engine.setMessage("")
        error_id = f"{decidability_level.lower().replace('_', '-')}-profile-error"
        messages, pointers = [], []
        if not compatible:
            messages, pointers = profile_errors(raw_message)
        results += make_outcomes(
            report,
            subject,
            "profile-compatibility",
            error_id,
            messages,
            pointers=pointers,
            skip_pass=skip_pass
        )
    
    if not "profile-compatibility" in SKIPPED_TESTS:
        assemble_assertion(
            report,
            assertor,
            subject,
            "profile-compatibility",
            make_result(
                report,
                results,
                skip_pass=skip_pass,
                not_tested=not_tested,
            ),
            skip_pass=skip_pass,
            tested_only=not_tested
        )

    # Check for respect for OWL constraints
    if not "owl-rl-constraint" in SKIPPED_TESTS:
        make_assertion(
            report,
            assertor,
            subject,
            "owl-rl-constraint",
            "owl-rl-constraint-violation",
            check_OWL_constraints(fragment),
            skip_pass=skip_pass,
            tested_only=not_tested
        )

def fragment_check(
        fragments,
        report,
        assertor,
        subject,
        extras="",
        skip=[],
        skip_pass=False,
        tested_only=False
    ):

    fragment_no_import = safe_load(
        fragments,
        extras,
        disable_import=True
    )
    no_import_load_error = isinstance(fragment_no_import, list)

    if no_import_load_error:
        make_assertion(
            report,
            assertor,
            subject,
            "syntax",
            "syntax-error",
            fragment_no_import,
            skip_pass=skip_pass,
            tested_only=tested_only
        )
        
        for criterion_id in MODEL_BEST_PRACTICES_TESTS:
            make_not_tested(
                report,
                assertor,
                subject,
                criterion_id,
                tested_only=tested_only
            )
        return True
    
    fragment_with_import = safe_load(fragments, extras)
    with_import_load_error = isinstance(fragment_with_import, list)

    profile_check(
        fragment_no_import,
        report,
        assertor,
        subject,
        skip_pass=skip_pass,
        not_tested=tested_only
    )

    if with_import_load_error:
        for criterion in MODEL_BEST_PRACTICES_TESTS:
            make_not_tested(
                report,
                assertor,
                subject,
                criterion,
                tested_only=tested_only
            )
        return True
    
    fragment_no_owl = safe_load(fragments, extras, disable_owl=True)

    best_practices_test(
        report,
        assertor,
        subject,
        fragment_with_import,
        fragment_no_import,
        fragment_no_owl,
        skip,
        skip_pass=skip_pass
    )
    
    return False

def modules_tests(
        glob_path,
        report,
        assertor,
        skip_pass=False,
        tested_only=False
    ):
    """Returns a report about of a profile check of a set of ontologies

    :param glob_path: A glob-format path string
    :returns: A dictionary of reports, the keys are the file paths
    """
    modules = glob(glob_path) if isinstance(glob_path, str) else glob_path

    if len(modules) == 0:
        return []
    
    unsafe_modules = []

    for module in tqdm(modules, disable=MODE=="actions"):
        module_key = relpath(module, PWD_TO_ROOT_FOLDER).replace(sep, "/")
        subject = make_subject(report, [module_key])
        load_error = fragment_check(
            module,
            report,
            assertor,
            subject,
            skip_pass=skip_pass,
            tested_only=tested_only
        )

        if load_error:
            unsafe_modules.append(module)

    return unsafe_modules

def modelets_tests(
        glob_path,
        report,
        assertor,
        skip_merge_test=False,
        skip_pass=False,
        tested_only=False
    ):
    """Test of the modelets
    Test them individually, and then checks how each module behave
    when merged with their related terms in the modelets

    :param glob_path: A glob-format path string
    :returns: A dictionary of reports
    """

    modelets = glob(glob_path) if isinstance(glob_path, str) else glob_path

    if len(modelets) == 0:
        return []

    unsafe_modelets = []

    for modelet in tqdm(modelets, disable=MODE=="actions"):
        if "template" in modelet:
            continue

        modelet_key = relpath(modelet, PWD_TO_ROOT_FOLDER).replace(sep, "/")
        standalone_subject = make_subject(report, [modelet_key])

        load_error = fragment_check(
            modelet,
            report,
            assertor,
            standalone_subject,
            skip=["domain-and-range-referencing"],
            skip_pass=skip_pass,
            tested_only=tested_only
        )

        if load_error:
            unsafe_modelets.append(modelet)
            continue

        if skip_merge_test:
            continue
        
        # Add each triple of the modelet to their related ontology, then proceed to profile checks
        alone_no_owl = safe_load(
            modelet,
            disable_owl=True
        )

        moduled_triples = group_terms_by_module(alone_no_owl)

        for module in moduled_triples.keys():
            module_key = f"src/{module}.ttl"
            module_path = f"{PWD_TO_ROOT_FOLDER}{module_key}"

            if abspath(module_path) in SKIPPED_FILES:
                continue

            merged_subject = make_subject(report, [module_key], [modelet_key])

            fragment_check(
                module_path,
                report,
                assertor,
                merged_subject,
                extras=moduled_triples[module],
                skip_pass=skip_pass,
                tested_only=tested_only
            )

    return unsafe_modelets

def levenshtein(s1, s2):
    """Returns the levenshtein distance between two trings
    Algorithm borrowed from https://en.wikibooks.org/wiki/Algorithm_Implementation/Strings/Levenshtein_distance#Python

    :param s1: The first string
    :param s2: The second string
    :returns: The levenshtein distance
    """
    if len(s1) < len(s2):
        return levenshtein(s2, s1)

    if len(s2) == 0:
        return len(s1)

    previous_row = range(len(s2) + 1)
    for i, c1 in enumerate(s1):
        current_row = [i + 1]
        for j, c2 in enumerate(s2):
            insertions = previous_row[j + 1] + 1 # j+1 instead of j since previous_row and current_row are one character longer
            deletions = current_row[j] + 1       # than s2
            substitutions = previous_row[j] + (c1 != c2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row
    
    return previous_row[-1]

def best_practices_test(
        report,
        assertor,
        subject,
        fragment_wih_import,
        fragment_no_import,
        fragment_no_owl,
        skip=[],
        skip_pass=False
    ):
    """Test the best practices mistakes that do not break the RDF syntax neither the OWL reasoning,
    but that should still not happen

    :param ontology: The ontology to test
    :returns: An report dictionary
    """

    skipped_best_practice = skip + SKIPPED_TESTS

    # Check for terms not linked to an ontology
    if not "term-referencing" in skipped_best_practice:
        unlinked_subjects = query_graph(fragment_no_owl, NOT_REFERENCED)
        unlinked_subjects_pointers = [[pointer] for pointer in unlinked_subjects]
        unlinked_subject_messages = [
            f"Subject :{item[len(ONTOLOGY_URL)+1:-1]} not linked to a module by a rdfs:isDefinedBy property"
            for item in unlinked_subjects
        ]
        make_assertion(
            report,
            assertor,
            subject,
            "term-referencing",
            "no-reference-module",
            unlinked_subject_messages,
            unlinked_subjects_pointers,
            skip_pass=skip_pass
        )
    
    if not "domain-and-range-referencing" in skipped_best_practice:
        # Checking for domain property out of the vocabulary
        dov = query_graph(fragment_wih_import, DOMAIN_OUT_Of_VOCABULARY)
        dov = [line.split("\t") for line in dov]
        dov_messages = [
            f"The property :{item[0][1:-1]} has a domain out of the ontology: {item[1]}"
            for item in dov
        ]
        dov_pointers = [
            [f"<{ONTOLOGY_URL}{item[0][1:-1]}>", item[1]]
            for item in dov
        ]
        make_assertion(
            report,
            assertor,
            subject,
            "domain-and-range-referencing",
            "domain-out-of-vocabulary",
            dov_messages,
            dov_pointers,
            skip_pass=skip_pass
        )

        # Checking for range property out of the vocabulary
        rov = query_graph(fragment_wih_import, RANGE_OUT_OF_VOCABULARY)
        rov = [line.split("\t") for line in rov]
        rov_messages = [
            f"The property :{item[0][1:-1]} has a range out of the ontology: {item[1]}"
            for item in rov
        ]
        rov_pointers = [
            [f"<{ONTOLOGY_URL}{item[0][1:-1]}>", item[1]]
            for item in rov
        ]
        make_assertion(
            report,
            assertor,
            subject,
            "domain-and-range-referencing",
            "range-out-of-vocabulary",
            rov_messages,
            rov_pointers,
            skip_pass=skip_pass
        )

    # Checking for too close terms
    if not "terms-differenciation" in skipped_best_practice:
        term_pairs = query_graph(fragment_no_import, GET_TERM_PAIRS)
        term_pairs = [[item.strip()[1:-1] for item in line.split("\t")] for line in term_pairs]
        term_pairs = [pair for pair in term_pairs if levenshtein(*pair) < TERM_DISTANCE_THRESHOLD]

        make_assertion(
            report,
            assertor,
            subject,
            "terms-differenciation",
            "too-close-terms",
            [f"The following terms are too similar: :{line[0]} and :{line[1]}" for line in term_pairs],
            [[f"<{ONTOLOGY_URL}{item}>" for item in line] for line in term_pairs],
            skip_pass=skip_pass
        )
    
    if not "labeled-terms" in skipped_best_practice:
        not_labeled_terms = query_graph(fragment_no_owl, NOT_LABELED)
        not_labeled_pointers = [[f"<{ONTOLOGY_URL}{line.strip()[1:-1]}>"] for line in not_labeled_terms if len(line.strip()) > 0]
        not_labeled_messages = [f"The term :{pointer[0].split(ONTOLOGY_SEPARATOR)[-1][:-1]} has no rdfs:label to define it in natural language" for pointer in not_labeled_pointers]
        make_assertion(
            report,
            assertor,
            subject,
            "labeled-terms",
            "not-labeled-term",
            not_labeled_messages,
            pointers=not_labeled_pointers,
            skip_pass=skip_pass
        )

def merged_fragment_set_test(
        report,
        assertor,
        fragments_to_merge,
        heart_name,
        skip_pass=False,
        tested_only=False,
        custom_title=""
    ):
    fragments_keys = [
        relpath(fragment, PWD_TO_ROOT_FOLDER).replace(sep, "/")
        for fragment in fragments_to_merge
    ]

    if len(fragments_keys) == 0:
        return

    subject = make_subject(report, fragments_keys, name=heart_name, custom_title=custom_title)
    fragment_check(
        fragments_to_merge,
        report,
        assertor,
        subject,
        skip_pass=skip_pass,
        tested_only=tested_only
    )
