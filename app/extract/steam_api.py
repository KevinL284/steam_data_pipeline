"""
Steam API extraction module.
"""

import logging

import requests

from app.core.config import REQUEST_TIMEOUT, STEAM_API_URL

logger = logging.getLogger(__name__)


def fetch_featured_games():
    """
    Fetch featured games data from Steam API.
    """

    logger.info("Iniciando extração de dados da Steam API")

    try:
        response = requests.get(
            STEAM_API_URL,
            timeout=REQUEST_TIMEOUT
        )

        logger.info("Requisição enviada para a Steam API")

        response.raise_for_status()

        logger.info("Dados recebidos com sucesso da Steam API")

        return response.json()

    except requests.exceptions.Timeout:
        logger.error("Requisição excedeu o tempo limite")

    except requests.exceptions.HTTPError as error:
        logger.error("Erro HTTP ao consumir Steam API: %s", error)

    except requests.exceptions.RequestException as error:
        logger.error("Falha na requisição para Steam API: %s", error)

    except ValueError:
        logger.error("JSON inválido recebido da Steam API")

    return None
