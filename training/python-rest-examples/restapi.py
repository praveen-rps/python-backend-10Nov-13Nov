from flask import Flask, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

books = [
   {"bookid":1, "name":"Python Basics", "author":"John"},
   {"bookid":2, "name":"Oracle", "author":"Philip"},
   {"bookid":3, "name":"Flask Guide", "author":"Charlie"},
]

# GET - /books --> return all the books
# POST - /books --> add book to existing books

# /books/<int:bookid> --GET -- Search the book with given id
# /books/<int:bookid> -- PUT -- modify the book details for the given bookid
# /books/<int:bookid> -- DELETE -- delete the book with given bookid

class Book(Resource):
   def put(self,bookid):
      data = request.get_json()
      for book in books:
         if book['bookid'] == bookid:
            book.update(data)
            return {"message":"Book data updated", "book":book}, 200
      return {"message":"Book not found"}, 404
   
   def get(self, bookid):
      for book in books:
         if book['bookid'] == bookid:
            return book,200
      return {"message" : "Book is not found"}, 404
   
   def delete(self,bookid):
      global books
      books = [b  for b in books if b['bookid'] != bookid]
      return {"message":"Book deleted"}, 200

class BooksList(Resource):
   def get(self):
      return {"books":books}, 200 # return all the books
   def post(self):
      book = request.get_json()
      books.append(book)
      return {"message":"Book Added","book":book}, 201
   


   
class Hello(Resource):
    def get(self):
       return {"message":" Hello World"}
    
    def post(self):
       return {"message":"Post Method is called..!"}
    
    def put(self):
       return {"message":"Put Method is called..!"}

# Api end points
api.add_resource(Hello, "/")
api.add_resource(BooksList, "/books")
api.add_resource(Book,"/books/<int:bookid>")

if __name__ == '__main__':
 app.run(debug=True)