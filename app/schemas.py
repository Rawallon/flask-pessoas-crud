from datetime import datetime
from typing import Optional

from pydantic import BaseModel, validator


class PessoaBase(BaseModel):
    nome: str
    rg: str
    cpf: str
    data_nascimento: datetime
    data_admissao: datetime
    funcao: Optional[str] = None


class PessoaView(PessoaBase):
    id_pessoa: int


class PessoaEdit(PessoaBase):
    pass


class PessoaCreate(PessoaBase):
    pass

    class Config:
        orm_mode = True
