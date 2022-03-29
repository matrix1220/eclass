from pytest import fixture


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