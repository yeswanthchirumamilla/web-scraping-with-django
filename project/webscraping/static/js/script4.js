document.addEventListener('DOMContentLoaded', () => {
    const flipCardInner = document.querySelector('.flip-card-inner');
    const changeButton = document.getElementById('changeButton');
  
    let isFlipped = false;
  
    changeButtonmovie.addEventListener('click', () => {
        const actorInfo = document.getElementById('actorInfo');
        actorInfo.innerHTML = '';
        const movieInfo = document.getElementById('movieInfo');
       movieInfo.innerHTML = '';
      flipCardInner.classList.toggle('flipped');
      isFlipped = !isFlipped;
    });
    changeButtonhero.addEventListener('click', () => {
    const actorInfo = document.getElementById('actorInfo');
     actorInfo.innerHTML = '';
     const movieInfo = document.getElementById('movieInfo');
    movieInfo.innerHTML = '';
      flipCardInner.classList.toggle('flipped');
      isFlipped = !isFlipped;
    });
    const searchButtonMovie = document.getElementById('searchButtonMovie');
    const searchButtonHero = document.getElementById('searchButtonHero');
  
    searchButtonMovie.addEventListener('click', () => {
      const searchTerm = document.getElementById('searchInputMovie').value.trim();
      if (searchTerm) {
        console.log(`Searching for movies with query "${searchTerm}"`);
        searchMovies(searchTerm);
      }
    });
  
    searchButtonHero.addEventListener('click', () => {
      const searchTerm = document.getElementById('searchInputActor').value.trim();
      if (searchTerm) {
        console.log(`Searching for heroes with query "${searchTerm}"`);
        searchHeroes(searchTerm);
      }
    });
});

async function searchMovies(searchTerm) {
    try {
        const response = await fetch(`/movies/${searchTerm}`);

        if (!response.ok) {
            throw new Error('Network response was not ok');
        }

        const data = await response.json();
        console.log('Response from Django:', data);
        displayMovieData(data)
    } catch (error) {
        console.error('Error:', error);
    }
}

async function searchHeroes(searchTerm) {
    try {
        const response = await fetch(`actors/${searchTerm}/`);

        if (!response.ok) {
            throw new Error('Network response was not ok');
        }

        const data = await response.json();
        console.log('Response from Django:', data);
        displayActorData(data)
    } catch (error) {
        console.error('Error:', error);
    }
}

function displayMovieData(movieData) {
    const movieInfo = document.getElementById('movieInfo');
    movieInfo.innerHTML = '';
    // const moviedta=movieData.querySelector
    const Movie_Name = movieData.answers.Movie_Name;
    const Rating = movieData.answers.Rating;
    const Summary = movieData.answers.Summary;
    const movieNameElement = document.createElement('h3');
            movieNameElement.textContent = ` ${Movie_Name}`;
            const ratingElement = document.createElement('p');
            ratingElement.textContent = `Rating: ${Rating}`;
            const summaryElement = document.createElement('p');
            summaryElement.textContent = `Summary: ${Summary}`;

            // Append elements to weatherInfo
            movieInfo.appendChild(movieNameElement);
            movieInfo.appendChild(ratingElement);
            movieInfo.appendChild(summaryElement);
}

function displayActorData(actorData) {
    // Get the actorInfo div
    const actorInfo = document.getElementById('actorInfo');
    
    // Clear previous actor data
    actorInfo.innerHTML = '';

    // Iterate through the array of actors
    actorData.answers.forEach(actorName => {
        // Create a paragraph element for each actor
        const actorElement = document.createElement('p');
        actorElement.style.backgroundColor = "white";
        actorElement.textContent = actorName;

        // Append the actor element to the actorInfo div
        actorInfo.appendChild(actorElement);
    });
}
