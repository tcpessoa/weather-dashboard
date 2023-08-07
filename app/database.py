from sqlalchemy.orm import Session
from . import models, schemas

def save_weather_data(db: Session, weather_data: schemas.WeatherData):
    """_summary_

    Args:
        db (Session): _description_
        weather_data (schemas.WeatherData): _description_

    Returns:
        _type_: _description_
    """
    
    weather_to_db = models.Weather(
        location=weather_data["name"],
        lon=weather_data["coord"]["lon"],
        lat=weather_data["coord"]["lat"],
        temperature=weather_data["main"]["temp"],
        humidity=weather_data["main"]["humidity"],
        pressure=weather_data["main"]["pressure"],
        weather_description=weather_data["weather"][0]["description"],
        
        
    )
    
    db.add(weather_to_db)
    db.commit()
    db.refresh(weather_to_db)
    return weather_to_db
    