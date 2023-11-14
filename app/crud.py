from datetime import datetime

from sqlalchemy import or_

from app.database import SessionLocal as Session
from app.models import Pessoa
from app.schemas import PessoaCreate


def create_pessoa(db: Session, pessoa: PessoaCreate):
    db.add(pessoa)
    db.commit()
    db.refresh(pessoa)
    return pessoa


def get_pessoa(db: Session, id_pessoa: int):
    return db.query(Pessoa).filter(Pessoa.id_pessoa == id_pessoa).first()


def get_pessoas(db: Session, skip: int = 0, limit: int = 10, **filters):
    query = db.query(Pessoa)

    if filters:
        # Apply filters if provided
        for key, value in filters.items():
            # Assuming all filtering criteria are case-insensitive
            query = query.filter(or_(getattr(Pessoa, key).ilike(f"%{value}%")))

    return query.offset(skip).limit(limit).all()


def update_pessoa(
    db: Session,
    id_pessoa: int,
    nome: str,
    rg: str,
    cpf: str,
    data_nascimento: datetime,
    data_admissao: datetime,
    funcao: str,
):
    pessoa = db.query(Pessoa).filter(Pessoa.id_pessoa == id_pessoa).first()
    pessoa.nome = nome
    pessoa.rg = rg
    pessoa.cpf = cpf
    pessoa.data_nascimento = data_nascimento
    pessoa.data_admissao = data_admissao
    pessoa.funcao = funcao
    db.commit()
    db.refresh(pessoa)
    return pessoa


def delete_pessoa(db: Session, id_pessoa: int):
    pessoa = db.query(Pessoa).filter(Pessoa.id_pessoa == id_pessoa).first()
    db.delete(pessoa)
    db.commit()
    return pessoa
