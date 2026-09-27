import pandas as pd


def validate_weather_data(df: pd.DataFrame):
    if df.empty:
        raise ValueError("DataFrame is empty")

    required_columns = {
        "city_id",
        "temperature",
        "humidity",
        "wind_speed",
        "observed_at",
    }

    missing_columns = required_columns - set(df.columns)

    if missing_columns:
        raise ValueError(
            f"Missing columns: {missing_columns}"
        )

    if df["city_id"].isnull().any():
        raise ValueError("city_id cannot be null")

    if df["temperature"].isnull().any():
        raise ValueError("temperature cannot be null")

    if df["humidity"].isnull().any():
        raise ValueError("humidity cannot be null")

    if df["wind_speed"].isnull().any():
        raise ValueError("wind_speed cannot be null")

    if ((df["humidity"] < 0) | (df["humidity"] > 100)).any():
        raise ValueError(
            "Humidity must be between 0 and 100"
        )

    if (df["wind_speed"] < 0).any():
        raise ValueError(
            "Wind speed cannot be negative"
        )

    parsed_dates = pd.to_datetime(
        df["observed_at"],
        errors="coerce",
    )

    if parsed_dates.isnull().any():
        raise ValueError(
            "Invalid observed_at"
        )

    return True