from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class Produto(BaseModel):
    codigo: int = None
    nome: str
    descricao: str
    foto: bool = None
    valor_unitario: float

# Criar os endpoints de produto: GET, POST, PUT, DELETE
@router.get("/produto/{id}", tags=["produto"])
def get_funcionario(id: int):
    return {"msg": "get executado", "id": id}, 200

@router.post("/produto/{id}", tags=["produto"])
def post_funcionario(id: int, f: Produto):
    return {"msg": "post executado", "id": id, "nome": f.nome, "cpf": f.cpf, "telefone": f.telefone}, 200

@router.put("/produto/{id}", tags=["produto"])
def put_funcionario(id: int, f: Produto):
    return {"msg": "put executado", "id": id, "nome": f.nome, "cpf": f.cpf, "telefone": f.telefone}, 201

@router.delete("/produto/{id}", tags=["produto"])
def delete_funcionario(id: int):
    return {"msg": "delete executado", "id": id}, 201