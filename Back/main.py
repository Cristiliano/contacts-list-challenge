from typing import Union
from fastapi import APIRouter, FastAPI

app = FastAPI()
router = APIRouter()

pessoas = {
    1: {"name": "João", 
        "tell": [
            '81989876767',
            '11986875452'
        ], 
        "email": 'juao@gmail.com'
        },
}

@app.get("/")
def read_root():
    return {
        'id': 1,
        'nome': 'nome1' 
    }

# @app.get("/pessoas/{id_pessoa}")
# def pegar_venda(id_pessoa: int):
#     if id_pessoa in pessoas:
#         return pessoas[id_pessoa]
#     else:
#         return {"Erro": "ID pessoa inexistente"}


app.include_router(prefix='/first', router = router)