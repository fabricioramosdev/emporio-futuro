from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import declarative_base

from sqlalchemy.future import select
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, String, select
from sqlalchemy.dialects.postgresql import UUID
from pydantic import BaseModel, Field
import uuid


# Import from the core package
from core.database import SessionLocal

# Define the Base class for declarative mapping
Base = declarative_base()

# Models
class User(Base):
    __tablename__ = 'users'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False)
    # Add other fields as needed

# Pydantic Schemas
class UserCreate(BaseModel):
    name: str
    # Include other fields necessary for creation

class UserRead(BaseModel):
    id: uuid.UUID
    name: str
    # Include other fields that should be visible in the API response

    class Config:
        orm_mode = True

# Dependency to get DB session
async def get_db_session():
    async with SessionLocal() as session:
        yield session

app = FastAPI()

# Dependency to get DB session
async def get_db_session():
    async with SessionLocal() as session:
        yield session


@app.post("/users/", response_model=UserRead)
async def create_user(user: UserCreate, db: AsyncSession = Depends(get_db_session)):
    db_user = User(name=user.name)  # Adjust based on your User model
    db.add(db_user)
    await db.commit()
    await db.refresh(db_user)
    return db_user

@app.get("/users/{user_id}", response_model=UserRead)
async def read_user(user_id: uuid.UUID, db: AsyncSession = Depends(get_db_session)):
    async with db:
        result = await db.execute(select(User).filter(User.id == user_id))
        user = result.scalars().first()
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        return user

# Additional routes can be added here

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        #workers=3,
        reload=True,
        use_colors=True
    )