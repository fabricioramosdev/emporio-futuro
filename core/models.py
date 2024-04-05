from sqlalchemy import (Column, String, Integer, Float, Boolean, ForeignKey, DateTime, Table)
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.postgresql import UUID
import uuid

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False)
    cpf = Column(String, unique=True, nullable=False)
    credit_card_number = Column(String, nullable=False)
    address = Column(String, nullable=False)
    password = Column(String, nullable=False)

class Product(Base):
    __tablename__ = 'product'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    description = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    is_on_sale = Column(Boolean, default=False)
    discount_rate = Column(Float)
    tag = Column(String)
    categories = relationship('Category', secondary='product_category', back_populates='products')

class Category(Base):
    __tablename__ = 'category'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False)
    description = Column(String)
    products = relationship('Product', secondary='product_category', back_populates='categories')

product_category_table = Table('product_category', Base.metadata,
    Column('product_id', ForeignKey('product.id'), primary_key=True),
    Column('category_id', ForeignKey('category.id'), primary_key=True)
)

class Order(Base):
    __tablename__ = 'order'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(ForeignKey('user.id'), nullable=False)
    date_placed = Column(DateTime, nullable=False)
    status = Column(String, nullable=False)
    user = relationship('User', back_populates='orders')
    details = relationship('OrderDetail', back_populates='order')

User.orders = relationship('Order', back_populates='user')

class OrderDetail(Base):
    __tablename__ = 'order_detail'
    order_id = Column(ForeignKey('order.id'), primary_key=True)
    product_id = Column(ForeignKey('product.id'), primary_key=True)
    quantity = Column(Integer, nullable=False)
    price_at_time = Column(Float, nullable=False)
    order = relationship('Order', back_populates='details')
    product = relationship('Product')

class Inventory(Base):
    __tablename__ = 'inventory'
    product_id = Column(ForeignKey('product.id'), primary_key=True)
    quantity_available = Column(Integer, nullable=False)
    product = relationship('Product')
