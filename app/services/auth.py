from datetime import datetime, timedelta

from fastapi import Annotated, Depends, HTTPException, Request, status
from jose import JWTError, jwt
from passlib.context import CryptContext


from app.backend.config import cfg
from app.models.user import User

from .dao.user import UserDao

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_password_hash(password):
    return pwd_context.hash(password)


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


async def create_access_token(
    username: str,
    user_id: int,
    is_admin: bool,
    is_supplier: bool,
    is_customer: bool,
    expires_delta: timedelta,
):
    encode = {
        "sub": username,
        "id": user_id,
        "is_admin": is_admin,
        "is_supplier": is_supplier,
        "is_customer": is_customer,
    }
    expires = datetime.now() + expires_delta
    encode.update({"exp": expires})
    return jwt.encode(encode, cfg.SECRET_KEY, algorithm="HS256")


async def authenticate_user(username: str, password: str):
    user = await UserDao.find_one_or_none(username=username)
    if not user or not verify_password(password, user.hashed_password):
        return None
    return user


def get_token(request: Request):
    token = request.cookies.get("access_token")
    if not token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="No access token supplied"
        )
    return token


async def get_current_user(token: Annotated[str, Depends(get_token)]):
    try:
        payload = jwt.decode(token, cfg.SECRET_KEY, algorithms=["HS256"])

    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Could not validate JWT token"
        )
    username: str = payload.get("sub")
    user_id: int = payload.get("id")
    is_admin: str = payload.get("is_admin")
    is_supplier: str = payload.get("is_supplier")
    is_customer: str = payload.get("is_customer")

    
    if username is None or user_id is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, 
            detail="Could not validate user")
    
    expire = payload.get("exp")
    
    if (expire is None) or (int(expire) < datetime.now(datetime.UTC).timestamp()):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="No access token supplied"
        )
    
    user = await UserDao.find_by_id(id=int(user_id))
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return user 

async def chek_admin(user: User = Depends(get_current_user)):
    if not user.is_admin:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not enough permissions")
    return user
    