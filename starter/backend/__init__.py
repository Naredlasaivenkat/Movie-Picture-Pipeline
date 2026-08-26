import os

from flask import Flask, jsonify
from flask_cors import CORS

from .movies import movies_api

app = Flask(__name__)
CORS(app)

app.register_blueprint(movies_api)


@app.route("/")
def health():
    return jsonify({"status": "Backend is running"})


if __name__ == "__main__":
    app.run(
        debug=False,
        host="0.0.0.0",
        port=int(os.getenv("FLASK_RUN_PORT", 5000)),
    )
