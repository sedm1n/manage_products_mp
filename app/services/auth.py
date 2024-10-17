from datetime import datetime, timedelta

from jose import jwt
from app.backend.config import db_cfg
from passlib.context import CryptContext
from pydantic import EmailStr

from .dao.user import UserDao

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_password_hash(password):
      return pwd_context.hash(password)

def verify_password(plain_password, hashed_password):
      return pwd_context.verify(plain_password, hashed_password)


async def create_access_token(username: str, user_id: int, is_admin: bool, is_supplier: bool, is_customer: bool, expires_delta: timedelta):
    encode = {'sub': username, 'id': user_id, 'is_admin': is_admin, 'is_supplier': is_supplier, 'is_customer': is_customer}
    expires = datetime.now() + expires_delta
    encode.update({'exp': expires})
    return jwt.encode(encode, db_cfg.SECRET_KEY, algorithm='HS256')



async def authenticate_user(username:str, password:str):
      user = await UserDao.find_one_or_none(username=username)
      if not user or not verify_password(password, user.hashed_password):
            return None
      return user

