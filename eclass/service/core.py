
from eclass.parser import parse
from eclass.links import MAIN_PAGE

class EclassService:
    def __init__(self, fetcher):
        self.fetcher = fetcher

    def list_assignments(self):
        pass

    async def list_courses(self):
        page = await self.fetcher.get(MAIN_PAGE)
        return parse(MAIN_PAGE, page)