import requests

from src.config import (
    WEATHER_API_URL,
    WEATHER_API_TIMEOUT,
)


def fetch_weather(latitude, longitude):
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current": (
            "temperature_2m,"
            "relative_humidity_2m,"
            "wind_speed_10m"
        ),
    }

    response = requests.get(
        WEATHER_API_URL,
        params=params,
        timeout=WEATHER_API_TIMEOUT,
    )

    response.raise_for_status()

    return response.json()