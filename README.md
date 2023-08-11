# weather-dashboard
A real-time weather dashboard

# Overview diagram

![App Diagram](./docs/WeatherDashboard.excalidraw.png)

# Requirements
- Python
- Docker

# Getting started
- Clone the repository
- Create a Virtual Environment

```sh
python -m venv env
```

- Activate the virtual environment
```sh
env\Scripts\activate
```

- Install the requirements
```sh
pip install -r requirements.txt
```

-  In the main directory create a **.env** file based on `.env.example` with your weather api key and your database connection info. 
You can find you key [here](https://openweathermap.org/current).

You need a running instance of postgres in order to store the data.
Run `docker-compose up -d` to run a local postgres instance in the background.

- Run the script
```sh
python main.py
```
  
# Test
At the root folder, run this in the terminal:
```sh
pytest
```
This will run all tests under the `tests/` folder.

# TODO
- Validate the JSON response of openweathermap so that I have a types object after the request
- Fix the pytest error

