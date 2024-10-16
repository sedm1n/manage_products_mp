from fastapi import APIRouter, status
from slugify import slugify

from app.schemas.category import SCategory
from app.services.dao.category import CategoryDao

router = APIRouter(prefix="/api/category", tags=["category"])


@router.get("/")
async def get_categories()->list[SCategory]:
      ...

@router.post("/create")
async def create_category(category_data:SCategory):
      await CategoryDao.add(
            name=category_data.name, 
            parent_id=category_data.parent_id, 
            slug=slugify(category_data.name), is_active=True)
      return {'status_code':status.HTTP_201_CREATED, 'message':'Category created'}


@router.put("/detail/{category_slug}")
async def update_product(category_slug:str):
      ...


@router.delete("/delete")
async def delete_category(category_id:int):
      ...