from .core import Template

from parse import parse

class ParseNamed(Template):
    def __init__(self, parse):
        self.parse = parse

    def apply(self, object):
        return parse(self.parse, object).named

class ParseFixed(Template):
    def __init__(self, parse):
        self.parse = parse

    def apply(self, object):
        return parse(self.parse, object).fixed