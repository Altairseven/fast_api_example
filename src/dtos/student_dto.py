from pydantic import BaseModel as DtoBase

class CreateStudentRequest(DtoBase):
    first_name: str
    last_name: str
    dni: int
    current_course: str | None

class StudentDto(DtoBase):
    id: int
    first_name: str
    last_name: str
    dni: int
    current_course: str | None
