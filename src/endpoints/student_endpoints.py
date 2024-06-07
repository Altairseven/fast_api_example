"""Student Endpoints"""
# pylint: disable=missing-function-docstring
from fastapi import status, APIRouter

from src.domain.Student import Student
from src.dtos.student_dto import StudentDto, CreateStudentRequest

from src.database import dbContext
studentEndpoints = APIRouter(prefix="/api/v1/students", tags=["Students"])

@studentEndpoints.get("/",
    status_code=status.HTTP_200_OK,
    response_model=list[StudentDto], summary="Get all students")
def get_students(_db: dbContext):
    studentsList = _db.query(Student).all()
    mapped = [StudentDto(**s.__dict__) for s in studentsList]
    return mapped

@studentEndpoints.get("/<id>",
    status_code=status.HTTP_200_OK,
    response_model=StudentDto, summary="Get studenty by Id")
def get_student(studentId: int, _db: dbContext):
    en = _db.query(Student).filter_by(id=studentId).first()
    if en is None:
        return None
    dic = en.__dict__
    newDto = StudentDto(**dic)
    return newDto


@studentEndpoints.post("/",
    status_code=status.HTTP_201_CREATED,
    response_model=StudentDto, summary="Create a new student")
def create_student(student: CreateStudentRequest, _db: dbContext):
    en = Student(**student.model_dump())
    _db.add(en)
    _db.commit()
    _db.refresh(en)
    newDto = StudentDto(**en.__dict__)
    return newDto

@studentEndpoints.put("/",
    status_code=status.HTTP_200_OK,
    summary="Update a student")
def update_student(student: StudentDto, _db: dbContext):
    # Forma 1 (Todos los campos menos los excluidos):
    # fields = student.model_dump(exclude=["id"])
    # _db.query(Student).filter_by(id=student.id).update(fields)
    # _db.commit()

    #Forma 2 (a mano campo por campo)
    en = _db.query(Student).filter_by(id=student.id).first()
    en.first_name = student.first_name
    en.last_name = student.last_name
    en.dni = student.dni
    _db.commit()
    _db.refresh(en)
    return student

@studentEndpoints.patch("/<id>/course/<cursito>",
    status_code=status.HTTP_200_OK,
    response_model=StudentDto, summary="Update current course for a student")
def update_current_course(studentId: int, cursito: str, _db: dbContext):
    en = _db.query(Student).filter_by(id=studentId).first()
    if en is None:
        return None
    en.current_course = cursito
    _db.commit()
    _db.refresh(en)
    return StudentDto(**en.__dict__)

@studentEndpoints.delete("/<studentId>", \
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Delete a Student")
def delete_student(studentId: int, _db: dbContext):
    en = _db.query(Student).filter_by(id=studentId).first()
    _db.delete(en)
    _db.commit()
