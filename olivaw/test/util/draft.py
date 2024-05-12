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
    
    def should_skip(self, **kwargs):
        return should_test_skip(self(**kwargs))