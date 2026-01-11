from pydantic import BaseModel

class StudentProfile(BaseModel):
    name: str
    skills: str
    interests: str
    experience: str

class InternshipRequest(BaseModel):
    student: StudentProfile
    internship_description: str
