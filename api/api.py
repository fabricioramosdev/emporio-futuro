from fastapi import APIRouter


from api.endpoint import product
from api.endpoint import user

api_router_v1 =  APIRouter()
api_router_v1.include_router(product.product_router, prefix='/product/', tags=['Products'])