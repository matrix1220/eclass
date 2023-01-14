from templated_parser import *

def test_Select(test_html):
    template = Select("h1")
    print(templated_parse(template, test_html))

def test_Contigious(test_html):
    template = Contigious(
        Select("h1::text"),
    )
    print(templated_parse(template, test_html))

def test_Attribute(test_html):
    template = Contigious(
        Select("body::attr(onclick)"),
    )
    print(templated_parse(template, test_html))

# def test_ParseFixed(test_html):
#     template = Contigious(
#         Select("h1::text"),
#         ParseFixed("This is {} heading")
#     )
#     print(templated_parse(template, test_html))

    # course_list = Contigious(
    #     Select("div.course_lists"),
    #     SelectArray("div.course_box"),
    #     ForArray(
    #         UniteObject(
    #             Contigious(
    #                 Select("a:attr(href)"),
    #                 ParseNamed("http://eclass.inha.ac.kr/course/view.php?id={id}"),
    #             ),
    #             Contigious(
    #                 Select("div.course-name div.course-title"),
    #                 Select("h3::text"),
    #                 ParseNamed("{name}[{}-{course}-{section}]"),
    #             ),
                
    #         )
    #     )
    # )

def test_eclass(eclass_html):

    course_list = Contigious(
        Select("div.course_lists"),
        Select("div.course_box"),
        ForArray(
            UniteObject(
                Contigious(
                    SelectGet("a::attr(href)"),
                    ParseNamed("http://eclass.inha.ac.kr/course/view.php?id={id}"),
                ),
                Contigious(
                    Select("div.course-name div.course-title"),
                    SelectGet("h3::text"),
                    ParseNamed("{name}[{}-{course}-{section}]"),
                ),
                
            )
        )

    )
    print(templated_parse(course_list, eclass_html))
