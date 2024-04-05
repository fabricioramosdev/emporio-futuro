from fastapi import APIRouter
from fastapi import Depends
from fastapi import status
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import Product  # Ensure you have this model defined

from core.deps import get_db_session

product_router = APIRouter()

@product_router.post("/products/")  # Define ProductRead schema
async def create_product(product: Product, db: AsyncSession = Depends(get_db_session)):  # Define ProductCreate schema
    db_product = Product(**product.dict())
    db.add(db_product)
    await db.commit()
    await db.refresh(db_product)
    return db_product

# Implement read, update, delete operations for Product