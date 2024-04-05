# schemas/product.py
from pydantic import BaseModel
import uuid
from typing import Optional

class ProductBase(BaseModel):
    description: str
    price: float
    is_on_sale: Optional[bool] = False
    discount_rate: Optional[float] = None
    tag: Optional[str] = None

class ProductCreate(ProductBase):
    pass  # All fields from ProductBase are required for creation

class ProductRead(ProductBase):
    id: uuid.UUID

    class Config:
        orm_mode = True
