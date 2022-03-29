
from fastapi import APIRouter

def EclassServiceRouter(eclass_service):
    router = APIRouter()

    @router.get("/list_courses")
    def list_courses():
        return eclass_service.list_courses()