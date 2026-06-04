import pandas as pd
import pytest
from fastapi.testclient import TestClient

from app.main import app


@pytest.fixture
def client():
    return TestClient(app)


@pytest.fixture
def mock_games_dataframe():
    return pd.DataFrame(
        [
            {
                "id": 1,
                "name": "Cyberpunk 2077",
                "discount_percent": 50,
                "original_price": 199.99,
                "final_price": 99.99,
                "currency": "BRL",
                "windows_available": True,
                "mac_available": False,
                "linux_available": False,
                "controller_support": "full",
            }
        ]
    )


@pytest.fixture
def mock_stats_dataframe():
    return pd.DataFrame(
        [
            {
                "total_games": 1,
                "average_discount": 50.0,
                "highest_discount": 50,
                "cheapest_price": 99.99,
                "average_price": 99.99,
            }
        ]
    )
