from unittest.mock import patch

import pandas as pd

from app.repositories.games_repository import (
    get_all_games,
    get_games_by_platform,
    get_games_stats,
    get_games_under_price,
    get_games_with_controller_support,
    get_top_discounts,
    search_games_by_name,
)


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


@patch("app.repositories.games_repository.pd.read_sql")
def test_get_all_games_calls_read_sql_with_pagination(mock_read_sql):
    mock_df = make_mock_dataframe()
    mock_read_sql.return_value = mock_df

    result = get_all_games(limit=5, offset=10)

    assert result.equals(mock_df)
    mock_read_sql.assert_called_once()

    _, kwargs = mock_read_sql.call_args

    assert kwargs["params"] == {
        "limit": 5,
        "offset": 10,
    }


@patch("app.repositories.games_repository.pd.read_sql")
def test_get_games_under_price_calls_read_sql_with_price(mock_read_sql):
    mock_df = make_mock_dataframe()
    mock_read_sql.return_value = mock_df

    result = get_games_under_price(price=50.0)

    assert result.equals(mock_df)
    mock_read_sql.assert_called_once()

    _, kwargs = mock_read_sql.call_args

    assert kwargs["params"] == {"price": 50.0}


@patch("app.repositories.games_repository.pd.read_sql")
def test_get_top_discounts_calls_read_sql_with_discount(mock_read_sql):
    mock_df = make_mock_dataframe()
    mock_read_sql.return_value = mock_df

    result = get_top_discounts(discount=30.0)

    assert result.equals(mock_df)
    mock_read_sql.assert_called_once()

    _, kwargs = mock_read_sql.call_args

    assert kwargs["params"] == {"discount": 30.0}


@patch("app.repositories.games_repository.pd.read_sql")
def test_search_games_by_name_calls_read_sql_with_search_param(mock_read_sql):
    mock_df = make_mock_dataframe()
    mock_read_sql.return_value = mock_df

    result = search_games_by_name(name="cyberpunk")

    assert result.equals(mock_df)
    mock_read_sql.assert_called_once()

    _, kwargs = mock_read_sql.call_args

    assert kwargs["params"] == {"search": "%cyberpunk%"}


@patch("app.repositories.games_repository.pd.read_sql")
def test_get_games_by_valid_platform_calls_read_sql(mock_read_sql):
    mock_df = make_mock_dataframe()
    mock_read_sql.return_value = mock_df

    result = get_games_by_platform(platform="windows")

    assert result.equals(mock_df)
    mock_read_sql.assert_called_once()


@patch("app.repositories.games_repository.pd.read_sql")
def test_get_games_by_invalid_platform_returns_none(mock_read_sql):
    result = get_games_by_platform(platform="xbox")

    assert result is None
    mock_read_sql.assert_not_called()


@patch("app.repositories.games_repository.pd.read_sql")
def test_get_games_with_controller_support_calls_read_sql(mock_read_sql):
    mock_df = make_mock_dataframe()
    mock_read_sql.return_value = mock_df

    result = get_games_with_controller_support()

    assert result.equals(mock_df)
    mock_read_sql.assert_called_once()


@patch("app.repositories.games_repository.pd.read_sql")
def test_get_games_stats_calls_read_sql(mock_read_sql):
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
    mock_read_sql.return_value = mock_df

    result = get_games_stats()

    assert result.equals(mock_df)
    mock_read_sql.assert_called_once()
