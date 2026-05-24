"""
Database access module.
"""

from sqlalchemy import create_engine

from app.core.config import DATABASE_URL


engine = create_engine(DATABASE_URL)


def save_games_data(df):
    """
    Save DataFrame data into the database.
    """

    df.to_sql(
        "games",
        con=engine,
        if_exists="replace",
        index=False
    )

    print("Dados salvos com sucesso no banco de dados.")
