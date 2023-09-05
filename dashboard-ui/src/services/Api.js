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
export const fetchData = async () => {
  try {
    const response = await fetch("/weather");
    if (!response.ok) {
      console.error(`HTTP error! status: ${response.status}`)
      console.error(response.statusText)
      throw new Error("Network response was not ok");
    }
    const jsonData = await response.json();
    return jsonData;
  } catch (error) {
    console.error("Error fetching data:", error);
  }
}
