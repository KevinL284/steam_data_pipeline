"""
Steam API extraction module.
"""

import requests

from app.core.config import REQUEST_TIMEOUT, STEAM_API_URL


def fetch_featured_games():
    """
    Fetch featured games data from Steam API.
    """

    try:
        response = requests.get(
            STEAM_API_URL,
            timeout=REQUEST_TIMEOUT
        )

        response.raise_for_status()

        return response.json()

    except requests.exceptions.Timeout:
        print("Requisição excedeu o tempo limite.")

    except requests.exceptions.HTTPError as error:
        print(f"HTTP error: {error}")

    except requests.exceptions.RequestException as error:
        print(f"Falha na requisição: {error}")

    except ValueError:
        print("JSON inválido recebido.")

    return None
