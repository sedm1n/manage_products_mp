from pydantic import BaseModel


class SCreateProduct(BaseModel):
    
    name: str
    description: str
    price: int
    image_url: str
    stock: int
    category_id: int

    class Config:
        orm_mode = True    

    
class SProduct(BaseModel):
    
    name: str
    description: str
    price: int
    image_url: str
    stock: int
    category_id: int

    class Config:
        orm_mode = True    




