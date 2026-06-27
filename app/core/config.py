"""
modulo para configuração da aplicação
"""

import os

from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
ALEMBIC_DATABASE_URL = os.getenv("ALEMBIC_DATABASE_URL", DATABASE_URL)
STEAM_API_URL = os.getenv("STEAM_API_URL")
REQUEST_TIMEOUT = int(os.getenv("REQUEST_TIMEOUT", 10))
