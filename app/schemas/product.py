from pydantic import BaseModel, ConfigDict


class SCreateProduct(BaseModel):
    name: str
    description: str
    price: int
    image_url: str
    stock: int
    category_id: int

    model_config = ConfigDict(orm_mode = True) 


class SProduct(BaseModel):
    id: int
    name: str
    description: str
    price: int
    image_url: str
    stock: int
    category_id: int

    model_config = ConfigDict(orm_mode = True) 
