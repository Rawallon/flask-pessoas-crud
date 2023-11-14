from fastapi import FastAPI
from app import models, fill_db

from app.database import engine
from app.routers.pessoas import pessoasRouter

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

fill_db.fill_db()
app = FastAPI(
    title="Pessoas Conhecidas Inc.", description="Lista todas as pessoas conhecidas"
)
app.include_router(pessoasRouter, prefix="", tags=["pessoa"])
