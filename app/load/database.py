"""
modulo de acesso ao DB
"""


from sqlalchemy import create_engine

DATABASE_URL = "sqlite:///data/games.db"

engine = create_engine(DATABASE_URL)
# Depois monto um env pra mais segurança de dados.

def save_games_data(df):
  """
  Salva os dados do DataFrame no banco de dados.
  """

  df.to_sql(
    "games",
    con=engine,
    if_exists="replace",
    index=False
  )

print("Dados salvos com sucesso no banco de dados.")


