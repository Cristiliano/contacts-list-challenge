from pydantic import BaseModel
from typing import List

class PersonCreateInput(BaseModel):
    name: str
    email: str

class NumberCreateInput(BaseModel):
    tell: str
    reference: str
    person_id: int

class StandardOutput(BaseModel):
    message: str

class ErrorOutput(BaseModel):
    detalil: str

class Number(BaseModel):
    id: int
    tell: str
    reference: str
    person_id: int

    class Config:
        orm_mode = True

class UserListOutput(BaseModel):
    id: int
    name: str
    numbers: List[Number]

    class Config:
        orm_mode = True