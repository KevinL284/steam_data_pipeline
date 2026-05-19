"""
Só pro pylint parar de gritar:
Steam API extraction module.
"""

import requests

STEAM_FEATURED_URL = "https://store.steampowered.com/api/featuredcategories/"

def fetch_featured_games():
    try:
        response = requests.get(
        STEAM_FEATURED_URL,
        timeout = 10
      )
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.Timeout:
        print("Requisição excedeu o tempo limete.")
    except requests.exceptions.HTTPError as error:
        print(f"HTTP Error: {error}")
    except requests.exceptions.RequestException as error:
        print(f"Falha na requisição: {error}")
    except ValueError:
        print("JSON inválido recebido.")
    return None
