from app.transform.clean_data import transform_games_data


def test_transform_games_data_returns_dataframe_with_expected_columns():
    data = {
        "specials": {
            "items": [
                {
                    "id": 1,
                    "name": "Test Game",
                    "discount_percent": 50,
                    "original_price": 1999,
                    "final_price": 999,
                    "currency": "BRL",
                    "windows_available": True,
                    "mac_available": False,
                    "linux_available": True,
                    "controller_support": "full",
                }
            ]
        }
    }

    df = transform_games_data(data)

    assert len(df) == 1
    assert df.iloc[0]["name"] == "Test Game"
    assert df.iloc[0]["original_price"] == 19.99
    assert df.iloc[0]["final_price"] == 9.99
    assert "windows_available" in df.columns
    assert "mac_available" in df.columns
    assert "linux_available" in df.columns
