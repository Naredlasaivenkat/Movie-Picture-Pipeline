from flask import jsonify, request
from flask.views import MethodView


movies = {
    "123": {
        "title": "Top Gun: Maverick",
        "description": "Fighter planes",
    },
    "456": {
        "title": "Sonic the Hedgehog",
        "description": "Blue Sega character",
    },
    "789": {
        "title": "A Quiet Place",
        "description": "Scary monsters",
    },
}


class Movies(MethodView):

    def get(self, movie_id=None):
        if movie_id is None:
            return jsonify({
                "movies": [
                    {
                        "id": movie_id,
                        "title": movie["title"],
                        "description": movie["description"],
                    }
                    for movie_id, movie in movies.items()
                ]
            }), 200

        movie = movies.get(str(movie_id))

        if movie is None:
            return jsonify({
                "error": "Movie not found"
            }), 404

        return jsonify({
            "movie": {
                "id": str(movie_id),
                **movie,
            }
        }), 200

    def post(self):
        data = request.get_json()

        if not data:
            return jsonify({
                "error": "Request body is required"
            }), 400

        movie_id = str(data.get("id"))

        if not movie_id or movie_id == "None":
            return jsonify({
                "error": "Movie id is required"
            }), 400

        movies[movie_id] = {
            "title": data.get("title", ""),
            "description": data.get("description", ""),
        }

        return jsonify({
            "message": "Movie created",
            "movie": {
                "id": movie_id,
                **movies[movie_id],
            }
        }), 201

    def put(self, movie_id):
        movie = movies.get(str(movie_id))

        if movie is None:
            return jsonify({
                "error": "Movie not found"
            }), 404

        data = request.get_json()

        if not data:
            return jsonify({
                "error": "Request body is required"
            }), 400

        movie["title"] = data.get("title", movie["title"])
        movie["description"] = data.get(
            "description",
            movie["description"],
        )

        return jsonify({
            "movie": {
                "id": str(movie_id),
                **movie,
            }
        }), 200

    def delete(self, movie_id):
        movie_id = str(movie_id)

        if movie_id not in movies:
            return jsonify({
                "error": "Movie not found"
            }), 404

        deleted = movies.pop(movie_id)

        return jsonify({
            "message": "Movie deleted",
            "movie": {
                "id": movie_id,
                **deleted,
            }
        }), 200
    