let myChart; // Declare myChart as a global variable

document.addEventListener('DOMContentLoaded', () => {
    const searchButton = document.querySelector('.searchButton');
    const searchInput = document.querySelector('.searchInput');
    const weatherInfo = document.getElementById('weatherInfo');
    
    searchButton.addEventListener('click', async () => {
        const cityName = searchInput.value.trim(); 

        if (cityName) {
            try {
                const weatherData = await fetchWeather(cityName);
                const todayTemp = weatherData.today_temp;
                if (weatherData && weatherData.weather_data) {
                    const weatherDataArray = weatherData.weather_data;
                    createChart(weatherDataArray);
                } else {
                    throw new Error('Weather data not found.');
                }
                if (todayTemp) {
                    const todayTempElement = document.createElement('p');
                    todayTempElement.textContent = `Current temperature is ${todayTemp}°C`;
                    if (weatherInfo.childNodes.length > 0) {
                        // If there's already a child node, replace it with the new temperature element
                        weatherInfo.replaceChild(todayTempElement, weatherInfo.childNodes[0]);
                    } else {
                        // Otherwise, just append the new temperature element
                        weatherInfo.appendChild(todayTempElement);
                    }
                }
            } catch (error) {
                console.error('Error fetching or processing weather data:', error);
                weatherInfo.innerText = 'An error occurred while fetching weather data.';
            }
        } else {
            weatherInfo.innerText = 'Please enter a city name.';
        }
    });

    searchInput.addEventListener('keydown', (event) => {
        if (event.key === "Enter") {
            searchButton.click();
        }
    });
});

async function fetchWeather(cityName) {
    try {
        console.log('Fetching weather data for', cityName);
        const response = await fetch(`/weather/${cityName}`);
        console.log('Response status:', response.status); 

        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }
        if (myChart) {
            myChart.destroy();
        }
        // Parse the response data as JSON
        const weatherData = await response.json();
        return weatherData;
    } catch (error) {
        console.error('Error fetching weather data:', error);
        return { error: 'An error occurred while fetching weather data.' };
    }
}

async function createChart(weatherData) {
    try {
        if (weatherData) {
            const dates = weatherData.map(data => data.date);
            const highTemperatures = weatherData.map(data => data.hightemperature);
            const lowTemperatures = weatherData.map(data => data.lowtemperature);
            const ctx = document.getElementById('weatherChart').getContext('2d');
            if (myChart) {
                myChart.destroy();
            }
            myChart = new Chart(ctx, {
                type: 'line',
                data: {
                    labels: dates,
                    datasets: [
                        {
                            label: 'High Temperature (°C)',
                            data: highTemperatures,
                            borderColor: 'rgba(255, 99, 132, 1)',
                            backgroundColor: 'rgba(255, 99, 132, 0.2)',
                            borderWidth: 1
                        },
                        {
                            label: 'Low Temperature (°C)',
                            data: lowTemperatures,
                            borderColor: 'rgba(54, 162, 235, 1)',
                            backgroundColor: 'rgba(54, 162, 235, 0.2)',
                            borderWidth: 1
                        }
                    ]
                },
                options: {
                    scales: {
                        y: {
                            beginAtZero: true
                        }
                    }
                }
            });
        } else {
            console.error('No weather data available.');
        }
    } catch (error) {
        console.error('Error creating chart:', error);
    }
}
