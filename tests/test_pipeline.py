from unittest.mock import patch

import pandas as pd

from app.core.pipeline import run_pipeline


@patch("app.core.pipeline.save_games_data")
@patch("app.core.pipeline.transform_games_data")
@patch("app.core.pipeline.fetch_featured_games")
def test_run_pipeline_executes_etl_successfully(
    mock_fetch_featured_games,
    mock_transform_games_data,
    mock_save_games_data,
):
    mock_data = {"featured_win": [{"id": 1, "name": "Cyberpunk 2077"}]}
    mock_df = pd.DataFrame([{"id": 1, "name": "Cyberpunk 2077"}])

    mock_fetch_featured_games.return_value = mock_data
    mock_transform_games_data.return_value = mock_df

    run_pipeline()

    mock_fetch_featured_games.assert_called_once_with()
    mock_transform_games_data.assert_called_once_with(mock_data)
    mock_save_games_data.assert_called_once_with(mock_df)


@patch("app.core.pipeline.save_games_data")
@patch("app.core.pipeline.transform_games_data")
@patch("app.core.pipeline.fetch_featured_games")
def test_run_pipeline_stops_when_extraction_fails(
    mock_fetch_featured_games,
    mock_transform_games_data,
    mock_save_games_data,
):
    mock_fetch_featured_games.return_value = None

    run_pipeline()

    mock_fetch_featured_games.assert_called_once_with()
    mock_transform_games_data.assert_not_called()
    mock_save_games_data.assert_not_called()


@patch("app.core.pipeline.save_games_data")
@patch("app.core.pipeline.transform_games_data")
@patch("app.core.pipeline.fetch_featured_games")
def test_run_pipeline_stops_when_dataframe_is_empty(
    mock_fetch_featured_games,
    mock_transform_games_data,
    mock_save_games_data,
):
    mock_data = {"featured_win": []}
    empty_df = pd.DataFrame()

    mock_fetch_featured_games.return_value = mock_data
    mock_transform_games_data.return_value = empty_df

    run_pipeline()

    mock_fetch_featured_games.assert_called_once_with()
    mock_transform_games_data.assert_called_once_with(mock_data)
    mock_save_games_data.assert_not_called()
