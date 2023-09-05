const generateRandomYAxis = () => {
  const yAxis = [];
  for (let i = 0; i < 7; i++) {
    yAxis.push(Math.floor(Math.random() * 1000));
  }
  return yAxis;
}

export const data = {
  xAxis: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
  yAxis: generateRandomYAxis(),
}


// mock fetching data from API
export const fetchData = async () => {
  try {
    const response = await fetch('/weather');
    const data = await response.json();
    return data;
  } catch (error) {
    console.log(error);
  }
}
