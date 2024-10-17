from fastapi import APIRouter, HTTPException, status

from app.schemas.product import SCreateProduct, SProduct
from app.services.dao.category import CategoryDao
from app.services.dao.product import ProductDao
from slugify import slugify

router = APIRouter(prefix="/api/products", tags=["products"])


@router.get("/")
async def get_all_products() -> list[SProduct]:
    return await ProductDao.get_all()


@router.get("/{category_slug}")
async def get_products_by_category(category_slug: str = None) -> list[SProduct]:
    category = await CategoryDao.find_one_or_none(slug=category_slug)
    
    if not category:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Category {category_slug} not found",
        )
    products = await ProductDao.get_all(category_id=category.id)
    return products


@router.post("/detail/{product_slug}")
async def product_detail(product_slug: str):
    return await ProductDao.find_one_or_none(slug=product_slug)


@router.post("/create")
async def create_product(product_data: SCreateProduct):
    category = await CategoryDao.find_one_or_none(id=product_data.category_id)
    if not category:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Category {category.id} not found",
        )
    slug= slugify(product_data.name)
    data = product_data.dict()
    data['slug'] = slug
    await ProductDao.add(**data)

    return {"status_code": status.HTTP_201_CREATED, "message": "Product created"}


@router.put("/detail/{product_slug}")
async def update_product(product_slug: str, update_data:SCreateProduct):
    product = await ProductDao.find_one_or_none(slug=product_slug)
    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Product {product_slug} not found",
        )

    await ProductDao.update(product.id, **update_data.dict())
    return {"status_code": status.HTTP_200_OK, "message": "Product updated"}


@router.delete("/delete")
async def delete_product(product_id: int):
    existing_product = await ProductDao.find_one_or_none(id=product_id)
    if not existing_product:
        raise HTTPException(status_code=404, detail=f"Product {product_id} not found")
    await ProductDao.delete(product_id)

    return {"status_code": status.HTTP_200_OK, "message": "Product deleted"}
