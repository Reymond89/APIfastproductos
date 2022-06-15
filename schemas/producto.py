
from pydantic import BaseModel
from typing import Optional

class Producto(BaseModel):
    id: Optional[str]
    ref: int
    name: str
    price: int
    stock: int

    