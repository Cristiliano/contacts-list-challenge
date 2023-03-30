from pydantic import BaseModel

class PersonCreateInput(BaseModel):
    name: str
    email: str

class StandardOutput(BaseModel):
    message: str

class ErrorOutput(BaseModel):
    detalil: str