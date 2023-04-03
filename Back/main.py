from typing import Union
from fastapi import APIRouter, FastAPI

from controllers.person_controller import person_router, number_router, contact_router

app = FastAPI()
router = APIRouter()

@app.get("/")
def read_root():
    return {
        'id': 1,
        'nome': 'nome1' 
    }

app.include_router(prefix='/first', router = router)
app.include_router(person_router)
app.include_router(number_router)
app.include_router(contact_router)