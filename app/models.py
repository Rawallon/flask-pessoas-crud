from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Pessoa(Base):
    __tablename__ = "pessoas"

    id_pessoa = Column(Integer, primary_key=True, index=True)
    nome = Column(String(255), index=True)
    rg = Column(String(255), index=True, unique=True)
    cpf = Column(String(255), index=True, unique=True)
    data_nascimento = Column(DateTime)
    data_admissao = Column(DateTime)
    funcao = Column(String(255), nullable=True)
