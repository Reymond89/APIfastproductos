

from fastapi import APIRouter, Response, status
from config.db import conn
from models.producto import productos
from schemas.producto import Producto
from starlette.status import HTTP_204_NO_CONTENT

producto = APIRouter()

@producto.get("/productos", response_model=list[Producto], tags=["productos"])
def get_productos():
    return conn.execute(productos.select()).fetchall()

@producto.post("/productos", response_model=Producto, tags=["productos"])
def create_producto(producto: Producto):
    new_user = {"id": producto.id, "ref": producto.ref, "name": producto.name, "price": producto.price, "stock": producto.stock}
    result = conn.execute(productos.insert().values(new_user))
    return conn.execute(productos.select().where(productos.c.id == result.lastrowid)).first()

@producto.get("/productos/{id}", response_model=Producto, tags=["productos"])
def get_producto(id: str):
    return conn.execute(productos.select().where(productos.c.id == id)).first()

@producto.put("/productos/{id}", response_model=Producto, tags=["productos"])
def update_producto(id: str, producto: Producto):
    conn.execute(productos.update().values(ref=producto.ref, name=producto.name, price=producto.price,
    stock=producto.stock).where(productos.c.id == id))
    return "update"

@producto.delete("/productos/{id}", status_code=status.HTTP_204_NO_CONTENT, tags=["productos"])
def delete_producto(id: str):
    conn.execute(productos.delete().where(productos.c.id == id))
    return Response(status_code=HTTP_204_NO_CONTENT)
