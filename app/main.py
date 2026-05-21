"""
Aplicação MAIN FastAPI
"""

from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(
    title="Pipeline de dados Steam API"
)

app.include_router(router)


