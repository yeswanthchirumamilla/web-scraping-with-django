document.addEventListener('DOMContentLoaded', function () {
    document.getElementById('backButton').addEventListener('click', function () {
        window.history.back();
    });

    fetchPriceComparatorHistory();
});

async function fetchPriceComparatorHistory() {
    try {
        const response = await fetch('/price_comparator_history');

        if (!response.ok) {
            throw new Error('Network response was not ok');
        }

        const data = await response.json();
        console.log('Price comparator history data:', data);
        displayHistoryData(data);
    } catch (error) {
        console.error('Error fetching price comparator history:', error);
    }
}

function displayHistoryData(historyData) {
    const resultsContainer = document.getElementById('results');
    resultsContainer.innerHTML = ""; 
    historyData.forEach(entry => {
        const card = document.createElement('div');
        card.classList.add('history-card');

        const productName = document.createElement('h3');
        productName.textContent = entry.productname;

        const productPrice = document.createElement('p');
        productPrice.textContent = `Price: ₹${entry.price}`;

        const productLink = document.createElement('a');
        productLink.href = entry.productlink;
        productLink.textContent = 'View Product';
        productLink.target = '_blank';

        card.appendChild(productName);
        card.appendChild(productPrice);
        card.appendChild(productLink);

        resultsContainer.appendChild(card);
    });
}
