
from templated_parser import *


course_list = Contigious(
    Select("div.course_lists"),
    SelectArray("div.course_box"),
    ForArray(
        UniteObject(
            Contigious(
                Select("a:attr(href)"),
                ParseNamed("http://eclass.inha.ac.kr/course/view.php?id={id}"),
            ),
            Contigious(
                Select("div.course-name div.course-title"),
                Select("h3::text"),
                ParseNamed("{name}[{}-{course}-{section}]"),
            ),
            
        )
    )
)