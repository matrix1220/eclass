from .core import Template

class Select(Template):
    def __init__(self, selector):
        self.selector = selector

    def apply(self, object):
        return object.css(self.selector)

class SelectGet(Template):
    def __init__(self, selector):
        self.selector = selector

    def apply(self, object):
        return object.css(self.selector).get()

class SelectGetArray(Template):
    def __init__(self, selector):
        self.selector = selector

    def apply(self, object):
        return object.css(self.selector).get_all()

# class Content(Template):
#     def apply(self, object: BeautifulSoup):
#         return object.contents[0]

# class Contents(Template):
#     def apply(self, object: BeautifulSoup):
#         return object.contents

# class Attribute(Template):
#     def __init__(self, attribute):
#         self.attribute = attribute

#     def apply(self, object: BeautifulSoup):
#         return object.attrs[self.attribute]

# class AttributesObject(Template):
#     def __init__(self, *attributes):
#         self.attributes = attributes

#     def apply(self, object: BeautifulSoup):
#         return {attr:object.attrs[attr] for attr in self.attributes}

# class AttributesArray(Template):
#     def __init__(self, *attributes):
#         self.attributes = attributes

#     def apply(self, object: BeautifulSoup):
#         return [object.attrs[attr] for attr in self.attributes]

# class Children(Template):
#     def apply(self, object: BeautifulSoup):
#         return object.children