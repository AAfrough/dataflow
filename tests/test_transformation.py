from src.transformation.weather_transform import (
    transform_weather_data,
)


def test_transform_weather_data():

    data = {
        "current": {
            "time": "2026-08-11T10:00",
            "temperature_2m": 30.5,
            "relative_humidity_2m": 45,
            "wind_speed_10m": 12.3,
        }
    }

    df = transform_weather_data(
        data=data,
        city_id=1,
    )

    assert len(df) == 1
    assert df.iloc[0]["city_id"] == 1
    assert df.iloc[0]["temperature"] == 30.5
    assert df.iloc[0]["humidity"] == 45
    assert df.iloc[0]["wind_speed"] == 12.3


import pytest

from src.transformation.weather_transform import (
    transform_weather_data,
)


def test_invalid_humidity():
    data = {
        "current": {
            "time": "2026-08-11T10:00",
            "temperature_2m": 30.5,
            "relative_humidity_2m": 150,
            "wind_speed_10m": 12.3,
        }
    }

    with pytest.raises(ValueError):
        transform_weather_data(
            data=data,
            city_id=1,
        )

def test_invalid_wind_speed():
    data = {
        "current": {
            "time": "2026-08-11T10:00",
            "temperature_2m": 30.5,
            "relative_humidity_2m": 45,
            "wind_speed_10m": -10,
        }
    }

    with pytest.raises(ValueError):
        transform_weather_data(
            data=data,
            city_id=1,
        )