import requests
import os
import logging
from sqlalchemy import create_engine
from dotenv import load_dotenv
from sqlalchemy.orm import sessionmaker
from app.config import DATABASE_URL
from . import models


load_dotenv()

Location = {
    'lat': -1.292066,
    'lon': 36.821945,
    'appid': os.getenv("WEATHER_API")
    }

engine = create_engine(DATABASE_URL)
Session = sessionmaker(autocommit=False, autoflush=False,bind=engine)

def extract_weather_data(Location):
    try:
        url= "https://api.openweathermap.org/data/2.5/weather?"
        response = requests.get(url,params=Location)
        weather_data = response.json() 
        return weather_data
    except Exception as e:
        logging.error(f"fetching weather data failed {e}")
        return None 
    

def transform_weather_data(weather_data):
    try:
        location=weather_data["name"],
        longitude=weather_data["coord"]["lon"],
        latitude=weather_data["coord"]["lat"],
        temperature=weather_data["main"]["temp"],
        humidity=weather_data["main"]["humidity"],
        pressure=weather_data["main"]["pressure"],
        weather_description=weather_data["weather"][0]["description"]
        return location, longitude, latitude, temperature, humidity, pressure, weather_description
    except Exception as e:
        logging.error("transforming weather data failed")
    

def load_weather_data_to_db(location,longitude,latitude,temperature, humidity, pressure, weather_description):
    try:
        db_session=Session()
        weather_data_to_db = models.Weather(location=location,longitude=longitude,latitude=latitude,temperature=temperature, humidity=humidity,pressure=pressure, weather_description=weather_description)
        db_session.add(weather_data_to_db)
        db_session.commit()
        db_session.refresh(weather_data_to_db)
        print("Weather data saved to database")
       
    except Exception as e:  
        logging.error(f"Error loading weather data to database: {e}")

def run_etl():
    weather_data = extract_weather_data( Location)
    if weather_data:
        location,longitude,latitude,temperature, humidity,pressure, weather_description = transform_weather_data(weather_data)
        load_weather_data_to_db(location,longitude,latitude,temperature, humidity,pressure, weather_description)
    else:
        logging.error("No weather data to load to database")
