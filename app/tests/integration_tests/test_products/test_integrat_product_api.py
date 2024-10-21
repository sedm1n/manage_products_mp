import pytest

from httpx import AsyncClient


@pytest.mark.parametrize(
    "name, category_id, description, price, stock,image_url , is_active , status_code",
    [
        ("test_create_product1", 1, "test_create_product1_desc", 99, 10, "image_url", True, 201),
        ("test_create_product2", 1, "test_create_product2_desc", 99, 10, "image_url", True, 201),
        
        
        
    ],
)
async def test_add_and_get_product(
    name: str, description:str, category_id: int, price:float, stock:int, image_url: str, is_active: bool, status_code, auth_asycn_client: AsyncClient
):
    created_product = await auth_asycn_client.post(
        "/api/products/create",
        json={"name": name, "category_id": category_id, "is_active": is_active, 
            "description": description,
            "price": price,
            "image_url": image_url,
            "stock": stock,
            },
    )

    
    assert created_product.status_code == status_code
    assert created_product.json()['product']['name'] == name
    
    slug_product = created_product.json()['product']['slug']
    
    
    product = await auth_asycn_client.get(f"/api/products/detail/{slug_product}")
    assert product.status_code == 200
    assert product.json()['name'] == name

