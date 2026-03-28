from flask import Flask, render_template
import random

app = Flask(__name__)

quotes = [
    "Believe in yourself!",
    "Never give up.",
    "Success is not final, failure is not fatal.",
    "Dream big and dare to fail.",
    "Push yourself, because no one else will do it for you.",
    "Stay positive, work hard, make it happen."
]

@app.route("/")
def home():
    quote = random.choice(quotes)
    return render_template("index.html", quote=quote)

if __name__ == "__main__":
    app.run(debug=True)
