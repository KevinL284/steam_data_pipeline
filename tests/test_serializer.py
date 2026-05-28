import pandas as pd

from app.utils.serializer import dataframe_to_json


def test_dataframe_to_json_converts_dataframe_to_list_of_dicts():
    df = pd.DataFrame(
        [
            {
                "id": 1,
                "name": "Test Game",
                "price": 9.99,
            }
        ]
    )

    result = dataframe_to_json(df)

    assert isinstance(result, list)
    assert result[0]["id"] == 1
    assert result[0]["name"] == "Test Game"
    assert result[0]["price"] == 9.99


def test_dataframe_to_json_converts_nan_to_none():
    df = pd.DataFrame(
        [
            {
                "id": 1,
                "name": None,
            }
        ]
    )

    result = dataframe_to_json(df)

    assert result[0]["name"] is None
