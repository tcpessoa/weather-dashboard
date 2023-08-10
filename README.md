# weather-dashboard
A real-time weather dashboard

# Overview diagram

![App Diagram](./docs/WeatherDashboard.excalidraw.png)
# Getting started
- Clone the repository
- Create a Virtual Environment
```
Python -m venv env
```
- Activate the virtual environment
  ```
  env\Scripts\activate
  ```
- Install the requirements
  ```
  pip install -r requirements.txt
  ```
-  In the main directory create a **.env** file with your weather api key. You can find you key [here](https://openweathermap.org/current)
- create a **config file** . This contains the database URL.
```
DATABASE_URL = (('postgresql+psycopg2://user:password\
@hostname:port/database_name')
```
- Run the script
```
python main.py
```
  
