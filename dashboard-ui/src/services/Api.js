const generateRandomYAxis = () => {
  const yAxis = [];
  for (let i = 0; i < 7; i++) {
    yAxis.push(Math.floor(Math.random() * 1000));
  }
  return yAxis;
}

const data = {
  xAxis: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
  yAxis: generateRandomYAxis(),
}


// mock fetching data from API
export const fetchData = () => {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      resolve(data);
    }, 5000);
  });
}

