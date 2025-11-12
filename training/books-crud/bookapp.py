from flask import Flask, render_template, url_for, request, redirect
import sqlite3
import mysql.connector
import pymysql

app = Flask(__name__)
database = "books.db"

def get_db_connection1():
    try:
        conn = pymysql.connect(
            host='localhost',      # Host where MySQL is running (localhost in this case)
            database='books',    # Your database name
            user='root',           # MySQL username
            password='rps12345'  # MySQL password (replace with your actual password)
        )
        return conn
    except sqlite3.Error as e:
        print("Error while connecting to MySQL", e)
        return None


def get_db_connection():
    conn = sqlite3.connect('books.db')
    conn.row_factory = sqlite3.Row  # To access columns by name
    return conn

# Initialize the database (you can run this separately to create the database)
def init_db():
    conn = get_db_connection()
    conn.execute('''CREATE TABLE IF NOT EXISTS books (
                        bookid INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL,
                        author TEXT NOT NULL);''')
    conn.commit()
    conn.close()


@app.route("/")
def home():
    return render_template("home.html")

@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/books")
def displaybooks():
    conn = get_db_connection()
    cursor = conn.cursor()  
    query = "select * from books"
    cursor.execute(query)
    books = cursor.fetchall()
    return render_template("books.html", books=books)

@app.route("/save", methods=["POST"])
def addData():
    bookid = request.form.get('bookid')
    name = request.form.get('name')
    author = request.form.get('author')
    conn = get_db_connection()
    cursor = conn.cursor()  
    print(bookid,name,author)
    query = "insert into books(bookid,name,author) values(?,?,?)"
    data = (bookid,name,author)
    cursor.execute(query,data)
    conn.commit()
    return render_template("home.html")


@app.route("/edit/<int:bookid>")
def edit_book(bookid):
    conn = get_db_connection()
    cursor = conn.cursor()  
    cursor.execute("select * from books where bookid = ?", (bookid,))
    book = cursor.fetchone()
    conn.close()
    return render_template("edit.html", book=book)

@app.route("/update", methods=["POST"])
def update_book():
    bookid = request.form.get('bookid')
    name = request.form.get('name')
    author = request.form.get('author')
    conn = get_db_connection()
    cursor = conn.cursor()  
    print(bookid,name,author)
    query = "update books set name=?, author = ? where bookid = ?"
    data = (name,author,bookid)
    cursor.execute(query,data)
    conn.commit()
   # books = cursor.execute("select * from books").fetchall()
    #return render_template("books.html",books=books)
    return redirect("/books")

@app.route("/delete/<int:bookid>")
def delete_book(bookid):
    conn = get_db_connection()
    cursor = conn.cursor()  
    cursor.execute("delete from books where bookid = ?", (bookid,))
    conn.commit()
    return redirect("/books")


if __name__ == '__main__':
    app.run(debug=True)

