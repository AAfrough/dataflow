CREATE TABLE IF NOT EXISTS cities (
    id BIGSERIAL PRIMARY KEY,
    name VARCHAR NOT NULL,
    country VARCHAR NOT NULL,
    latitude NUMERIC,
    longitude NUMERIC
);


CREATE TABLE IF NOT EXISTS weather_observations (
    id BIGSERIAL PRIMARY KEY,
    temperature NUMERIC,
    humidity NUMERIC,
    wind_speed NUMERIC,
    observed_at TIMESTAMP NOT NULL,
    city_id BIGINT,
    
    CONSTRAINT fk_weather_city
        FOREIGN KEY (city_id)
        REFERENCES cities(id),

    CONSTRAINT unique_city_observation
        UNIQUE (city_id, observed_at),

    CONSTRAINT check_humidity
        CHECK (humidity >= 0 AND humidity <= 100),

    CONSTRAINT check_wind_speed
        CHECK (wind_speed >= 0)
);


CREATE INDEX IF NOT EXISTS idx_weather_city
ON weather_observations(city_id);