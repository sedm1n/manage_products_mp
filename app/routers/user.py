from fastapi import APIRouter, HTTPException, Response, status

from app.schemas.user import SUserAuth, SUserRegister
from app.services.auth import (authenticate_user, create_access_token,
                               get_password_hash, verify_password)
from app.services.dao.user import UserDao

router = APIRouter(prefix="/api/user", tags=["user"])


@router.post("/register")
async def register(user_data:SUserRegister):
      existing_user = await UserDao.find_one_or_none(email=user_data.email)
      if existing_user:
            raise HTTPException(status_code=400)
      hashed_password = get_password_hash(user_data.password)
      await UserDao.add(email=user_data.email, hashed_password=hashed_password)
      return {"message": "User created"}


@router.post("/login")
async def user_login(response:Response, user_data:SUserAuth):
      user = await authenticate_user(email=user_data.email, password=user_data.password)
      if not user:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect email or password")
      access_token = create_access_token(data={"sub": user.id})
      response.set_cookie(key="access_token", value=f"Bearer {access_token}", httponly=True)
      return {"access_token": user.email, "token_type": "bearer"}
      
