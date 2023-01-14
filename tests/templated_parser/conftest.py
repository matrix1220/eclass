
from pytest import fixture

from posixpath import dirname

@fixture
def test_html():
    return """<!DOCTYPE html>
<html>
<title>HTML Tutorial</title>
<body onclick=alert() align=center>

<h1>This is a heading</h1>
<p>This is a paragraph.</p>

</body>
</html>"""

@fixture
def eclass_html():
    return open(f"{dirname(__file__)}/eclass.html").read()