from flask import Flask, render_template

app = Flask(__name__)

@app.route("/api/products")
def showproducts():
    products = [
        {"id":1001,"name":"Laptop","quantity":5, "price":7500},
        {"id":1002,"name":"Smarphone","quantity":35, "price":2500},
        {"id":1003,"name":"HeadPhones","quantity":29, "price":2000},
        {"id":1004,"name":"Keyboard","quantity":15, "price":500},
        {"id":1005,"name":"Mouse","quantity":105, "price":700}
    ]
    return render_template("products.html", products= products)


if __name__ == '__main__':
    app.run(debug=True)