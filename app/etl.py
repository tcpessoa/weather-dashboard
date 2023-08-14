import os

import requests  # type: ignore
from dotenv import load_dotenv
from pydantic import ValidationError
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app import models
from app.config import DATABASE_URL
from app.logger import logger

load_dotenv()


engine = create_engine(DATABASE_URL)
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def extract_weather_data(location):
    """_summary_

    Args:
        Location (_type_): dict with the lat,lon and appid to a location

    Returns:
        Json data
    """
    try:
        url = "https://api.openweathermap.org/data/2.5/weather?"
        response = requests.get(url, params=location)
        response.raise_for_status()  # Raise HTTPError for non-2xx responses

        weather_data = response.json()
        weather_data_validated = validate_weather_data(weather_data)
        return weather_data_validated
    except requests.exceptions.RequestException as req_err:
        logger.error(f"Error fetching weather data: {req_err}")
        raise req_err


def validate_weather_data(weather_data):
    try:
        validated_data = models.WeatherModel(**weather_data)
        return validated_data
    except ValidationError as e:
        print("Validation error:", e)
        raise e


def transform_weather_data(weather_data: models.WeatherModel) -> models.WeatherCreate:
    """_summary_

    Args:
        weather_data (Json): stores the json from the get request

    Returns:
        exctract data from the json
    """
    weather_create = models.WeatherCreate(
        location=weather_data.name,
        longitude=weather_data.coord.lon,
        latitude=weather_data.coord.lat,
        temperature=weather_data.main.temp,
        humidity=weather_data.main.humidity,
        pressure=weather_data.main.pressure,
        weather_description=weather_data.weather[0].description,
    )
    logger.info(
        f"Location: {weather_create.location} Temperature: {weather_create.temperature} \
Weather Description: {weather_create.weather_description}"
    )
    return weather_create


def load_weather_data_to_db(weather_create: models.WeatherCreate):
    """_summary_

    Args:
        location (string): name of the location
        longitude (float): longitude of the location
        latitude (float): latitude of the location
        temperature (float): temperature value at current state
        humidity (float): current humidity value
        pressure (float): current pressure value
        weather_description (string): description of the current weather condition
    """
    try:
        db_session = Session()
        weather_data_to_db = models.Weather(**weather_create.model_dump())
        db_session.add(weather_data_to_db)
        db_session.commit()
        db_session.refresh(weather_data_to_db)
        print("Weather data saved to database")

    except Exception as e:
        logger.error(f"Error loading weather data to database: {e}")


def run_etl():
    """_summary_"""
    location = {"lat": -1.292066, "lon": 36.821945, "appid": os.getenv("WEATHER_API")}
    weather_data = extract_weather_data(location)
    weather_create = transform_weather_data(weather_data)
    load_weather_data_to_db(weather_create)


if __name__ == "__main__":
    """
    Run this file to extract and transform weather data
    without loading it to the database
    """
    location = {"lat": -1.292066, "lon": 36.821945, "appid": os.getenv("WEATHER_API")}
    weather_data = extract_weather_data(location)
    weather_data_create = transform_weather_data(weather_data)
    logger.info(f"weather_data_create: {weather_data_create}")
