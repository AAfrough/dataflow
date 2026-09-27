from src.database.loader import (
    get_all_cities,
    load_weather_data,
)
from src.ingestion.weather_api import fetch_weather
from src.transformation.weather_transform import transform_weather_data
from logs.logger import logger


def run_pipeline():
    logger.info("Pipeline started.")

    cities = get_all_cities()

    for city in cities:
        city_name = city["name"]

        try:
            logger.info(f"Processing {city_name}...")

            data = fetch_weather(
                latitude=city["latitude"],
                longitude=city["longitude"],
            )

            df = transform_weather_data(
                data=data,
                city_id=city["id"],
            )

            load_weather_data(df)

            logger.info(
                f"{city_name} completed successfully."
            )

        except Exception:
            logger.exception(
                f"Pipeline failed for {city_name}."
            )

    logger.info("Pipeline finished.")


if __name__ == "__main__":
    run_pipeline()