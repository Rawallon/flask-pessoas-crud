from datetime import datetime
from typing import List, Optional

from fastapi import APIRouter, Depends, HTTPException, Query

from app.crud import (
    create_pessoa,
    delete_pessoa,
    get_pessoa,
    get_pessoas,
    update_pessoa,
)
from app.database import SessionLocal as Session
from app.models import Pessoa
from app.schemas import PessoaCreate, PessoaEdit, PessoaView

pessoasRouter = APIRouter()


# Dependency to get the database session
def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()


@pessoasRouter.post("/pessoas/", response_model=PessoaView)
def create_person(pessoa: PessoaCreate, db: Session = Depends(get_db)):
    print("pessoa", pessoa)
    pessoa_model = Pessoa(
        nome=pessoa.nome,
        rg=pessoa.rg,
        cpf=pessoa.cpf,
        data_nascimento=pessoa.data_nascimento,
        data_admissao=pessoa.data_admissao,
        funcao=pessoa.funcao,
    )
    return create_pessoa(db=db, pessoa=pessoa_model)


@pessoasRouter.get("/pessoas/{id_pessoa}", response_model=PessoaView)
def read_person(id_pessoa: int, db: Session = Depends(get_db)):
    pessoa = get_pessoa(db=db, id_pessoa=id_pessoa)
    if pessoa is None:
        raise HTTPException(status_code=404, detail="PessoaView not found")
    return pessoa


@pessoasRouter.get("/pessoas/", response_model=List[PessoaView])
def read_people(
    db: Session = Depends(get_db),
    nome: Optional[str] = Query(None),
    rg: Optional[str] = Query(None),
    cpf: Optional[str] = Query(None),
    data_nascimento: Optional[datetime] = Query(None),
    data_admissao: Optional[datetime] = Query(None),
    funcao: Optional[str] = Query(None),
    skip: int = 0,
    limit: int = 10,
):
    filters = {
        "nome": nome,
        "rg": rg,
        "cpf": cpf,
        "data_nascimento": data_nascimento,
        "data_admissao": data_admissao,
        "funcao": funcao,
    }

    filtered_pessoas = get_pessoas(
        db=db,
        skip=skip,
        limit=limit,
        **{k: v for k, v in filters.items() if v is not None}
    )
    return filtered_pessoas


@pessoasRouter.put("/pessoas/{id_pessoa}", response_model=PessoaView)
def update_person(id_pessoa: int, pessoa: PessoaEdit, db: Session = Depends(get_db)):
    existing_pessoa = get_pessoa(db=db, id_pessoa=id_pessoa)
    if existing_pessoa is None:
        raise HTTPException(status_code=404, detail="PessoaView not found")
    return update_pessoa(db=db, id_pessoa=id_pessoa, **pessoa.dict())


@pessoasRouter.delete("/pessoas/{id_pessoa}", response_model=PessoaView)
def delete_person(id_pessoa: int, db: Session = Depends(get_db)):
    pessoa = get_pessoa(db=db, id_pessoa=id_pessoa)
    if pessoa is None:
        raise HTTPException(status_code=404, detail="PessoaView not found")
    return delete_pessoa(db=db, id_pessoa=id_pessoa)
