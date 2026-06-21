"""
Tests for database persistence layer.
"""

from unittest.mock import MagicMock, patch

from app.load.database import engine, save_games_data


def test_save_games_data_success():
    """
    Should save data successfully using to_sql.
    """

    mock_df = MagicMock()

    save_games_data(mock_df)

    mock_df.to_sql.assert_called_once_with(
        "games",
        con=engine,
        if_exists="replace",
        index=False,
    )


@patch("app.load.database.logger")
def test_save_games_data_exception(mock_logger):
    """
    Should log an error when persistence fails.
    """

    mock_df = MagicMock()
    mock_df.to_sql.side_effect = Exception("Database Error")

    save_games_data(mock_df)

    mock_df.to_sql.assert_called_once()

    mock_logger.error.assert_called_once()
