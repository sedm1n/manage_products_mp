from pydantic import BaseModel, EmailStr, ConfigDict


class SUserRegister(BaseModel):
      username:str
      email : EmailStr
      password : str

      model_config = ConfigDict(orm_mode = True)

class SUserAuth(BaseModel):
      username : str
      password : str

      model_config = ConfigDict(orm_mode = True)