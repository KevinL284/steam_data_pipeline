"""
Módulo de rotas da API.
"""

import logging

from fastapi import APIRouter, HTTPException

from app.repositories.games_repository import (
    get_all_games,
    get_games_under_price,
    get_top_discounts,
    search_games_by_name,
    get_games_by_platform,
    get_games_with_controller_support,
    get_games_stats,
)
from app.schemas.game_schema import GameResponse, StatsResponse
from app.utils.serializer import dataframe_to_json

logger = logging.getLogger(__name__)

router = APIRouter()


@router.get("/games", response_model=list[GameResponse])
def list_games(limit: int = 10, offset: int = 0):
    """
    Retorna jogos com paginação.
    """

    logger.info("Requisição recebida em /games. limit=%s, offset=%s", limit, offset)

    df = get_all_games(limit=limit, offset=offset)

    return dataframe_to_json(df)


@router.get("/games/under/{price}", response_model=list[GameResponse])
def list_games_under_price(price: float):
    """
    Retorna jogos abaixo de determinado preço.
    """

    logger.info("Requisição recebida em /games/under/%s", price)

    df = get_games_under_price(price)

    return dataframe_to_json(df)


@router.get("/games/top-discounts", response_model=list[GameResponse])
def list_top_discounts(discount: float = 0):
    """
    Retorna jogos com maiores descontos.
    """

    logger.info("Requisição recebida em /games/top-discounts. discount=%s", discount)

    df = get_top_discounts(discount)

    return dataframe_to_json(df)


@router.get("/games/search/{name}", response_model=list[GameResponse])
def search_games(name: str):
    """
    Busca jogos pelo nome.
    """

    logger.info("Requisição recebida em /games/search/%s", name)

    df = search_games_by_name(name)

    return dataframe_to_json(df)


@router.get("/games/platform/{platform}", response_model=list[GameResponse])
def list_games_by_platform(platform: str):
    """
    Retorna jogos disponíveis em uma plataforma.
    """

    logger.info("Requisição recebida em /games/platform/%s", platform)

    df = get_games_by_platform(platform)

    if df is None:
        logger.warning("Plataforma inválida informada na rota: %s", platform)

        raise HTTPException(
            status_code=400,
            detail="Invalid platform. Use: windows, mac or linux."
        )

    return dataframe_to_json(df)


@router.get("/games/controller-support", response_model=list[GameResponse])
def list_games_with_controller_support():
    """
    Retorna jogos com suporte completo a controle.
    """

    logger.info("Requisição recebida em /games/controller-support")

    df = get_games_with_controller_support()

    return dataframe_to_json(df)


@router.get("/stats", response_model=StatsResponse)
def list_stats():
    """
    Retorna estatísticas gerais dos jogos.
    """

    logger.info("Requisição recebida em /stats")

    df = get_games_stats()

    return dataframe_to_json(df)[0]
