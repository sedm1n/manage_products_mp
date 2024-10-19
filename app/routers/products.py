from fastapi import APIRouter, HTTPException, status
from slugify import slugify

from app.schemas.product import ProductCreateSchema, ProductInfoSchema
from app.services.dao.category import CategoryDao
from app.services.dao.product import ProductDao

router = APIRouter(prefix="/api/products", tags=["products"])


@router.get("/")
async def get_all_products() -> list[ProductInfoSchema]:
    return await ProductDao.get_all()


@router.get("/{category_slug}")
async def get_products_by_category(category_slug: str = None) -> list[ProductInfoSchema]:
    category = await CategoryDao.find_one_or_none(slug=category_slug)

    if not category:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Category {category_slug} not found",
        )
    subcategories = await CategoryDao.get_all(parent_id=category.id)
    category_subcategories = [category.id] + [
        subcategory.id for subcategory in subcategories
    ]

    products = await ProductDao.get_all(category_id__in=category_subcategories)

    return products


@router.get("/detail/{product_slug}")
async def product_detail(product_slug: str) -> ProductInfoSchema:
    product = await ProductDao.find_one_or_none(slug=product_slug)
    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Product {product_slug} not found",
        )
    return product


@router.post("/create")
async def create_product(product_data: ProductCreateSchema):
    category = await CategoryDao.find_one_or_none(id=product_data.category_id)
    if not category:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Category {category.id} not found",
        )
    slug = slugify(product_data.name)
    data = product_data.dict()
    data["slug"] = slug
    await ProductDao.add(**data)

    return {"status_code": status.HTTP_201_CREATED, "message": "Product created"}


@router.put("/detail/{product_slug}")
async def update_product(product_slug: str, update_data: ProductCreateSchema):
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
