# FastAPI Pessoas CRUD

API simples contendo um CRUD para entidade Pessoa

# Introdução
Este projeto faz uso das tecnologias FastAPI e SQLAlchemy para criar uma aplicação web eficiente e escalável. As principais vantagens dessas tecnologias incluem:

- FastAPI:

Desenvolvimento rápido : O FastAPI é conhecido por sua sintaxe simples permitindo um desenvolvimento rápido de APIs.
Autodocumentação: Gera automaticamente documentação interativa da API a partir de modelos Pydantic.
Performance: Utiliza o Starlette e Pydantic para proporcionar uma execução comparável a frameworks como o NodeJS e o Go.

- SQLAlchemy:

Abstração de Banco de Dados: Oferece uma abstração eficaz para interagir com diferentes sistemas de banco de dados.
Expressividade: Permite definir modelos de banco de dados usando classes Python, tornando o código mais expressivo e fácil de entender.
Flexibilidade: Suporta uma variedade de abordagens de mapeamento objeto-relacional (ORM), proporcionando flexibilidade na escolha do estilo de programação.

## Endpoints

Endpoints definem todas as operações CRUD que podem ser realizadas em entidades de Pessoa:

- GET `/docs` - Documentação do OpenAPI (gerado pelo FastAPI)
- GET `/redoc` - Documentação do Redocly (gerado pelo FastAPI)
- GET /pessoas - listar todas as pessoas disponíveis
- GET /pessoas/{person_id} - obter uma única pessoa pelo seu ID único
- POST /pessoas - criar uma nova pessoa
- PATCH /pessoas/{person_id} - atualizar uma pessoa existente
- DELETE /pessoas/{person_id} - excluir uma pessoa existente

## Instalação

Para executar este projeto localmente, siga os seguintes passos:


1. **Clonar o repositório e crie o ambiente virtual:**

    ```bash
    git clone https://github.com/your-username/your-project.git
    cd your-project
    python -m venv .venv
    ```

1. **Ativar o ambiente virtual:**

    - Windows:

        ```bash
        .\venv\Scripts\activate
        ```

    - macOS/Linux:

        ```bash
        source venv/bin/activate
        ```

1. **Instalar as dependências:**

    ```bash
    pip install -r requirements.txt
    ```

1. **Rode o servidor localmente:**

    ```bash
    uvicorn app.main:app --reload
    ```

Estrutura do Projeto
A estrutura do projeto está organizada da seguinte forma:

## Estrutura do Projeto

A estrutura do projeto está organizada da seguinte forma:

- `app/`: Contém o código principal do projeto.
  - `__init__.py`: Torna o diretório `app` um pacote Python.
  - `crud.py`: Contém operações CRUD.
  - `database.py`: Gerencia a conexão com o banco de dados.
  - `main.py`: Ponto de entrada principal para o projeto.
  - `models.py`: Define modelos SQLAlchemy.
  - `routers/`: Contém roteadores adicionais.
- `venv/`: Diretório do ambiente virtual.
- `requirements.txt`: Lista de dependências do projeto.
- `.flake8`: Arquivo de configuração para o Flake8.
- `.pre-commit-config.yaml`: Arquivo de configuração para ganchos pré-commit.
