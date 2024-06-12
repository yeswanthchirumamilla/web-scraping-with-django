document.addEventListener('DOMContentLoaded', function () {
    const searchButton = document.getElementById('searchButton');
    const inputField = document.getElementById('search');

    searchButton.addEventListener('click', handleSearch);
    inputField.addEventListener('keydown', function(event) {
        if (event.key === "Enter") {
            handleSearch();
        }
    });

    async function handleSearch() {
        const productName = inputField.value.trim();
        if (productName !== '') {
            await fetchProductPrices(productName);
        } else {
            alert('Please enter a product name');
        }
    }

    async function fetchProductPrices(productName) {
        try {
            const response = await fetch(`products/${productName}`);
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }

            const data = await response.json();
            console.log('Response from the server:', data);
            displayProductData(data);
        } catch (error) {
            console.error('Error:', error);
        }
    }

    function displayProductData(data) {
        const resultsContainer = document.getElementById('results');
        if (!resultsContainer) {
            console.error('Results container not found');
            return;
        }
        resultsContainer.innerHTML = "";
    
        const card = document.createElement('div');
        card.classList.add('product-card');
    
        const productName = document.createElement('h3');
        productName.textContent = (data.answers).name; // Accessing the 'name' property
    
        const productPrice = document.createElement('p');
        productPrice.textContent = `Price: ₹${(data.answers).price}`; // Accessing the 'price' property
    
        const buyLink = document.createElement('a');
        buyLink.href = (data.answers).url; // Accessing the 'url' property
        buyLink.textContent = 'Buy Now';
        buyLink.target = '_blank';
    
        card.appendChild(productName);
        card.appendChild(productPrice);
        card.appendChild(buyLink);
    
        resultsContainer.appendChild(card);
    }
    
});