from sqlalchemy import TIMESTAMP, Column, Float, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func
from pydantic import BaseModel

# Check https://docs.sqlalchemy.org/en/20/changelog/whatsnew_20.html#migrating-an-existing-mapping
# for declarative base

Base = declarative_base()

class Weather(Base): # type: ignore
    __tablename__ = "weather_table" 
    
    id = Column(Integer, primary_key=True, index=True)
    temperature = Column(Float)
    latitude = Column(Float)
    longitude = Column(Float)
    humidity = Column(Float)
    pressure = Column(Float)
    location = Column(String(256))
    weather_description = Column(String(256))
    timestamp = Column(TIMESTAMP, server_default=func.now())

class WeatherCreate(BaseModel):
    temperature: float
    latitude: float
    longitude: float
    humidity: float
    pressure: float
    location: str
    weather_description: str

class CoordinatesModel(BaseModel):
    lon: float
    lat: float

class MainDataModel(BaseModel):
    temp: float
    humidity: int
    pressure: float

class WeatherDescriptionModel(BaseModel):
    description: str

class WeatherModel(BaseModel):
    name: str
    coord: CoordinatesModel
    main: MainDataModel
    weather: list[WeatherDescriptionModel]   
