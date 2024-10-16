from sqlalchemy import select

from app.models.product import Product
from .base import BaseDao

# from .schemas import ProductCreate, ProductUpdate

class ProductDao(BaseDao):
      model = Product
      
      