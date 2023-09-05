import React from "react";
import ReactECharts from "echarts-for-react";

function WeatherChart({ data }) {
  console.log(data);
  return (
    <div>
      <h1>Weather Chart</h1>
    </div>
  )
  const option = {
    title: {
      text: "Weather Data",
    },
    tooltip: {
      trigger: "axis",
    },
    legend: {
      data: ["Temperature", "Humidity", "Pressure"],
    },
    xAxis: {
      type: "category",
      data: data.items.map((item) => item.timestamp),
    },
    yAxis: [
      {
        type: "value",
        name: "Temperature (K)",
        min: Math.min(...data.items.map((item) => item.temperature)) - 10,
        max: Math.max(...data.items.map((item) => item.temperature)) + 10,
      },
      {
        type: "value",
        name: "Humidity (%)",
        min: 0,
        max: 100,
      },
      {
        type: "value",
        name: "Pressure (hPa)",
        min: Math.min(...data.items.map((item) => item.pressure)) - 10,
        max: Math.max(...data.items.map((item) => item.pressure)) + 10,
      },
    ],
    series: [
      {
        name: "Temperature",
        type: "line",
        data: data.items.map((item) => item.temperature),
        yAxisIndex: 0,
      },
      {
        name: "Humidity",
        type: "line",
        data: data.items.map((item) => item.humidity),
        yAxisIndex: 1,
      },
      {
        name: "Pressure",
        type: "line",
        data: data.items.map((item) => item.pressure),
        yAxisIndex: 2,
      },
    ],
  };

  return <ReactECharts option={option} style={{ height: "400px" }} />;
}

export default WeatherChart;
