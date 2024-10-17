
from typing import List
from fastapi import APIRouter, status, HTTPException
from fastapi.security import OAuth2PasswordBearer

from slugify import slugify

from app.schemas.category import SCategory, SCreateCategory
from app.services.dao.category import CategoryDao

router = APIRouter(prefix="/api/category", tags=["category"])

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/category/token")

@router.get("/")
async def get_categories()->List[SCategory]:
      result = await CategoryDao.get_all()
      if result is None:
            raise HTTPException(status_code=404, detail="Categories not found")
      return result

@router.post("/create")
async def create_category(category_data:SCreateCategory):
      if category_data.parent_id :
            existing_category = await CategoryDao.find_one_or_none(id=category_data.parent_id)
            
            if not existing_category:
                  raise HTTPException(status_code=404, detail=f"Parent category {category_data.parent_id} not found")
      
      await CategoryDao.add(
            name=category_data.name, 
            parent_id=category_data.parent_id, 
            slug=slugify(category_data.name), is_active=True)
      return {'status_code':status.HTTP_201_CREATED, 'message':'Category created'}


@router.put("/detail/{category_id}")
async def update_category(category_id:int, update_data:SCreateCategory):
      category = await CategoryDao.find_one_or_none(id=category_id)
      if not category:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Category {category_id} not found")
      await CategoryDao.update(category_id, **update_data.dict())
      return {'status_code':status.HTTP_200_OK, 'message':'Category updated'}
      


@router.delete("/delete")
async def delete_category(category_id:int):
      existing_category = await CategoryDao.find_one_or_none(id=category_id)
      if not existing_category:
            raise HTTPException(status_code=404, detail=f"Category {category_id} not found")
      await CategoryDao.delete(category_id)
      return {'status_code':status.HTTP_200_OK, 'message':'Category deleted'}