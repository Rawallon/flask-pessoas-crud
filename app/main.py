from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app import fill_db, models
from app.database import engine
from app.routers.frontend import router as frontRouter
from app.routers.pessoas import pessoasRouter

models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Pessoas Conhecidas Inc.", description="Lista todas as pessoas conhecidas"
)
app.mount("/static", StaticFiles(directory="app/static"), name="static")

fill_db.fill_db()
app.include_router(pessoasRouter, prefix="/api")
app.include_router(frontRouter, prefix="")
