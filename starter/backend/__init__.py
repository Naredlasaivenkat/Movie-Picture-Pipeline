import os

from flask import Flask, jsonify
from flask_cors import CORS

from .movies import movies_api

app = Flask(__name__)
CORS(app)

app.register_blueprint(movies_api)


@app.errorhandler(Exception)
def handle_error(error):
    print("BACKEND ERROR:", repr(error), flush=True)

    return jsonify({
        "error": str(error),
        "type": type(error).__name__,
    }), 500


@app.route("/health")
def health():
    return jsonify({"status": "ok"}), 200


if __name__ == "__main__":
    app.run(
        debug=False,
        host="0.0.0.0",
        port=int(os.getenv("FLASK_RUN_PORT", 5000)),
    )
    