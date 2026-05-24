from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_get_games_returns_200():
    response = client.get("/games")

    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_get_stats_returns_200():
    response = client.get("/stats")

    assert response.status_code == 200
    assert isinstance(response.json(), dict)


def test_get_games_by_valid_platform_returns_200():
    response = client.get("/games/platform/windows")

    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_get_games_by_invalid_platform_returns_400():
    response = client.get("/games/platform/playstation")

    assert response.status_code == 400
    assert response.json()["detail"] == "Invalid platform. Use: windows, mac or linux."
