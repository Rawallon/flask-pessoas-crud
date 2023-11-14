from datetime import datetime
from typing import Optional

from pydantic import BaseModel, validator


class PessoaBase(BaseModel):
    nome: str
    rg: str
    cpf: str
    data_nascimento: datetime
    data_admissao: datetime
    funcao: Optional[str]

    @validator("data_nascimento", pre=True)
    def parse_data_nascimento(cls, value):
        return cls.parse_datetime(value)

    @validator("data_admissao", pre=True)
    def parse_data_admissao(cls, value):
        return cls.parse_datetime(value)

    @classmethod
    def parse_datetime(cls, value):
        if isinstance(value, str):
            try:
                return datetime.strptime(value, "%d-%m-%Y")
            except ValueError as e:
                raise ValueError("Invalid datetime format. Use '%d-%m-%Y'") from e
        return value


class PessoaView(PessoaBase):
    pass


class PessoaCreate(PessoaBase):
    id_pessoa: int

    class Config:
        orm_mode = True
