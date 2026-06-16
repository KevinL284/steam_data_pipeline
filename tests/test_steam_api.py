from unittest.mock import Mock, patch

import requests

from app.core.config import REQUEST_TIMEOUT, STEAM_API_URL
from app.extract.steam_api import fetch_featured_games


@patch("app.extract.steam_api.requests.get")
def test_fetch_featured_games_returns_json_when_request_succeeds(mock_get):
    expected_data = {
        "featured_win": [
            {
                "id": 1,
                "name": "Cyberpunk 2077",
            }
        ]
    }

    mock_response = Mock()
    mock_response.json.return_value = expected_data
    mock_response.raise_for_status.return_value = None
    mock_get.return_value = mock_response

    result = fetch_featured_games()

    assert result == expected_data
    mock_get.assert_called_once_with(STEAM_API_URL, timeout=REQUEST_TIMEOUT)
    mock_response.raise_for_status.assert_called_once_with()
    mock_response.json.assert_called_once_with()


@patch("app.extract.steam_api.requests.get")
def test_fetch_featured_games_returns_none_on_timeout(mock_get):
    mock_get.side_effect = requests.exceptions.Timeout

    result = fetch_featured_games()

    assert result is None
    mock_get.assert_called_once_with(STEAM_API_URL, timeout=REQUEST_TIMEOUT)


@patch("app.extract.steam_api.requests.get")
def test_fetch_featured_games_returns_none_on_http_error(mock_get):
    mock_response = Mock()
    mock_response.raise_for_status.side_effect = requests.exceptions.HTTPError(
        "HTTP error"
    )
    mock_get.return_value = mock_response

    result = fetch_featured_games()

    assert result is None
    mock_get.assert_called_once_with(STEAM_API_URL, timeout=REQUEST_TIMEOUT)
    mock_response.raise_for_status.assert_called_once_with()


@patch("app.extract.steam_api.requests.get")
def test_fetch_featured_games_returns_none_on_request_exception(mock_get):
    mock_get.side_effect = requests.exceptions.RequestException("Request failed")

    result = fetch_featured_games()

    assert result is None
    mock_get.assert_called_once_with(STEAM_API_URL, timeout=REQUEST_TIMEOUT)


@patch("app.extract.steam_api.requests.get")
def test_fetch_featured_games_returns_none_on_invalid_json(mock_get):
    mock_response = Mock()
    mock_response.raise_for_status.return_value = None
    mock_response.json.side_effect = ValueError

    mock_get.return_value = mock_response

    result = fetch_featured_games()

    assert result is None
    mock_get.assert_called_once_with(STEAM_API_URL, timeout=REQUEST_TIMEOUT)
    mock_response.raise_for_status.assert_called_once_with()
    mock_response.json.assert_called_once_with()
