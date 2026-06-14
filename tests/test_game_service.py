from unittest.mock import patch

import pandas as pd

from app.services.game_service import GameService


def make_mock_dataframe():
    return pd.DataFrame(
        [
            {
                "id": 1,
                "name": "Cyberpunk 2077",
                "discount_percent": 50,
                "original_price": 199.99,
                "final_price": 99.99,
                "windows_available": True,
                "mac_available": False,
                "linux_available": False,
                "controller_support": "full",
            }
        ]
    )


def make_expected_games_response():
    return [
        {
            "id": 1,
            "name": "Cyberpunk 2077",
            "discount_percent": 50,
            "original_price": 199.99,
            "final_price": 99.99,
            "windows_available": True,
            "mac_available": False,
            "linux_available": False,
            "controller_support": "full",
        }
    ]


# Vamos começar os testes:


@patch("app.services.game_service.get_all_games")
def test_list_games_returns_serialized_games(mock_get_all_games):
    mock_df = make_mock_dataframe()
    mock_get_all_games.return_value = mock_df

    result = GameService.list_games(limit=5, offset=10)

    assert result == make_expected_games_response()
    mock_get_all_games.assert_called_once_with(limit=5, offset=10)


@patch("app.services.game_service.get_games_under_price")
def test_list_games_under_price_returns_serialized_games(mock_get_games_under_price):
    mock_df = make_mock_dataframe()
    mock_get_games_under_price.return_value = mock_df

    result = GameService.list_games_under_price(price=50.0)

    assert result == make_expected_games_response()
    mock_get_games_under_price.assert_called_once_with(50.0)


@patch("app.services.game_service.get_top_discounts")
def test_list_top_discounts_returns_serialized_games(mock_get_top_discounts):
    mock_df = make_mock_dataframe()
    mock_get_top_discounts.return_value = mock_df

    result = GameService.list_top_discounts(discount=30.0)

    assert result == make_expected_games_response()
    mock_get_top_discounts.assert_called_once_with(30.0)


@patch("app.services.game_service.search_games_by_name")
def test_search_games_returns_serialized_games(mock_search_games_by_name):
    mock_df = make_mock_dataframe()
    mock_search_games_by_name.return_value = mock_df

    result = GameService.search_games(name="cyberpunk")

    assert result == make_expected_games_response()
    mock_search_games_by_name.assert_called_once_with("cyberpunk")


@patch("app.services.game_service.get_games_by_platform")
def test_list_games_by_platform_returns_serialized_games(mock_get_games_by_platform):
    mock_df = make_mock_dataframe()
    mock_get_games_by_platform.return_value = mock_df

    result = GameService.list_games_by_platform(platform="windows")

    assert result == make_expected_games_response()
    mock_get_games_by_platform.assert_called_once_with("windows")


@patch("app.services.game_service.get_games_by_platform")
def test_list_games_by_invalid_platform_returns_none(mock_get_games_by_platform):
    mock_get_games_by_platform.return_value = None

    result = GameService.list_games_by_platform(platform="xbox")

    assert result is None
    mock_get_games_by_platform.assert_called_once_with("xbox")


@patch("app.services.game_service.get_games_with_controller_support")
def test_list_games_with_controller_support_returns_serialized_games(
    mock_get_games_with_controller_support,
):
    mock_df = make_mock_dataframe()
    mock_get_games_with_controller_support.return_value = mock_df

    result = GameService.list_games_with_controller_support()

    assert result == make_expected_games_response()
    mock_get_games_with_controller_support.assert_called_once_with()


@patch("app.services.game_service.get_games_stats")
def test_list_stats_returns_serialized_stats(mock_get_games_stats):
    mock_df = pd.DataFrame(
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
    mock_get_games_stats.return_value = mock_df

    result = GameService.list_stats()

    assert result == {
        "total_games": 1,
        "average_discount": 50.0,
        "highest_discount": 50,
        "cheapest_price": 99.99,
        "average_price": 99.99,
    }
    mock_get_games_stats.assert_called_once_with()
