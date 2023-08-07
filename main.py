import requests
from dotenv import load_dotenv
import os
from config import DATABASE_URL
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
from app import models, schemas, database
from config import DATABASE_URL
import schedule
import time

load_dotenv()
weather_api = os.getenv("WEATHER_API")
weather_endpoint = "https://api.openweathermap.org/data/2.5/weather?"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
db = SessionLocal()  # creates a session

def fetch_and_save_weather_data():
    parameters = {
        "lat": -1.292066,
        "lon": 36.821945,
        "appid": os.getenv("WEATHER_API")
        }

    response = requests.get(url=weather_endpoint, params=parameters)
    weather_data = response.json()

    weather_data_to_db = database.save_weather_data(db, weather_data)
    print("data saved to db")



schedule.every(20).seconds.do(fetch_and_save_weather_data)

# Run the scheduled task in a loop
while True:
    schedule.run_pending()
    time.sleep(1)
