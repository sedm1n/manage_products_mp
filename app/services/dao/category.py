from sqlalchemy import select

from app.models.category import Category
from .base import BaseDao


class CategoryDao(BaseDao):
      model = Category