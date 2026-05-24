"""
Módulo de rotas da API.
"""

from fastapi import APIRouter, HTTPException
from app.repositories.games_repository import (
    get_all_games,
    get_games_under_price,
    get_top_discounts,
    search_games_by_name,
    get_games_by_platform,
    get_games_with_controller_support,
    get_games_stats
)
from app.utils.serializer import dataframe_to_json
from app.schemas.game_schema import GameResponse, StatsResponse

router = APIRouter()


@router.get("/games", response_model=list[GameResponse])
def list_games(limit: int = 10, offset: int = 0):
    """
    Retorna jogos com paginação.
    """

    df = get_all_games(limit=limit, offset=offset)

    return dataframe_to_json(df)


@router.get("/games/under/{price}", response_model=list[GameResponse])
def list_games_under_price(price: float):
    """
    Retorna jogos abaixo de determinado preço.
    """

    df = get_games_under_price(price)

    return dataframe_to_json(df)


@router.get("/games/top-discounts", response_model=list[GameResponse])
def list_top_discounts(discount: float = 0):
    """
    Retorna jogos com maiores descontos.
    """

    df = get_top_discounts(discount)

    return dataframe_to_json(df)


@router.get("/games/search/{name}", response_model=list[GameResponse])
def search_games(name: str):
    """
    Busca jogos pelo nome.
    """

    df = search_games_by_name(name)

    return dataframe_to_json(df)


@router.get("/games/platform/{platform}", response_model=list[GameResponse])
def list_games_by_platform(platform: str):
    """
    Retorna jogos disponíveis em uma plataforma.
    """

    df = get_games_by_platform(platform)

    if df is None:
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

    df = get_games_with_controller_support()

    return dataframe_to_json(df)


@router.get("/stats", response_model=StatsResponse)
def list_stats():
    """
    Retorna estatísticas gerais dos jogos.
    """

    df = get_games_stats()

    return dataframe_to_json(df)[0]
