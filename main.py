from typing import Any, List, Union
from fastapi import FastAPI
from models.item_model import Item
from pydantic import BaseModel



app = FastAPI()

class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None
    tags: List[str] = []


fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"},{"item_name": "Buzzz"}]

@app.get("/")
async def root():
    return {"message": "hola mundo"}

@app.get("/saludo")
async def saludo():
    return {"message": "saludo en otra pagina"}


@app.post("/items/", response_model=Item)
async def create_item(item: Item) -> Any:
    return item


@app.get("/items/", response_model=List[Item])
async def read_items() -> Any:
    return [
        {"name": "Portal Gun", "price": 42.0},
        {"name": "Plumbus", "price": 32.0},
    ]
