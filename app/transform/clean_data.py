
"""
Modulo de transformação de dados.
"""

import pandas as pd


def transform_games_data(data):
    """
    Vai transformar os dados em um dataframe mais limpo.
    """

    specials = data["specials"]["items"]

    rows = []

    for game in specials:
        rows.append({
            "id": game.get("id"),
            "name": game.get("name"),
            "discount_percent": game.get("discount_percent"),
            "original_price": game.get("original_price", 0) / 100,
            "final_price": game.get("final_price", 0) / 100,
            "currency": game.get("currency"),
            "windows_avaible": game.get("windows_available"),
            "mac_avaible": game.get("mac_available"),
            "linux_avaible": game.get("linux_available"),
            "controller_support": game.get("controller_support"),
        })

    df = pd.DataFrame(rows)
    return df
