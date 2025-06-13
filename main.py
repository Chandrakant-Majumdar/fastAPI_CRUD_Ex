from fastapi import FastAPI,HTTPException
from pydantic import BaseModel

app= FastAPI()

students={}

class Student(BaseModel):
    """
    Student model representing basic information about a student.
    """
    name:str
    Gender:str
    age:int

@app.post("/students/{student_id}")
def create_student(student_id:int,student:Student):
    """
    Create a new student with the given ID.

    - **student_id**: Unique ID for the student
    - **student**: Student object with name, age, and grade

    Returns a success message and the student details.
    """
    if student_id in students:
        raise HTTPException(status_code=400, detail="Student already exists")
    students[student_id] = student
    return {"message": "Student added successfully", "student": student}

@app.get("/students/{student_id}")
def read_student(student_id: int):
    """
    Get details of a student by ID.
    """
    if student_id not in students:
        raise HTTPException(status_code=404, detail="Student not found")
    return students[student_id]
