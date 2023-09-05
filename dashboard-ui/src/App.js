import './App.css';
import BarChart from './components/BarChart';
import LineChart from './components/LineChart';
import WeatherChart from './components/WeatherChart';
import SampleHello from './components/SampleHello';
import { fetchData } from './services/Api';
import { useEffect, useState } from "react"
import SampleTempChart from './components/SampleTempChart';

function App() {
  const [users, setUsers] = useState([])
  const [loadingUsers, setLoadingUsers] = useState(false)
  const [loadingWeather, setLoadingWeather] = useState(false)
  const [weatherData, setWeatherData] = useState([])
  useEffect(() => {
    setLoadingUsers(true)
    setLoadingWeather(true)
    fetch("https://jsonplaceholder.typicode.com/users")
      .then(response => response.json())
      .then(json => setUsers(json))
      .finally(() => {
        setLoadingUsers(false)
      })
    fetchData()
      .then(data => {
        setWeatherData(data)
      })
      .finally(() => {
        setLoadingWeather(false)
      })
  }, [])

  const data = {
    xAxis: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
    yAxis: [820, 932, 901, 934, 1290, 1330, 1320],
  }

  return (
    <div className="App">
      {loadingUsers ? (
        <div>Loading...</div>
      ) : (
        <>
          <h1>Users</h1>
          <table border={1}>
            <tr>
              <th>Name</th>
              <th>Email</th>
              <th>Phone</th>
            </tr>
            {users.map(user => (
              <tr key={user.id}>
                <td>{user.name}</td>
                <td>{user.email}</td>
                <td>{user.phone}</td>
              </tr>
            ))}
          </table>
        </>
      )}
      <SampleHello data={{ name: 'Tum' }} />
      <div>
        {loadingWeather ? (
          <h2 style={{ color: 'black' }}>Loading...</h2>
        ) : (
          <WeatherChart data={weatherData} />
        )}

      </div>
      <BarChart data={data} />
      <SampleTempChart />
    </div>
  );
}

export default App;
