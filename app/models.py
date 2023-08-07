from sqlalchemy import Column,Float,Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class Weather(Base):
    __tablename__ = "weather_table"

    id = Column(Integer, primary_key=True, index=True)
    temperature = Column(Float)
    lat = Column(Float)
    lon = Column(Float)
    humidity = Column(Float)
    pressure = Column(Float)
    location = Column(String(256))
    weather_description = Column(String(256))
    