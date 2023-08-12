import logging
import os

import requests  # type: ignore
from dotenv import load_dotenv  # type: ignore
from pydantic import ValidationError  # type: ignore
from sqlalchemy import create_engine  # type: ignore
from sqlalchemy.orm import sessionmaker  # type: ignore

from app import models
from app.config import DATABASE_URL


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
        logging.error(f"Error fetching weather data: {req_err}")

    return None

def validate_weather_data(weather_data):
    try:
        validated_data = models.WeatherModel(**weather_data)
        return validated_data
    except ValidationError as e:
        print("Validation error:", e)
        return None

def transform_weather_data(weather_data: models.WeatherModel):
    """_summary_

    Args:
        weather_data (Json): stores the json from the get request

    Returns:
        exctract data from the json
    """
    location = weather_data.name
    longitude = weather_data.coord.lon
    latitude = weather_data.coord.lat
    temperature = weather_data.main.temp
    humidity = weather_data.main.humidity
    pressure = weather_data.main.pressure
    weather_description = weather_data.weather[0].description
    return (
        location,
        longitude,
        latitude,
        temperature,
        humidity,
        pressure,
        weather_description,
    )


def load_weather_data_to_db(
    location, longitude, latitude, temperature, humidity, pressure, weather_description
):
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
        weather_data_to_db = models.Weather(
            location=location,
            longitude=longitude,
            latitude=latitude,
            temperature=temperature,
            humidity=humidity,
            pressure=pressure,
            weather_description=weather_description,
        )
        db_session.add(weather_data_to_db)
        db_session.commit()
        db_session.refresh(weather_data_to_db)
        print("Weather data saved to database")

    except Exception as e:
        logging.error(f"Error loading weather data to database: {e}")


def run_etl():
    """_summary_"""
    location = {"lat": -1.292066, "lon": 36.821945, "appid": os.getenv("WEATHER_API")}
    weather_data = extract_weather_data(location)
    if weather_data:
        (
            location,
            longitude,
            latitude,
            temperature,
            humidity,
            pressure,
            weather_description,
        ) = transform_weather_data(weather_data)
        load_weather_data_to_db(
            location,
            longitude,
            latitude,
            temperature,
            humidity,
            pressure,
            weather_description,
        )
    else:
        logging.error("No weather data to load to database")

