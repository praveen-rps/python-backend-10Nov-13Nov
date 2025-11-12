from flask import Flask, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

books = [
   {"bookid":1, "name":"Python Basics", "author":"John"},
   {"bookid":2, "name":"Java Basics", "author":"John"},
   {"bookid":3, "name":"evil dead", "author":"Alice"},
   {"bookid":4, "name":"Data Science", "author":"Bob"},
]

# GET - /books --> return all the books
# POST - /books --> add book to existing books

# /books/<int:bookid> --GET -- Search the book with given id
# /books/<int:bookid> -- PUT -- modify the book details for the given bookid
# /books/<int:bookid> -- DELETE -- delete the book with given bookid

class Book(Resource):
    def get(self, name):
      data = []
      print(name)
      for book in books:
         if book['name'] == name:
            data.append(book)
      return data,200
      
class BooksList(Resource):
   def get(self):
      return {"books":books}, 200 # return all the books
   def post(self):
      book = request.get_json()
      books.append(book)
      return {"message":"Book Added","book":book}, 201
   


# Api end points
api.add_resource(BooksList, "/books")
api.add_resource(Book,"/books/<name>")

if __name__ == '__main__':
 app.run(debug=True, port=5001)