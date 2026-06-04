"""
Camada de serviço responsável pelas regras de negócio relacionadas a jogos.
"""

import logging

from app.repositories.games_repository import (
    get_all_games,
    get_games_by_platform,
    get_games_stats,
    get_games_under_price,
    get_games_with_controller_support,
    get_top_discounts,
    search_games_by_name,
)
from app.utils.serializer import dataframe_to_json

logger = logging.getLogger(__name__)


class GameService:
    """
    Serviço simples para jogos.

    Centraliza a comunicação entre as rotas da API e a camada de repository.
    """

    @staticmethod
    def list_games(limit: int = 10, offset: int = 0):
        logger.info("Buscando jogos paginados. limit=%s, offset=%s", limit, offset)
        df = get_all_games(limit=limit, offset=offset)
        return dataframe_to_json(df)

    @staticmethod
    def list_games_under_price(price: float):
        logger.info("Buscando jogos abaixo do preço: %s", price)

        df = get_games_under_price(price)

        return dataframe_to_json(df)

    @staticmethod
    def list_top_discounts(discount: float = 0):
        logger.info("Buscando jogos com desconto mínimo: %s", discount)

        df = get_top_discounts(discount)

        return dataframe_to_json(df)

    @staticmethod
    def search_games(name: str):
        logger.info("Buscando jogos pelo nome: %s", name)

        df = search_games_by_name(name)

        return dataframe_to_json(df)

    @staticmethod
    def list_games_by_platform(platform: str):
        logger.info("Buscando jogos pela plataforma: %s", platform)

        df = get_games_by_platform(platform)

        if df is None:
            logger.warning("Plataforma inválida informada: %s", platform)
            return None

        return dataframe_to_json(df)

    @staticmethod
    def list_games_with_controller_support():
        logger.info("Buscando jogos com suporte completo a controle.")

        df = get_games_with_controller_support()

        return dataframe_to_json(df)

    @staticmethod
    def list_stats():
        logger.info("Buscando estatísticas gerais dos jogos.")

        df = get_games_stats()

        return dataframe_to_json(df)[0]
