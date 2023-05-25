from typing import Optional
from uuid import uuid4 as uuid
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

class Producto(BaseModel):
    id: Optional[str]
    nombre: str
    precio_compra: float
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
    raise HTTPException(status_code=404,detail='id de producto no encontrado')

@app.delete('/productos/{producto_id}')
def eliminar_producto(producto_id: str):
    for producto in productos:
        if producto.id == producto_id:
            productos.remove(producto)
            return {'mensaje': 'Producto eliminado'}
    raise HTTPException(status_code=404,detail='id de producto no encontrado, no se puede eliminar')

@app.put('/productos/{producto_id}')
def actualizar_producto(producto_id: str, producto: Producto):
    for i, producto_encontrado in enumerate(productos):
        if producto_encontrado.id == producto_id:
            productos[i].nombre = producto.nombre
            productos[i].precio_compra = producto.precio_compra
            productos[i].precio_venta = producto.precio_venta
            productos[i].proveedor = producto.proveedor
            return productos[i]
    raise HTTPException(status_code=404, detail='id de producto no encontrado, modificar')

