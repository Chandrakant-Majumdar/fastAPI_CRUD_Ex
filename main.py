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

    - student_id: Unique ID for the student
    - student: Student object with name, age, and grade

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

@app.put("/students/{student_id}")
def update_student(student_id: int, student: Student):
    """
    Update an existing student's information.

    - student_id: ID of the student to update
    - student: Updated student data

    Returns a success message and the updated student.
    """
    if student_id not in students:
        raise HTTPException(status_code=404, detail="Student not found")
    students[student_id] = student
    return {"message": "Student updated successfully", "student": student}

@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    """
    Delete a student by ID.

    - student_id: ID of the student to delete

    Returns a success message if deletion is successful.
    """
    if student_id not in students:
        raise HTTPException(status_code=404, detail="Student not found")
    del students[student_id]
    return {"message": "Student deleted successfully"}

class Student(BaseModel):
    """
    Student model representing basic information about a student.
    """
    name: str
    Gender: str
    age: int

@app.get("/")
def root():
    """
    Root endpoint providing API information.
    """
    return {
        
        "endpoints": {
            "Create": "POST /students/{student_id}",
            "Read": "GET /students/{student_id}",
            "Update": "PUT /students/{student_id}",
            "Delete": "DELETE /students/{student_id}"
        },
        "author": "Chandrakant & Saima"
    }