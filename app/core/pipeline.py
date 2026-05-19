import json

from app.extract.steam_api import fetch_featured_games
from app.transform.clean_data import transform_games_data


def run_pipeline():
    data = fetch_featured_games()
    if data is None:
        print("Pipeline falhou ao extrair os dados.")
        return

    print("Pipeline executado com sucesso. Dados extraídos:")

    df = transform_games_data(data)
    print(df.head())
