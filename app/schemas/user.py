from pydantic import BaseModel, EmailStr, ConfigDict

class BaseConfig:
    from_attributes = True

class UserBaseSchema(BaseModel):
      username:str
      password : str


class UserCreateSchema(UserBaseSchema):
      email : EmailStr


class UserAuthSchema(UserBaseSchema):
      pass 