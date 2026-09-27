import pandas as pd

from src.data_quality.checks import validate_weather_data


def transform_weather_data(data, city_id):
    current = data["current"]

    transformed_data = {
        "city_id": city_id,
        "temperature": current["temperature_2m"],
        "humidity": current["relative_humidity_2m"],
        "wind_speed": current["wind_speed_10m"],
        "observed_at": current["time"],
    }

    df = pd.DataFrame([transformed_data])

    validate_weather_data(df)

    return df