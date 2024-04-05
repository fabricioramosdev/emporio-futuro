# schemas/user.py
from pydantic import BaseModel, Field
import uuid
from typing import Optional

class UserBase(BaseModel):
    name: str
    cpf: str
    credit_card_number: str = Field(None, alias="creditCardNumber")
    address: str

class UserCreate(UserBase):
    password: str

class UserRead(UserBase):
    id: uuid.UUID

    class Config:
        orm_mode = True
