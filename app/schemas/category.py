from typing import Optional
from pydantic import BaseModel


class SCreateCategory(BaseModel):
    name: str
    parent_id: Optional[int] | None

    class Config:
        orm_mode = True    

class SCategory(BaseModel):
    name: str
    parent_id: Optional[int] | None
    slug: str
    is_active: bool
    
    class Config:
        orm_mode = True    