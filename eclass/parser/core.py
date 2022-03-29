
from templated_parser import templated_parse

from eclass.service.models import Course

from .templates import course_list

page_map = {
    "http://eclass.inha.ac.kr": course_list,
}


def parse(page_url, page):
    template = page_map[page_url]
    return templated_parse(template, page)