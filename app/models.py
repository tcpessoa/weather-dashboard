from sqlalchemy import TIMESTAMP, Column, Float, Integer, String # type: ignore
from sqlalchemy.orm import DeclarativeBase # type: ignore
from sqlalchemy.sql import func # type: ignore

# Check https://docs.sqlalchemy.org/en/20/changelog/whatsnew_20.html#migrating-an-existing-mapping
# for declarative base

class Base(DeclarativeBase):
    pass

class Weather(Base):
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
    
