from templated_parser import *

def test_Select(parser, test_html):
    template = Select("h1")
    print(parser.parse(template, test_html))

def test_Contigious(parser, test_html):
    template = Contigious(
        Select("h1::text"),
    )
    print(parser.parse(template, test_html))

def test_Attribute(parser, test_html):
    template = Contigious(
        Select("body::attr(onclick)"),
    )
    print(parser.parse(template, test_html))

def test_ParseFixed(parser, test_html):
    template = Contigious(
        Select("h1::text"),
        ParseFixed("This is {} heading")
    )
    print(parser.parse(template, test_html))
