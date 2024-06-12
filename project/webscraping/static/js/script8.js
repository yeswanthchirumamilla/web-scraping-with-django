document.addEventListener('DOMContentLoaded', function () {
    fetchDoubtResolveHistory();
});

async function fetchDoubtResolveHistory() {
    try {
        const response = await fetch('/doubt_resolve_history');

        if (!response.ok) {
            throw new Error('Network response was not ok');
        }

        const data = await response.json();
        console.log('Doubt resolve history data:', data);
        displayDoubtResolveHistory(data);
    } catch (error) {
        console.error('Error fetching doubt resolve history:', error);
    }
}

function displayDoubtResolveHistory(historyData) {
    const resultsContainer = document.getElementById('results');
    resultsContainer.innerHTML = "";

    historyData.forEach(doubt => {
        const doubtCard = document.createElement('div');
        doubtCard.classList.add('doubt-card');

        const doubtTitle = document.createElement('h3');
        doubtTitle.textContent = doubt.doubt;
        doubtCard.appendChild(doubtTitle);

        doubt.answers.forEach(answer => {
            if (answer.answer !== null && answer.answer !== "" && answer.url !== null) {
                const answerCard = document.createElement('div');
                answerCard.classList.add('answer-card');

                const answerParagraph = document.createElement('p');
                answerParagraph.textContent = answer.answer;

                const answerLink = document.createElement('a');
                answerLink.href = answer.url;
                answerLink.textContent = 'For more info, click here';
                answerLink.target = '_blank';
                answerCard.appendChild(answerParagraph);
                answerCard.appendChild(answerLink);

                doubtCard.appendChild(answerCard);
            }
        });

        resultsContainer.appendChild(doubtCard);
    });
}

