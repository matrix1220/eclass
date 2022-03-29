
from eclass.parser import parse
MAIN_PAGE = "http://eclass.inha.ac.kr"

class EclassService:
    def __init__(self, fetcher):
        self.fetcher = fetcher

    def list_assignments(self):
        pass

    def list_courses(self):
        page = self.fetcher.get(MAIN_PAGE)
        return parse(MAIN_PAGE, page)