"""
Aplicação MAIN FastAPI
"""

import logging

from fastapi import FastAPI

from app.api.routes import router
from app.core.logging_config import setup_logging

setup_logging()

logger = logging.getLogger(__name__)

app = FastAPI(title="Pipeline de dados Steam API")

app.include_router(router)

logger.info("Aplicação FastAPI inicializada")
