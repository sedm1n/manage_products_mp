from datetime import timedelta


from passlib.context import CryptContext
from pydantic import EmailStr

from .dao.user import UserDao

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_password_hash(password):
      return pwd_context.hash(password)

def verify_password(plain_password, hashed_password):
      return pwd_context.verify(plain_password, hashed_password)

SECRET_KEY= "8sCmO0CxC9uFNsXU20mqKEWLi868jMT5NvJ/quUJn8s="
def create_access_token(data: dict):
      to_encode = data.copy()
      expire = datetime.utcnow() + timedelta(minutes=30)
      to_encode.update({"exp": expire})
      encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm="HS256")
      return encoded_jwt



async def authenticate_user(email:EmailStr, password:str):
      user = await UserDao.find_one_or_none(email=email)
      if not user and not verify_password(password, user.hashed_password):
            return None
      return user