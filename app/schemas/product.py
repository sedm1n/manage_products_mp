from pydantic import BaseModel, ConfigDict

class BaseConfig:
    from_attributes = True

class ProductBaseSchema(BaseModel):
    name: str
    description: str
    price: int
    image_url: str
    stock: int
    category_id: int
    

  


class ProductCreateSchema(ProductBaseSchema):
    pass 


class ProductInfoSchema(ProductBaseSchema):
    id: int
    name: str
    description: str
    price: int
    image_url: str
    stock: int
    category_id: int

    
