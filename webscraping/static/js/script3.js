document.getElementById("search").addEventListener("keydown", function(event) {
    if (event.key === "Enter") {
        searchDoubt(this.value);
    }
});

async function searchDoubt(searchTerm) {
    try {
        const response = await fetch(`doubts/${searchTerm}/`);

        if (!response.ok) {
            throw new Error('Network response was not ok');
        }

        const data = await response.json();
        console.log('Response from Django:', data);
        displayDoubt(data);
    } catch (error) {
        console.error('Error:', error);
    }
}

function displayDoubt(data) {
    const resultsContainer = document.getElementById("results");
    resultsContainer.innerHTML = "";
    const urls=data.answers.urls;
    const paragraphs=data.answers.summaries;

    for (let i = 0; i < 3; i++) {
        if (paragraphs[i] !== null && paragraphs[i]!="" && urls[i]!=null){
        const card = document.createElement("div");
        card.classList.add("card");
        const paragraph = document.createElement("p");
        paragraph.textContent = paragraphs[i];
        const link = document.createElement("a");
        link.href = urls[i];
        link.textContent = "For more info, click here";
        link.target = "_blank"; 
        card.appendChild(paragraph);
        card.appendChild(link);
        resultsContainer.appendChild(card);
        }
    }
    
    }
