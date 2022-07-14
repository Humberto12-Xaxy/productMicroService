from typing import Optional
from pydantic import BaseModel

class Product(BaseModel):
    id: Optional[int] 
    name: str
    img_saucer: str
    description: str
    price: float
    menu_id: int

class ProductUpdate(BaseModel):
    id: int
    name: str
    img_saucer: str
    description: str
    price: float