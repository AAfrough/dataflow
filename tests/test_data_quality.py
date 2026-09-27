import pandas as pd
import pytest

from src.data_quality.checks import validate_weather_data


def create_valid_dataframe():
    return pd.DataFrame(
        [
            {
                "city_id": 1,
                "temperature": 30.5,
                "humidity": 45,
                "wind_speed": 12.3,
                "observed_at": "2026-08-11T10:00",
            }
        ]
    )


def test_valid_weather_data():
    df = create_valid_dataframe()

    assert validate_weather_data(df) is True


def test_invalid_humidity():
    df = create_valid_dataframe()
    df.loc[0, "humidity"] = 150

    with pytest.raises(ValueError):
        validate_weather_data(df)


def test_negative_wind_speed():
    df = create_valid_dataframe()
    df.loc[0, "wind_speed"] = -5

    with pytest.raises(ValueError):
        validate_weather_data(df)


def test_missing_city_id():
    df = create_valid_dataframe()
    df.loc[0, "city_id"] = None

    with pytest.raises(ValueError):
        validate_weather_data(df)


def test_invalid_timestamp():
    df = create_valid_dataframe()
    df.loc[0, "observed_at"] = "invalid-date"

    with pytest.raises(ValueError):
        validate_weather_data(df)