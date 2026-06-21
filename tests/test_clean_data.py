"""
Tests for data transformation layer.
"""

from unittest.mock import patch

import pandas as pd

from app.transform.clean_data import transform_games_data


def make_valid_steam_data():
    """
    Create valid Steam API-like payload for transformation tests.
    """

    return {
        "specials": {
            "items": [
                {
                    "id": 10,
                    "name": "Test Game",
                    "discount_percent": 50,
                    "original_price": 1000,
                    "final_price": 500,
                    "currency": "BRL",
                    "windows_available": True,
                    "mac_available": False,
                    "linux_available": True,
                    "controller_support": "full",
                }
            ]
        }
    }


def test_transform_games_data_success():
    """
    Should transform valid Steam data into a cleaned DataFrame.
    """

    data = make_valid_steam_data()

    result = transform_games_data(data)

    assert isinstance(result, pd.DataFrame)
    assert not result.empty
    assert len(result) == 1

    assert result.iloc[0]["id"] == 10
    assert result.iloc[0]["name"] == "Test Game"
    assert result.iloc[0]["discount_percent"] == 50
    assert result.iloc[0]["original_price"] == 10
    assert result.iloc[0]["final_price"] == 5
    assert result.iloc[0]["currency"] == "BRL"


@patch("app.transform.clean_data.logger")
def test_transform_games_data_key_error(mock_logger):
    """
    Should return an empty DataFrame and log an error when payload structure is invalid.
    """

    invalid_data = {}

    result = transform_games_data(invalid_data)

    assert isinstance(result, pd.DataFrame)
    assert result.empty

    mock_logger.error.assert_called_once()


@patch("app.transform.clean_data.logger")
@patch("app.transform.clean_data.pd.DataFrame")
def test_transform_games_data_unexpected_error(
    mock_dataframe,
    mock_logger,
):
    """
    Should return an empty DataFrame and log an error when an
    unexpected exception occurs.
    """
    data = make_valid_steam_data()
    empty_df = pd.core.frame.DataFrame()

    mock_dataframe.side_effect = [Exception("Unexpected Error"), empty_df]

    result = transform_games_data(data)

    assert result is empty_df
    assert result.empty

    mock_logger.error.assert_called_once()
