from sqlalchemy.ext.asyncio.session import async_session
from sqlalchemy import delete
from sqlalchemy.future import select

from database.models import Person, Number
from database.connection import async_session


class PersonService:
    async def create_person(name: str, email: str):
        async with async_session() as session:
            session.add(Person(name=name, email=email))
            await session.commit()

    async def delete_person(person_id: int):
        async with async_session() as session:
            await session.execute(delete(Person).where(Person.id==person_id))
            await session.commit()
    
    async def list_person():
        async with async_session() as session:
            response = await session.execute(select(Person))
            return response.scalars().all()
        

class NumberService:
    async def create_number(person_id: int, tell: str, reference: str):
        async with async_session() as session:
            session.add(Number(person_id=person_id, tell=tell, reference=reference))
            await session.commit()
    
    async def delete_number(number_id: int):
        async with async_session() as session:
            await session.execute(delete(Number).where(Number.id==number_id))
            await session.commit()