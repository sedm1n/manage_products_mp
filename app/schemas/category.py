from typing import Optional
from pydantic import BaseModel


class SCreateCategory(BaseModel):
    name: str
    parent_id: Optional[int]

    class Config:
        orm_mode = True    

