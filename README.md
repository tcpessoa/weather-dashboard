# weather-dashboard
A real-time weather dashboard

# Overview diagram

![App Diagram](./docs/WeatherDashboard.excalidraw.png)

# Requirements
- Python
- Docker
- make

# Getting started
- Clone the repository
- `cd` to your cloned repo
-  In the main directory create a `.env` file based on `.env.example` with your weather api key and your database connection info. 
You can find you key [here](https://openweathermap.org/current).

You need a running instance of postgres in order to store the data.
Run `docker-compose up -d` to run a local postgres instance in the background.
- Run the script
```sh
make run
```
  
# Test
At the root folder, run this in the terminal:
```sh
make test
```
This will run all tests under the `tests/` folder.

# DB migrations

This project uses Alembic to handle migrations.
Check more info [here](./alembic/README.md)

# Dashboard UI
Built with React and Apache Echarts.

Currently using `echarts-for-react`, check examples [here](https://git.hust.cc/echarts-for-react/examples/simple)

```
npm install;
npm run start
```

# Backend

- `cd backend/`
- Then:

```sh
uvicorn backend.main:app --reload
```

# NOTES

The UI has a proxy to proxy `/weather` requests to the backend running on `http://localhost:8000`
