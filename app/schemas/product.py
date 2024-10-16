from pydantic import BaseModel


class SProduct(BaseModel):
    id: int
    name: str
    description: str
    price: float
    stock: int
    category_id: int
    
    class Config:
        orm_mode = True