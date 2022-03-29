from pydantic import BaseModel

class Course(BaseModel):
    id: int
    name: str
    number: str
    section: str
    teacher: str