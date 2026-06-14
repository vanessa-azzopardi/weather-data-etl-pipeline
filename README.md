# Weather Data ETL Pipeline

![Weather Data ETL Pipeline Banner](images/weather-etl-banner.png)

## Overview

This project demonstrates the implementation of a simple end-to-end ETL pipeline using Python.

Weather data is extracted from the OpenWeatherMap API, transformed into a structured tabular dataset using Pandas, loaded into a SQLite database using SQLAlchemy, queried using SQL, and visualised using Matplotlib.

The project was developed as a portfolio example to demonstrate practical skills in API integration, data transformation, database loading, and analytical output generation.

## Technologies Used

- Python
- OpenWeatherMap API
- Pandas
- Requests
- SQLAlchemy
- SQLite
- Matplotlib
- python-dotenv

## Project Architecture

![Weather ETL Architecture](images/weather-etl-architecture.png)

## ETL Process

### 1. Extract

The pipeline sends requests to the OpenWeatherMap API for a predefined list of cities and retrieves current weather data in JSON format.

### 2. Transform

The raw JSON responses are transformed into a structured dataset containing selected fields such as:

- Country
- City
- Temperature
- Humidity
- Weather description
- Wind speed

### 3. Load

The transformed dataset is loaded into a SQLite database table for storage and querying.

### 4. Visualise

A simple bar chart is generated to compare temperatures across the selected cities.

## Sample Output

The transformed output contains one record per city.

| country | city | temperature | humidity | weather | wind_speed |
|---|---|---:|---:|---|---:|
| MT | Valletta | 28.06 | 64 | clear sky | 3.95 |
| MT | Saint Venera | 27.92 | 64 | clear sky | 4.00 |
| GB | London | 21.11 | 49 | overcast clouds | 2.24 |
| FR | Paris | 25.75 | 35 | broken clouds | 1.79 |
| US | New York | 29.99 | 45 | overcast clouds | 4.92 |

## Visualisation

![Temperature Comparison Chart](images/temperature-comparison-chart.png)

## Repository Structure

```text
etl-pipeline/
│
├── README.md
├── requirements.txt
├── .gitignore
├── .env.example
│
├── src/
│   └── weather_pipeline.py
│
├── data/
│   └── sample_output.csv
│
└── images/
    ├── weather-etl-banner.png
    ├── weather-etl-architecture.png
    └── temperature-comparison-chart.png
