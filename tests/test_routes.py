from unittest.mock import patch


@patch("app.api.routes.get_all_games")
def test_get_games_returns_200(
    mock_get_all_games,
    client,
    mock_games_dataframe,
):
    mock_get_all_games.return_value = mock_games_dataframe

    response = client.get("/games")

    assert response.status_code == 200
    assert isinstance(response.json(), list)


@patch("app.api.routes.get_games_stats")
def test_get_stats_returns_200(
    mock_get_games_stats,
    client,
    mock_stats_dataframe,
):
    mock_get_games_stats.return_value = mock_stats_dataframe

    response = client.get("/stats")

    assert response.status_code == 200
    assert isinstance(response.json(), dict)


@patch("app.api.routes.get_games_by_platform")
def test_get_games_by_valid_platform_returns_200(
    mock_get_games_by_platform,
    client,
    mock_games_dataframe,
):
    mock_get_games_by_platform.return_value = mock_games_dataframe

    response = client.get("/games/platform/windows")

    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_get_games_by_invalid_platform_returns_400(client):
    response = client.get("/games/platform/playstation")

    assert response.status_code == 400
    assert response.json()["detail"] == "Invalid platform. Use: windows, mac or linux."
