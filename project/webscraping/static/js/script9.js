document.addEventListener('DOMContentLoaded', function () {
    document.getElementById('backButton').addEventListener('click', function () {
        window.history.back();
    });

    fetchWeatherSearchHistory();
});

async function fetchWeatherSearchHistory() {
    try {
        const response = await fetch('/weather_search_history');

        if (!response.ok) {
            throw new Error('Network response was not ok');
        }

        const data = await response.json();
        console.log('Weather search history data:', data);
        displayWeatherSearchHistory(data);
    } catch (error) {
        console.error('Error fetching weather search history:', error);
    }
}

function displayWeatherSearchHistory(weatherData) {
    const tableHead = document.getElementById('table-head');
    const tableBody = document.getElementById('table-body');
    tableHead.innerHTML = "";
    tableBody.innerHTML = "";

    // Create table headers based on the first entry's keys
    const headers = Object.keys(weatherData[0]);
    const headerRow = document.createElement('tr');
    headers.forEach(header => {
        const th = document.createElement('th');
        th.textContent = header.charAt(0).toUpperCase() + header.slice(1); // Capitalize the first letter
        headerRow.appendChild(th);
    });
    tableHead.appendChild(headerRow);

    // Populate table body with data
    weatherData.forEach(entry => {
        const row = document.createElement('tr');
        headers.forEach(header => {
            const td = document.createElement('td');
            td.textContent = entry[header];
            row.appendChild(td);
        });
        tableBody.appendChild(row);
    });
}
