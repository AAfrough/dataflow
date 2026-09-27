import os

from dotenv import load_dotenv


load_dotenv()


def require(value, name):
    if not value:
        raise ValueError(
            f"Missing required configuration: {name}"
        )

    return value


DB_HOST = require(
    os.getenv("DB_HOST"),
    "DB_HOST",
)

DB_PORT = require(
    os.getenv("DB_PORT"),
    "DB_PORT",
)

DB_NAME = require(
    os.getenv("DB_NAME"),
    "DB_NAME",
)

DB_USER = require(
    os.getenv("DB_USER"),
    "DB_USER",
)

DB_PASSWORD = require(
    os.getenv("DB_PASSWORD"),
    "DB_PASSWORD",
)

WEATHER_API_URL = require(
    os.getenv("WEATHER_API_URL"),
    "WEATHER_API_URL",
)

WEATHER_API_TIMEOUT = int(
    os.getenv("WEATHER_API_TIMEOUT", "10")
)