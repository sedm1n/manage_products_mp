from sqlalchemy import select

from app.models.product import Product

from .base import BaseDao



class ProductDao(BaseDao):
      model = Product
      
      