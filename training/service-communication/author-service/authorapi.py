from flask import Flask, jsonify
from flask_restful import Api, Resource
import requests

app = Flask(__name__)
api = Api(app)

# Sample data for authors (author_id, name, genre)
authors = [
    {"author_id": 1, "name": "J.D. Salinger", "genre": "Fiction"},
    {"author_id": 2, "name": "George Orwell", "genre": "Dystopian"},
    {"author_id": 3, "name": "Harper Lee", "genre": "Fiction"},
    {"author_id": 4, "name": "Aldous Huxley", "genre": "Dystopian"},
    {"author_id": 5, "name": "F. Scott Fitzgerald", "genre": "Fiction"},
]

# Base URL of the BookService
BOOK_SERVICE_URL = "http://localhost:5000"

# API to retrieve all authors
class AuthorListResource(Resource):
    def get(self):
        """Returns all authors with id, name, and genre"""
        return jsonify({"authors": authors})

# API to retrieve books for the given genre
class GenreBooksResource(Resource):
    def get(self, genre):
        """Returns books for a specific genre by finding authors and then querying BookService"""
        # Find authors for the given genre
        authors_in_genre = [author for author in authors if author['genre'].lower() == genre.lower()]
        
        if not authors_in_genre:
            return jsonify({"message": "No authors found for this genre"}), 404
        
        books_by_authors = []
        
        # For each author in the genre, request their books from BookService
        for author in authors_in_genre:
            response = requests.get(f"{BOOK_SERVICE_URL}/books/author/{author['name']}")
            if response.status_code == 200:
                books_by_authors.extend(response.json().get("books", []))
        
        if books_by_authors:
            return jsonify({"books": books_by_authors})
        else:
            return jsonify({"message": "No books found for this genre"}), 404

# Add resources to the API
api.add_resource(AuthorListResource, '/authors')
api.add_resource(GenreBooksResource, '/books/genre/<string:genre>')

if __name__ == '__main__':
    app.run(debug=True, port=5001)  # AuthorService runs on port 5000
