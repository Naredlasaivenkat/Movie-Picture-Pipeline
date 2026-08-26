from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

MOVIES = [
    {
        "id": "123",
        "title": "Top Gun: Maverick",
        "description": "Fighter planes",
    },
    {
        "id": "456",
        "title": "Sonic the Hedgehog",
        "description": "Blue Sega character",
    },
    {
        "id": "789",
        "title": "A Quiet Place",
        "description": "Scary monsters",
    },
]


@app.route("/")
def home():
    return jsonify({"status": "Backend is running"})


@app.route("/health")
def health():
    return jsonify({"status": "ok"})


@app.route("/movies")
def get_movies():
    return jsonify({"movies": MOVIES})


if __name__ == "__main__":
    app.run(
        debug=False,
        host="0.0.0.0",
        port=5000,
    )