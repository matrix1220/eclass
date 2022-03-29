from pytest import fixture

from templated_parser import Parser

@fixture
def parser():
    return Parser()