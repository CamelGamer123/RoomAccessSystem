"""
This is the main file of the project.

This file contains the FastAPI application and the routes.

To access the API documentation, go to http://localhost:8000/docs or http://localhost:8000/redoc
"""
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Please go to http://localhost:8000/docs or http://localhost:8000/redoc to see the API "
                       "documentation"}


@app.get("/getaccesslogs/{studentId}")
async def getAccessLogs(studentId: str):
    """
    This route returns all access logs of a specific student.

    Args:
        studentId (str): The student ID of the student whose access logs are to be returned.

    Returns:
        list: A list of AccessInstance objects.
    """
    pass
