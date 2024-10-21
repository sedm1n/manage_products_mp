from typing import Optional

from pydantic import BaseModel


class BaseConfig:
    from_attributes = True




class CategoryBaseSchema(BaseModel):
    name: str
    parent_id: Optional[int] = None
    is_active: bool
        
   
    
class CategoryCreateSchema(CategoryBaseSchema):
    pass


class CategoryInfoSchema(CategoryBaseSchema):
    id: int
    slug: str
    