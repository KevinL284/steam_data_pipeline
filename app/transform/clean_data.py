"""
Modulo de transformação de dados.
"""

import logging

import pandas as pd

logger = logging.getLogger(__name__)


def transform_games_data(data):
    """
    Vai transformar os dados em um dataframe mais limpo.
    """

    logger.info("Iniciando transformação dos dados")

    try:
        specials = data["specials"]["items"]

        logger.info(
            "Quantidade de jogos recebidos para transformação: %s", len(specials)
        )

        rows = []

        for game in specials:
            rows.append(
                {
                    "id": game.get("id"),
                    "name": game.get("name"),
                    "discount_percent": game.get("discount_percent"),
                    "original_price": game.get("original_price", 0) / 100,
                    "final_price": game.get("final_price", 0) / 100,
                    "currency": game.get("currency"),
                    "windows_available": game.get("windows_available"),
                    "mac_available": game.get("mac_available"),
                    "linux_available": game.get("linux_available"),
                    "controller_support": game.get("controller_support"),
                }
            )

        df = pd.DataFrame(rows)

        logger.info(
            "Transformação concluída com sucesso. Total de registros: %s", len(df)
        )

        return df

    except KeyError as error:
        logger.error("Erro de estrutura nos dados recebidos: %s", error)

    except Exception as error:
        logger.error("Erro inesperado durante transformação dos dados: %s", error)

    return pd.DataFrame()
