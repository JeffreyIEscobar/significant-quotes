import random
from flask import Flask, render_template, jsonify

# Load quotes with authors from a file
with open("quotes.txt", "r") as file:
    quotes = [line.strip() for line in file]

# Function to get a random quote and author
def get_random_quote_with_author():
    random_quote = random.choice(quotes)
    quote, author = random_quote.split(" - ", 1)
    return quote, author

# Flask web app to serve the HTML
app = Flask(__name__, template_folder="templates", static_folder="static")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get_quote")
def get_quote():
    quote, author = get_random_quote_with_author()
    return jsonify({"quote": quote, "author": author})

if __name__ == "__main__":
    app.debug = True  # Enable debug mode
    app.run()
