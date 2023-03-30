from fastapi import APIRouter, HTTPException

from database.schemas import PersonCreateInput, StandardOutput, ErrorOutput
from services.person_service import PersonService

person_router = APIRouter(prefix='/person')
number_router = APIRouter(prefix='/number')

@person_router.post('/create', response_model=StandardOutput, responses={400: {'model': ErrorOutput}})
async def person_create(person_input: PersonCreateInput):
    try:
         await PersonService.create_user(name=person_input.name, email=person_input.email)
         return StandardOutput(message='Ok')
    except Exception as error:
         raise HTTPException(400, detail=str(error))