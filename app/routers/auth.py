from datetime import datetime, timedelta

from fastapi import APIRouter, Depends, HTTPException, Response, status

from jose import JWTError, jwt
from typing_extensions import Annotated

from app.models import User
from app.schemas.user import UserAuthSchema, UserCreateSchema
from app.services.auth import (authenticate_user, create_access_token,
                               get_current_user, get_password_hash)
from app.services.dao.user import UserDao

router = APIRouter(prefix="/api/auth", tags=["auth"])






@router.post("/register", status_code=status.HTTP_201_CREATED)
async def register(user_data:UserCreateSchema):
      
      existing_user = await UserDao.find_one_or_none(username=user_data.username)
      if existing_user:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="User already exists")
      existing_email = await UserDao.find_one_or_none(email=user_data.email)
      
      if existing_email:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f"Email {user_data.email} user already exists")

      hashed_password = get_password_hash(user_data.password)
      
      await UserDao.add(username=user_data.username, email=user_data.email, hashed_password=hashed_password)
      return {"message": "User created"}





@router.post('/login')
async def login(response: Response,form_data: UserAuthSchema):
    
    user = await authenticate_user(form_data.username, form_data.password) 
    print(user)
    if not user or not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Could not validate user'
        )

    token = await create_access_token(user.username, user.id, user.is_admin, user.is_supplier, user.is_customer,
                                expires_delta=timedelta(minutes=20))
    response.set_cookie(key="access_token", value=token, httponly=True)
    return {
        'access_token': token,
        'token_type': 'bearer'
    }


@router.get('/logout')
async def logout(response: Response, user: User = Depends(get_current_user)):
    response.delete_cookie(key="access_token")
    return {'message': 'User logged out'}

@router.get('/read_current_user')
async def read_current_user(user: User = Depends(get_current_user)):

    return user