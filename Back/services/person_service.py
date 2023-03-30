from database.models import Person, Number
from database.connection import async_session

# from typing import List

class PersonService:
    async def create_user(name: str, email: str):
        async with async_session() as session:
            session.add(Person(name=name, email=email))
            await session.commit()