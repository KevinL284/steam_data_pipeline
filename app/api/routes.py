"""
Modulo de rotas da API
"""

from fastapi import APIRouter
from sqlalchemy import create_engine
import pandas as pd


from app.core.config import DATABASE_URL

router = APIRouter()
engine = create_engine(DATABASE_URL)

@router.get("/games")
def get_games():
    """
    Nosso primeiro Endpoint pra retornar os jogos
    """
    query = "SELECT * FROM games"
    df = pd.read_sql(query, engine)
    return (
        df.astype(object)
        .where(pd.notnull(df), None)
        .to_dict(orient="records")
    )  #vou testar isso no outro end point depois.

@router.get("/games/under/{price}")
def get_games_under_price(price: float):
    """
    Return games cheaper than a given price.
    """

    query = f"""
        SELECT *
        FROM games
        WHERE final_price <= {price}
    """

    df = pd.read_sql(query, engine)
    return df.fillna("")
    return df.to_dict(orient="records")
