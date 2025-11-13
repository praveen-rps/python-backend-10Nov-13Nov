from flask import Flask
from flask_restful import Api, Resource, reqparse
from flask import jsonify

app = Flask(__name__)
api = Api(app)

# Sample data for books (book_id, name, author)
books = [
    {"book_id": 1, "name": "The Catcher in the Rye", "author": "J.D. Salinger"},
    {"book_id": 2, "name": "1984", "author": "George Orwell"},
    {"book_id": 3, "name": "To Kill a Mockingbird", "author": "Harper Lee"},
    {"book_id": 4, "name": "Brave New World", "author": "Aldous Huxley"},
    {"book_id": 5, "name": "The Great Gatsby", "author": "F. Scott Fitzgerald"},
    {"book_id": 6, "name": "The Ghost", "author": "J.D. Salinger"}
]

class BookListResource(Resource):
    def get(self):
        """Returns all books"""
        return jsonify({"books": books})

class BookByAuthorResource(Resource):
    def get(self, author_name):
        """Returns books for the given author"""
        filtered_books = [book for book in books if book['author'].lower() == author_name.lower()]
        if filtered_books:
            return jsonify({"books": filtered_books})
        else:
            return jsonify({"message": "No books found for this author"}), 404

# Adding resources to the API
api.add_resource(BookListResource, '/books')
api.add_resource(BookByAuthorResource, '/books/author/<string:author_name>')

if __name__ == '__main__':
    app.run(debug=True)
