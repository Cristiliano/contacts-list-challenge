from fastapi import APIRouter, HTTPException

from database.schemas import PersonCreateInput, NumberCreateInput, ContactCreateInput, StandardOutput, ErrorOutput, UserListOutput
from services.person_service import PersonService, NumberService

from typing import List

person_router = APIRouter(prefix='/person')
number_router = APIRouter(prefix='/number')
contact_router = APIRouter(prefix='/contact')

@person_router.post('/create', response_model=StandardOutput, responses={400: {'model': ErrorOutput}})
async def person_create(person_input: PersonCreateInput):
    try:
         await PersonService.create_person(name=person_input.name, email=person_input.email)
         return StandardOutput(message='Ok')
    except Exception as error:
         raise HTTPException(400, detail=str(error))

@person_router.delete('/delete/{person_id}', response_model=StandardOutput, responses={400: {'model': ErrorOutput}})
async def person_delete(person_id: int):
    try:
         await PersonService.delete_person(person_id=person_id)
         return StandardOutput(message='Ok')
    except Exception as error:
         raise HTTPException(400, detail=str(error))
    
@person_router.get('/list', response_model=List[UserListOutput], responses={400: {'model': ErrorOutput}})
async def person_list():
    try:
         return await PersonService.list_person()
    except Exception as error:
         raise HTTPException(400, detail=str(error))
    


@number_router.post('/create', response_model=StandardOutput, responses={400: {'model': ErrorOutput}})
async def number_create(number_input: NumberCreateInput):
    try:
         await NumberService.create_number(person_id=number_input.person_id, tell=number_input.tell, reference=number_input.reference)
         return StandardOutput(message='Ok')
    except Exception as error:
         raise HTTPException(400, detail=str(error))
    
@number_router.delete('/delete/{number_id}', response_model=StandardOutput, responses={400: {'model': ErrorOutput}})
async def person_delete(number_id: int):
    try:
         await NumberService.delete_number(number_id=number_id)
         return StandardOutput(message='Ok')
    except Exception as error:
         raise HTTPException(400, detail=str(error))


@contact_router.post('/create', response_model=StandardOutput, responses={400: {'model': ErrorOutput}})
async def contact_create(contact_input: ContactCreateInput):
    try:
         person_id = await PersonService.create_person(email=contact_input.email, name=contact_input.name)
         
         for n in contact_input.numbers:
              await NumberService.create_number(person_id=person_id, reference=n.reference, tell=n.tell)

         return StandardOutput(message='Ok')
    except Exception as error:
         raise HTTPException(400, detail=str(error))