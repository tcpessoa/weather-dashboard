import './App.css';
import { fetchData } from './services/Api';
import { useEffect, useState } from "react"
import WeatherChart from './components/WeatherChart';

function App() {
  const [data, setData] = useState(undefined)
  useEffect(() => {
    fetchData()
      .then(data => {
        setData(data)
      })
  }, [])

  return (
    <div className="App">
      <h1>Dashboard UI</h1>
      { data && <WeatherChart data={data} /> }
    </div>
  );
}

export default App;
