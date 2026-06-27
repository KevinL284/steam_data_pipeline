"""
Tests for database persistence layer.
"""

from unittest.mock import MagicMock, patch

from app.load.database import save_games_data


@patch("app.load.database.engine")
def test_save_games_data_success(mock_engine):
    """
    Should truncate table and append data successfully.
    """

    mock_df = MagicMock()

    mock_connection = MagicMock()

    mock_engine.begin.return_value.__enter__.return_value = mock_connection

    save_games_data(mock_df)

    mock_connection.execute.assert_called_once()

    mock_df.to_sql.assert_called_once_with(
        "games",
        con=mock_connection,
        if_exists="append",
        index=False,
    )


@patch("app.load.database.logger")
@patch("app.load.database.engine")
def test_save_games_data_exception(mock_engine, mock_logger):
    """
    Should log an error when persistence fails.
    """

    mock_df = MagicMock()

    mock_connection = MagicMock()

    mock_engine.begin.return_value.__enter__.return_value = mock_connection

    mock_df.to_sql.side_effect = Exception("Database Error")

    save_games_data(mock_df)

    mock_logger.error.assert_called_once()
