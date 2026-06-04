"""
Módulo de rotas da API.
"""

import logging

from fastapi import APIRouter, HTTPException

from app.schemas.game_schema import GameResponse, StatsResponse
from app.services.game_service import GameService

logger = logging.getLogger(__name__)

router = APIRouter()


@router.get("/games", response_model=list[GameResponse])
def list_games(limit: int = 10, offset: int = 0):
    """
    Retorna jogos com paginação.
    """

    logger.info("Requisição recebida em /games. limit=%s, offset=%s", limit, offset)

    return GameService.list_games(limit=limit, offset=offset)


@router.get("/games/under/{price}", response_model=list[GameResponse])
def list_games_under_price(price: float):
    """
    Retorna jogos abaixo de determinado preço.
    """

    logger.info("Requisição recebida em /games/under/%s", price)

    return GameService.list_games_under_price(price=price)


@router.get("/games/top-discounts", response_model=list[GameResponse])
def list_top_discounts(discount: float = 0):
    """
    Retorna jogos com maiores descontos.
    """

    logger.info("Requisição recebida em /games/top-discounts. discount=%s", discount)

    return GameService.list_top_discounts(discount=discount)


@router.get("/games/search/{name}", response_model=list[GameResponse])
def search_games(name: str):
    """
    Busca jogos pelo nome.
    """

    logger.info("Requisição recebida em /games/search/%s", name)

    return GameService.search_games(name=name)


@router.get("/games/platform/{platform}", response_model=list[GameResponse])
def list_games_by_platform(platform: str):
    """
    Retorna jogos disponíveis em uma plataforma.
    """

    logger.info("Requisição recebida em /games/platform/%s", platform)

    games = GameService.list_games_by_platform(platform=platform)

    if games is None:
        logger.warning("Plataforma inválida informada na rota: %s", platform)

        raise HTTPException(
            status_code=400, detail="Invalid platform. Use: windows, mac or linux."
        )

    return games


@router.get("/games/controller-support", response_model=list[GameResponse])
def list_games_with_controller_support():
    """
    Retorna jogos com suporte completo a controle.
    """

    logger.info("Requisição recebida em /games/controller-support")

    return GameService.list_games_with_controller_support()


@router.get("/stats", response_model=StatsResponse)
def list_stats():
    """
    Retorna estatísticas gerais dos jogos.
    """

    logger.info("Requisição recebida em /stats")

    return GameService.list_stats()
