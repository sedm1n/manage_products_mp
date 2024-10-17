from typing_extensions import Annotated
from app.models import User
from fastapi import APIRouter, HTTPException, Response, status, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from app.schemas.user import SUserAuth, SUserRegister
from app.services.auth import (authenticate_user, create_access_token,
                               get_password_hash, verify_password)
from app.services.dao.user import UserDao

router = APIRouter(prefix="/api/user", tags=["user"])

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/user/token")



@router.post("/register")
async def register(user_data:SUserRegister):
      existing_user = await UserDao.find_one_or_none(email=user_data.username)
      if existing_user:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="User already exists")
      
      hashed_password = get_password_hash(user_data.password)
      await UserDao.add(username=user_data.username, email=user_data.email, hashed_password=hashed_password)
      return {"message": "User created"}





@router.post('/token')
async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    
    user = await authenticate_user(form_data.username, form_data.password)
    

    if not user or not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Could not validate user'
        )

    return {
        'access_token': user.email,
        'token_type': 'bearer'
    }

@router.get('/read_current_user')
async def read_current_user(user: User = Depends(oauth2_scheme)):
    return user