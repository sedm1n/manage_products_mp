from app.models.user import User
from .base import BaseDao


class UserDao(BaseDao):
      model = User