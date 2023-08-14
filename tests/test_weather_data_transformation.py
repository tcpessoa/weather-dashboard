from pydantic import ValidationError # type: ignore
from app.etl import \
    transform_weather_data  # Replace 'your_module' with the actual module name
from app.models import WeatherModel, WeatherCreate
import pytest # type: ignore


def test_valid_data():
    weather_data = {
        "name": "New York",
        "coord": {"lon": -74.006, "lat": 40.7128},
        "main": {"temp": 25.6, "humidity": 60, "pressure": 1013.2},
        "weather": [{"description": "Clear sky"}],
    }
    weather_data = WeatherModel(**weather_data)
    expected_result = WeatherCreate(
        location="New York",
        longitude=-74.006,
        latitude=40.7128,
        temperature=25.6,
        humidity=60,
        pressure=1013.2,
        weather_description="Clear sky",
    )
    assert transform_weather_data(weather_data) == expected_result


def test_missing_key():
    weather_data = {
        "name": "London",
        "coord": {"lat": 51.5074},
        "main": {"temp": 20.3, "humidity": 75}
        # "weather" key is missing here
    }
    # test that a ValidationError is raised
    with pytest.raises(ValidationError):
        weather_data = WeatherModel(**weather_data)


