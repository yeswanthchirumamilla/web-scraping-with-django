document.addEventListener('DOMContentLoaded', function () {
    document.getElementById('backButton').addEventListener('click', function () {
        window.history.back();
    });

    fetchMovieHistory();
});

async function fetchMovieHistory() {
    try {
        const response = await fetch('/movie_history');

        if (!response.ok) {
            throw new Error('Network response was not ok');
        }

        const data = await response.json();
        console.log('Movie history data:', data);
        displayMovieHistory(data);
    } catch (error) {
        console.error('Error fetching movie history:', error);
    }
}

function displayMovieHistory(movieData) {
    const resultsContainer = document.getElementById('results');
    resultsContainer.innerHTML = ""; 

    movieData.forEach(movie => {
        const movieCard = document.createElement('div');
        movieCard.classList.add('movie-card');

        const movieTitle = document.createElement('h3');
        movieTitle.textContent = movie.title;
        movieCard.appendChild(movieTitle);

        const movieRating = document.createElement('p');
        movieRating.textContent = `Rating: ${movie.rating}/10`;
        movieCard.appendChild(movieRating);

        const movieSummary = document.createElement('p');
        movieSummary.textContent = movie.summary;
        movieCard.appendChild(movieSummary);

        resultsContainer.appendChild(movieCard);
    });
}
