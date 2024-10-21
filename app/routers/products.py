from fastapi import APIRouter, HTTPException, status, Depends
from slugify import slugify

from app.schemas.product import ProductCreateSchema, ProductInfoSchema
from app.models.user import User
from app.services.dao.category import CategoryDao
from app.services.dao.product import ProductDao
from app.services.auth import get_current_user

router = APIRouter(prefix="/api/products", tags=["products"])


@router.get("/")
async def get_all_products() -> list[ProductInfoSchema]:
    return await ProductDao.get_all()




@router.get("/detail/{product_slug}")
async def product_detail(product_slug: str) -> ProductInfoSchema:
   
    product = await ProductDao.find_one_or_none(slug=product_slug)
   
    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Product {product_slug} not found",
        )
    return product


@router.post("/create", status_code=status.HTTP_201_CREATED)
async def create_product(product_data: ProductCreateSchema, user: User = Depends(get_current_user)):
    category = await CategoryDao.find_by_id(product_data.category_id)
    
    if not category:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Category {category.id} not found",
        )
    slug = slugify(product_data.name)
    product_dict = product_data.model_dump()
    product_dict["slug"] = slug
    
    try:
        result = await ProductDao.add(**product_dict)
    
    except ValueError as e:
        if str(e) == "Item already exists!":
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Product with the same name or data already exists",
            )
        else:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Internal server error",
            )

    

    return {"product": result, "status_code": "201", "message": "Product created"}


@router.put("/detail/{product_slug}")
async def update_product(product_slug: str, update_data: ProductCreateSchema, user: User = Depends(get_current_user)):
    product = await ProductDao.find_one_or_none(slug=product_slug)
    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Product {product_slug} not found",
        )

    await ProductDao.update(product.id, **update_data.dict())
    return {"status_code": status.HTTP_200_OK, "message": "Product updated"}


@router.delete("/delete")
async def delete_product(product_id: int, user: User = Depends(get_current_user)):
    existing_product = await ProductDao.find_one_or_none(id=product_id)
    if not existing_product:
        raise HTTPException(status_code=404, detail=f"Product {product_id} not found")
    await ProductDao.delete(product_id)

    return {"status_code": status.HTTP_200_OK, "message": "Product deleted"}
