
from templated_parser import *


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