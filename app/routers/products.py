from fastapi import APIRouter
from app.services.dao.product import ProductDao
from app.schemas.product import SProduct



router = APIRouter(prefix="/api/products", tags=["products"])


@router.get("/")
async def get_products()->list[SProduct]:
      return await ProductDao.get_all()


@router.get("/{category_slug}")
async def get_products_by_category(category_slug:str)->list[SProduct]:
      ...

@router.post("/detail/{product_slug}")
async def product_detail(product_slug:str)->SProduct:
      ...


@router.post("/create")
async def create_product(product_data:SProduct):
      ...

@router.put("/detail/{product_slug}")
async def update_product(product_slug:str):
      ...


@router.delete("/delete")
async def delete_product(product_data_id:int):
      ...