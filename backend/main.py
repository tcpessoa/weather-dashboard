import math
from fastapi import FastAPI, Query
from databases import Database
from pydantic import BaseModel
from sqlalchemy import TIMESTAMP, Column, Float, Integer, String
from sqlalchemy.orm import declarative_base
from sqlalchemy.sql import func
from app.config import DATABASE_URL
import datetime

Base = declarative_base()

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

# Configure your database connection
database = Database(DATABASE_URL)
metadata = Base.metadata # type: ignore

# Create the FastAPI app
app = FastAPI()

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

class WeatherResponse(BaseModel):
    id: int
    temperature: float
    latitude: float
    longitude: float
    humidity: float
    pressure: float
    location: str
    weather_description: str
    timestamp: datetime.datetime

# Define the endpoint to fetch the latest weather data for all locations
@app.get("/weather")
async def get_paginated_latest_weather_data(
    page: int = Query(1, description="Page number"),
    pagesize: int = Query(10, description="Items per page")
):
    query = f"""
    SELECT 
    --DISTINCT ON (location) 
    *
    FROM weather_table
    ORDER BY location, timestamp DESC
    OFFSET {(page - 1) * pagesize} LIMIT {pagesize}
    """
    results = await database.fetch_all(query)
    
    total_query = "SELECT COUNT(*) FROM weather_table"
    total = await database.fetch_val(total_query)
    total_pages = math.ceil(total / pagesize)

    return {
        "total_pages": total_pages,
        "current_page": page,
        "per_page": pagesize,
        "total_items": total,
        "items": [WeatherResponse(**result) for result in results] # type: ignore
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
