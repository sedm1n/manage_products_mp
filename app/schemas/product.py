from typing import Optional
from decimal import Decimal
from pydantic import BaseModel


class BaseConfig:
    from_attributes = True

class ProductBaseSchema(BaseModel):
    name: str
    description: Optional[str]
    price: Optional[Decimal]
    image_url: Optional[str]
    stock: Optional[int]
    category_id: int
    

  


class ProductCreateSchema(ProductBaseSchema):
    pass 


class ProductInfoSchema(ProductBaseSchema):
    id: int
    slug: str
    
    
    

    
