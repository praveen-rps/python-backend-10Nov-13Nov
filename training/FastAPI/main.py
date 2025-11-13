from fastapi import FastAPI
from pydantic import BaseModel

app= FastAPI()

class Product(BaseModel):
    name: str
    price: float
    qty: int

@app.get("/")
def home():
    return {"message": "Welcome to FastAPI!"}

@app.put("/put")
def put():
    return {"message": "Welcome to FastAPI! - PUT Method"}

@app.post("/post")
def post():
    return {"message": "Welcome to Post FastAPI!"}


@app.get("/product/{id}")
def get_product(id: int):
    return {"product_id": id}

@app.get("/search")
def search(name: str, price: float):
    return {"name": name, "price": price}

@app.post("/product")
def create_product(p: Product):
    return {"message": "Product added", "data": p}