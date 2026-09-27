DataFlow

A simple data engineering pipeline for collecting, transforming, validating, and storing weather data.

Overview

DataFlow fetches weather data from an external API, processes and validates the data, and stores the results in PostgreSQL.

Pipeline

Weather API
    ↓
Ingestion
    ↓
Transformation
    ↓
Data Quality Checks
    ↓
PostgreSQL

Tech Stack

- Python
- PostgreSQL
- Docker
- pytest
- REST API

Project Structure

DataFlow/
├── src/
│   ├── config/
│   ├── ingestion/
│   ├── transformation/
│   ├── database/
│   ├── data_quality/
│   └── pipeline.py
├── tests/
├── sql/
│   └── schema.sql
├── requirements.txt
└── README.md

Features

- Fetch weather data from an API
- Transform raw data into a consistent format
- Validate data quality
- Store weather observations in PostgreSQL
- Use primary keys, foreign keys, constraints, and unique records
- Automated tests with pytest
- PostgreSQL running in Docker

Setup

Create a ".env" file with the required configuration:

DB_HOST=localhost
DB_PORT=5433
DB_NAME=dataflow
DB_USER=dataflow
DB_PASSWORD=your_password

Install dependencies:

pip install -r requirements.txt

Run the tests:

pytest

Goal

DataFlow is a practical project for learning and demonstrating core data engineering concepts, including data ingestion, transformation, data quality, SQL, PostgreSQL, testing, and containerization.