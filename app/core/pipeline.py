import logging

from app.extract.steam_api import fetch_featured_games
from app.load.database import save_games_data
from app.transform.clean_data import transform_games_data

logger = logging.getLogger(__name__)


def run_pipeline():
    logger.info("Iniciando execução do pipeline ETL")

    data = fetch_featured_games()

    if data is None:
        logger.error("Pipeline interrompido: falha na extração dos dados")
        return

    logger.info("Dados extraídos com sucesso")

    df = transform_games_data(data)

    if df.empty:
        logger.warning("Pipeline interrompido: transformação retornou DataFrame vazio")
        return

    logger.info("Dados transformados com sucesso. Total de registros: %s", len(df))

    save_games_data(df)

    logger.info("Pipeline ETL executado com sucesso")
