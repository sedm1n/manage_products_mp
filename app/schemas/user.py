from pydantic import BaseModel, EmailStr


class SUserRegister(BaseModel):
      username:str
      email : EmailStr
      password : str


class SUserAuth(BaseModel):
      email : EmailStr
      password : str