"""
Repository layer for games database queries.
"""

import pandas as pd
from sqlalchemy import create_engine, text

from app.core.config import DATABASE_URL


engine = create_engine(DATABASE_URL)


def get_all_games(limit: int = 10, offset: int = 0):
    query = text("""
        SELECT *
        FROM games
        LIMIT :limit
        OFFSET :offset
    """)

    return pd.read_sql(query, engine, params={
        "limit": limit,
        "offset": offset,
    })


def get_games_under_price(price: float):
    query = text("""
        SELECT *
        FROM games
        WHERE final_price <= :price
        ORDER BY final_price ASC
    """)

    return pd.read_sql(query, engine, params={
        "price": price,
    })


def get_top_discounts(discount: float = 0):
    query = text("""
        SELECT *
        FROM games
        WHERE discount_percent > :discount
        ORDER BY discount_percent DESC
        LIMIT 10
    """)

    return pd.read_sql(query, engine, params={
        "discount": discount,
    })


def search_games_by_name(name: str):
    query = text("""
        SELECT *
        FROM games
        WHERE LOWER(name) LIKE LOWER(:search)
    """)

    return pd.read_sql(query, engine, params={
        "search": f"%{name}%",
    })


def get_games_by_platform(platform: str):
    allowed_platforms = {
        "windows": "windows_available",
        "mac": "mac_available",
        "linux": "linux_available",
    }

    column = allowed_platforms.get(platform.lower())

    if column is None:
        return None

    query = text(f"""
        SELECT *
        FROM games
        WHERE {column} = 1
    """)

    return pd.read_sql(query, engine)


def get_games_with_controller_support():
    query = text("""
        SELECT *
        FROM games
        WHERE controller_support = 'full'
    """)

    return pd.read_sql(query, engine)


def get_games_stats():
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
