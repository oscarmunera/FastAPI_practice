from typing import Optional
from uuid import uuid4 as uuid
from fastapi import FastAPI
from pydantic import BaseModel

class Producto(BaseModel):
    id: Optional[str]
    nombre: str
    precio_compras: float
    precio_venta: float
    proveedor: str

app = FastAPI()

productos = []

@app.get('/')
def index():
    return {'mensaje': 'Bienvenidos a la API de productos'}


@app.get('/productos')
def obtener_productos():
    return productos


@app.post('/productos')
def crear_productos(producto: Producto):
    producto.id = str(uuid())
    productos.append(producto)
    return {'mensaje': 'producto creado'}

@app.get('/productos/{producto_id}')
def obtener_product_id(producto_id: str):
    for producto in productos:
        if producto.id == producto_id:
            return producto
    return {'mensaje': 'proucto no encontado'}    