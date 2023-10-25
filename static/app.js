// Define the function to get a new quote
function getNewQuote() {
    // Make an AJAX request to your Flask route to get a new quote
    fetch("/get_quote")
        .then(response => response.json())
        .then(data => {
            // Update the quote text and author in the HTML
            document.getElementById("quote-text").textContent = data.quote;
            document.getElementById("author").textContent = "- " + data.author;
        })
        .catch(error => {
            console.error("Error fetching a new quote:", error);
        });
}

// Call the function to get the initial quote when the page loads
document.addEventListener("DOMContentLoaded", getNewQuote);

// Add a click event listener to the "Generate Quote" button
document.getElementById("generate-button").addEventListener("click", getNewQuote);
