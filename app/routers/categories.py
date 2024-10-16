from fastapi import APIRouter
from app. import CategoryDao
from app.schemas.category import SCategry



router = APIRouter(prefix="/api/category", tags=["category"])


@router.get("/")
async def get_categories()->list[SCategory]:

@router.post("/create")
async def create_category(category_data:SCategory):
      ...

@router.put("/detail/{category_slug}")
async def update_product(category_slug:str):
      ...


@router.delete("/delete")
async def delete_category(category_id:int):
      ...