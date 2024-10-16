from pydantic import BaseModel
class CreateProduct(BaseModel):
    
    name: str
    description: str
    price: int
    image_url: str
    stock: int
    category_id: int

    class Config:
        orm_mode = True    

    



