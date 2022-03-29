from .core import Template

class Contigious(Template):
    def __init__(self, *templates):
        self.templates = templates

    def apply(self, object):
        for template in self.templates:
            object = template.apply(object)
        
        return object

class ForArray(Template):
    def __init__(self, template):
        self.template = template

    def apply(self, object):
        return [self.template.apply(item) for item in object]


class UniteObject(Template):
    def __init__(self, *elements):
        self.elements = elements

    def apply(self, object):
        result = {}
        for element in self.elements:
            result.update(**element.apply(object))
        return result

class UniteArray(Template):
    def __init__(self, *elements):
        self.elements = elements

    def apply(self, object):
        result = []
        for element in self.elements:
            result.extend(element.apply(object))
        return result