from fastapi import FastAPI
from models.item_model import Item



app = FastAPI()


fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

@app.get("/")
async def root():
    return {"message": "hola mundo"}

@app.get("/saludo")
async def saludo():
    return {"message": "saludo en otra pagina"}


@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return{"item_name": item.name, "price": item.price, "item_id": item_id}
