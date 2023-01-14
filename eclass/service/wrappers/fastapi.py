
from fastapi import APIRouter

def EclassServiceRouter(eclass_service):
    router = APIRouter()

    @router.get("/list_courses")
    async def list_courses():
        return await eclass_service.list_courses()
    
    return router