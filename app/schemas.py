import datetime
from pydantic import BaseModel
from sqlalchemy import Float, Integer, String

class WeatherData(BaseModel):
    temperature :Float
    lat :Float
    lon :Float
    humidity : Float
    pressure : Float
    location :str
    weather_description :str
    
    
    class Config:
        arbitrary_types_allowed = True