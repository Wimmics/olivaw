"""Module reponsible for providing the draft class that stores the useful data when preparing a test"""

from rdflib import BNode, Graph
from rdflib.term import Identifier
from olivaw.test.util.skip import should_skip as should_test_skip

class AssertDraft:
    """Utilitary class that stores useful data for building report assertions
    
    The following fields are going to be used anywhere in the `olivaw.test` module:

    :param graph: Graph containing the subject
    :type graph: `py4j.java_gateway.JavaObject` referencing an instance of `fr.inria.corese.core.Graph`

    :param report: The test report
    :type report: `rdflib.Graph`

    :param criterion: Criterion identifier for the current test
    :type criterion: `str`

    :param outcome_type: Outcome type that is expected for the next outcome
    :type outcome_type: `str`, one of MajorFail, MinorFail, NotTested, CannotTell, Pass

    :param error: Error identifier that is expected for the next outcome
    :type error: `str`

    :param description: Description of the next outcome
    :type description: `str`

    :param pointers: List of pointers to include to the next outcome or outcomes
    :type pointers: `Union[list[str], list[list[str]]`

    :param messages: Expected messages to include to the next outcome or outcomes
    :type: messages: `Union[str, list[str]]`

    :param criterion_uri: URI of the test criterion
    :type criterion_uri: `str`

    :param assertor: `rdflib` object representing the test assertor
    :type assertor: `rdflib.BNode`

    :param subject: `rdflib` object representing the test subject
    :type subject: `rdflib.BNode`

    :param file: File path or list of file paths leading to the test subject part(s)
    :type file: `Union[str, list[str]]`

    :param custom_test_data: Dictionary contaning the useful information about the custom tests
    :type custom_test_data: 

    ```
    dict[ # dict containing information about all the custom tests

            str, # A custom test criterion identifier

            dict [ # A dict contaninig the information about a given custom test

                str, # A information name

                Union[str, List[str]] # Some useful information

            ]

        ]
    ```
    """
    def __init__(self, report: Graph, assertor: BNode, **kwargs) -> None:
        """Constructor method

        :param report: Test report
        :type report: `rdflib.Graph`

        :param assertor: The test assertor
        :type assertor: `rdflib.BNode`

        :param **kwargs: Set of optional fields to the `olivaw.test.AssertDraft`
        :type **kwargs: See the `olivaw.test.AssertDraft`class documentation for the details
        """
        self.report = report
        self.assertor = assertor
        self.pointers = []
        self(**kwargs)

    def __call__(self,**kwargs) -> None:
        """Sets the provided fields to the AssertDraft

        :params **kwargs: Set of optional fields to the `olivaw.test.AssertDraft`
        :type **kwargs: See the `olivaw.test.AssertDraft`class documentation for the details
        """
        for field , value in kwargs.items():
            setattr(self, field, value)
        return self
    
    def reporting(
            self,
            subject: BNode,
            statement: list[tuple[Identifier, Identifier]]
        ) -> None:
        """Add the provided triples to the `olivaw.test.AssertDraft` embedded report

        :param subject: The test subject
        :type subject: `rdflib.BNode`

        :param statement: List of predicates with related objects that must be added to the report, with the subect parameter as subject
        :type statement: `list[tuple[rdflib.term.Identifier, rdflib.term.Identifier]]`
        """
        for predicate, object in statement:
            self.report.add((subject, predicate, object))

    def has_field(self, field: str) -> bool:
        """Returns if the provided field name exists in the current `olivaw.test.AssertDraft` instance with a not null value

        :param field: The field name
        :type field: `str`

        :returns: A boolean stating if the value exists with a non null value
        :rtype: `bool`
        """
        return hasattr(self, field) and not getattr(self, field) is None
    
    def new_assertion(self) -> None:
        """Erase the proper attributes from the current `olivaw.test.AssertDraft` instance for the next assertions preparation"""
        for field in vars(self).keys():
            if field in ["report", "assertor", "subject", "criterion", "file"]:
                continue
            if field == "pointers":
                self.pointers = []
                continue
            setattr(self, field, None)

    def fix_pointers(self) -> None:
        """Removes the pointer if their number does not match with the current `olivaw.test.AssertDraft` instance number of messages"""
        if self.has_field("pointers") and \
            len(self.pointers) > 0 and \
            len(self.pointers) == len(self.messages): return
        self.pointers = []
    
    def should_skip(self, **kwargs) -> bool:
        """Returns if the current `olivaw.test.AssertDraft` instance test should be skipped
        
        :param **kwargs: Set of optional information to set to the current `olivaw.test.AssertDraft` instance
        :type **kwargs: See the `olivaw.test.AssertDraft`class documentation for the details

        :returns: A boolean stating if the current test should be skipped
        :rtype: `bool`
        """
        return should_test_skip(self(**kwargs))