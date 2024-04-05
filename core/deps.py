from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine

from core.configs import settings


DATABASE_URL = settings.DB_URL
engine = create_async_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine, class_=AsyncSession)

app = FastAPI()

# Dependency to get DB session
async def get_db_session():
    async with SessionLocal() as session:
        yield session