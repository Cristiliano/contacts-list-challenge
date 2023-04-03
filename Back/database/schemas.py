from pydantic import BaseModel
from typing import List

class Person(BaseModel):
    name: str
    email: str

class Number(BaseModel):
    tell: str
    reference: str
    person_id: int

class PersonCreateInput(Person):
    pass

class NumberCreateInput(Number):
    pass

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

class ContactNumberList(BaseModel):
    tell: str
    reference: str

class ContactCreateInput(Person):
    numbers: List[ContactNumberList]

    class Config:
        orm_mode = True