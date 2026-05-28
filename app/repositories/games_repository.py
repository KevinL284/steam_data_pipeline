"""
Repository layer for games database queries.
"""

import logging

import pandas as pd
from sqlalchemy import create_engine, text

from app.core.config import DATABASE_URL

logger = logging.getLogger(__name__)

engine = create_engine(DATABASE_URL)


def get_all_games(limit: int = 10, offset: int = 0):
    logger.info("Buscando jogos com paginação. limit=%s, offset=%s", limit, offset)

    query = text("""
        SELECT *
        FROM games
        LIMIT :limit
        OFFSET :offset
    """)

    return pd.read_sql(
        query,
        engine,
        params={
            "limit": limit,
            "offset": offset,
        },
    )


def get_games_under_price(price: float):
    logger.info("Buscando jogos com preço final até %s", price)

    query = text("""
        SELECT *
        FROM games
        WHERE final_price <= :price
        ORDER BY final_price ASC
    """)

    return pd.read_sql(
        query,
        engine,
        params={
            "price": price,
        },
    )


def get_top_discounts(discount: float = 0):
    logger.info("Buscando jogos com desconto acima de %s", discount)

    query = text("""
        SELECT *
        FROM games
        WHERE discount_percent > :discount
        ORDER BY discount_percent DESC
        LIMIT 10
    """)

    return pd.read_sql(
        query,
        engine,
        params={
            "discount": discount,
        },
    )


def search_games_by_name(name: str):
    logger.info("Buscando jogos pelo nome: %s", name)

    query = text("""
        SELECT *
        FROM games
        WHERE LOWER(name) LIKE LOWER(:search)
    """)

    return pd.read_sql(
        query,
        engine,
        params={
            "search": f"%{name}%",
        },
    )


def get_games_by_platform(platform: str):
    logger.info("Buscando jogos pela plataforma: %s", platform)

    allowed_platforms = {
        "windows": "windows_available",
        "mac": "mac_available",
        "linux": "linux_available",
    }

    column = allowed_platforms.get(platform.lower())

    if column is None:
        logger.warning("Plataforma inválida recebida: %s", platform)
        return None

    query = text(f"""
        SELECT *
        FROM games
        WHERE {column} = 1
    """)

    return pd.read_sql(query, engine)


def get_games_with_controller_support():
    logger.info("Buscando jogos com suporte completo a controle")

    query = text("""
        SELECT *
        FROM games
        WHERE controller_support = 'full'
    """)

    return pd.read_sql(query, engine)


def get_games_stats():
    logger.info("Buscando estatísticas gerais dos jogos")

    query = text("""
        SELECT
            COUNT(*) AS total_games,
            ROUND(AVG(discount_percent), 2) AS average_discount,
            MAX(discount_percent) AS highest_discount,
            MIN(final_price) AS cheapest_price,
            ROUND(AVG(final_price), 2) AS average_price
        FROM games
    """)

    return pd.read_sql(query, engine)
