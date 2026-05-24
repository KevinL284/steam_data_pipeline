"""
Database access module.
"""

import logging

from sqlalchemy import create_engine

from app.core.config import DATABASE_URL

logger = logging.getLogger(__name__)

engine = create_engine(DATABASE_URL)


def save_games_data(df):
    """
    Save DataFrame data into the database.
    """

    logger.info("Iniciando persistência dos dados no banco")

    try:
        df.to_sql(
            "games",
            con=engine,
            if_exists="replace",
            index=False
        )

        logger.info(
            "Dados salvos com sucesso no banco de dados. Total de registros: %s",
            len(df)
        )

    except Exception as error:
        logger.error(
            "Erro ao salvar dados no banco de dados: %s",
            error
        )
