from fastapi import FastAPI
from fastapi import HTTPException
from pydantic import BaseModel

products = {}
app= FastAPI()

class Product(BaseModel):
    name: str
    price: float
    qty: int


@app.post("/product/{id}")
def add_product(id: int, p: Product):
    products[id] = p
    return {"msg": "Created"}
 
@app.get("/product/{id}")
def get_product(id: int):
    return products.get(id, {"error": "Not found"})
@app.put("/product/{id}")
def update_product(id: int, p: Product):
    products[id] = p
    return {"msg": "Updated"}

@app.delete("/product/{id}")
def delete_product(id: int):
    products.pop(id, None)
    return {"msg": "Deleted"}

@app.get("/item/{id}")
def get_item(id: int):
    if id not in products:
        raise HTTPException(status_code=404, detail="Item not found in the list")
    return products[id]