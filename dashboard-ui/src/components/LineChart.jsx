import React from 'react';
import ReactECharts from 'echarts-for-react';

const LineChart = ({ data }) => {
  console.log(data);
  const options = {
    grid: { top: 8, right: 8, bottom: 24, left: 36 },
    xAxis: {
      type: 'category',
      data: data.xAxis,
    },
    yAxis: {
      type: 'value',
    },
    series: [
      {
        data: data.yAxis,
        type: 'line',
        smooth: true,
      },
    ],
    tooltip: {
      trigger: 'axis',
    },
  };

  return <ReactECharts option={options} />;
};

export default LineChart;
