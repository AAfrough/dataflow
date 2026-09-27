from psycopg2.extras import execute_values

from src.database.connection import get_connection


def get_all_cities():
    connection = get_connection()

    try:
        with connection.cursor() as cursor:
            query = """
                SELECT id, name, latitude, longitude
                FROM cities
                ORDER BY id;
            """

            cursor.execute(query)

            rows = cursor.fetchall()

            return [
                {
                    "id": row[0],
                    "name": row[1],
                    "latitude": float(row[2]),
                    "longitude": float(row[3]),
                }
                for row in rows
            ]

    finally:
        connection.close()


def get_city(city_name):
    connection = get_connection()

    try:
        with connection.cursor() as cursor:
            query = """
                SELECT id, name, latitude, longitude
                FROM cities
                WHERE name = %s;
            """

            cursor.execute(query, (city_name,))

            result = cursor.fetchone()

            if result is None:
                raise ValueError(f"City not found: {city_name}")

            return {
                "id": result[0],
                "name": result[1],
                "latitude": float(result[2]),
                "longitude": float(result[3]),
            }

    finally:
        connection.close()


def load_weather_data(df):
    connection = get_connection()

    try:
        with connection.cursor() as cursor:
            query = """
                    INSERT INTO weather_observations
                        (
                            city_id,
                            temperature,
                            humidity,
                            wind_speed,
                            observed_at
                        )
                    VALUES %s
                    ON CONFLICT (city_id, observed_at)
                    DO UPDATE SET
                        temperature = EXCLUDED.temperature,
                        humidity = EXCLUDED.humidity,
                        wind_speed = EXCLUDED.wind_speed;
                    """
            values = [
                (
                    row.city_id,
                    row.temperature,
                    row.humidity,
                    row.wind_speed,
                    row.observed_at,
                )
                for row in df.itertuples(index=False)
            ]

            execute_values(cursor, query, values)

        connection.commit()

    except Exception:
        connection.rollback()
        raise

    finally:
        connection.close()