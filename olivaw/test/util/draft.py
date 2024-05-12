from olivaw.test.turtle import (
    make_subject as make_turtle_subject,
    make_not_tested as make_turtle_not_tested,
    make_assertion as make_turtle_assertion,
    make_outcomes as make_turtle_outcomes,
    make_outcome as make_turtle_outcome
)
from olivaw.test.util.skip import should_skip as should_test_skip

class AssertDraft:
    def __init__(self, report, assertor, **args):
        self.report = report
        self.assertor = assertor
        self.pointers = []
        self(**args)

    def __call__(self,**args):
        for field , value in args.items():
            setattr(self, field, value)
        return self
    
    def reporting(self, subject, statement):
        for predicate, object in statement:
            self.report.add((subject, predicate, object))

    def has_field(self, field):
        return hasattr(self, field) and not getattr(self, field) is None
    
    def new_assertion(self):
        for field in vars(self).keys():
            if field in ["report", "assertor", "subject", "criterion", "file"]:
                continue
            if field == "pointers":
                self.pointers = []
                continue
            setattr(self, field, None)

    def fix_pointers(self):
        if self.has_field("pointers") and \
            len(self.pointers) > 0 and \
            len(self.pointers) == len(self.messages): return
        self.pointers = []

    def make_subject(self, *args, **kwargs):
        self.subject = make_turtle_subject(self, *args, **kwargs)

    def make_assertion(self, **kwargs):
        make_turtle_assertion(self(**kwargs))

    def make_not_tested(self, *criterions):
        for criterion in criterions:
            make_turtle_not_tested(self(criterion=criterion))
    
    def make_outcomes(self, **kwargs):
        return make_turtle_outcomes(self(**kwargs))
    
    def make_outcome(self, **kwargs):
        return make_turtle_outcome(self(**kwargs))
    
    def should_skip(self, **kwargs):
        return should_test_skip(self(**kwargs))