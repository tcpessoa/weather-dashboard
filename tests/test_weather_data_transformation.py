from app.etl import \
    transform_weather_data  # Replace 'your_module' with the actual module name


def test_valid_data():
    weather_data = {
        "name": "New York",
        "coord": {"lon": -74.006, "lat": 40.7128},
        "main": {"temp": 25.6, "humidity": 60, "pressure": 1013.2},
        "weather": [{"description": "Clear sky"}],
    }
    expected_result = (
        ("New York",),
        (-74.006,),
        (40.7128,),
        (25.6,),
        (60,),
        (1013.2,),
        "Clear sky",
    )
    assert transform_weather_data(weather_data) == expected_result


def test_missing_key():
    weather_data = {
        "name": "London",
        "coord": {"lat": 51.5074},
        "main": {"temp": 20.3, "humidity": 75}
        # "weather" key is missing here
    }
    assert transform_weather_data(weather_data) is None

