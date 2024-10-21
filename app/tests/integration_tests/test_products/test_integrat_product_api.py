import pytest

from httpx import AsyncClient


@pytest.mark.parametrize(
    "name, category_id, is_active , status_code",
    [
        ("test_product", 2, True, 201),
        
        
    ],
)
async def test_add_and_get_product(
    name, category_id, is_active, status_code, auth_asycn_client: AsyncClient
):
    created_product = await auth_asycn_client.post(
        "/api/products/create",
        json={"name": name, "category_id": category_id, "is_active": is_active, 
            "description": "string",
            "price": 10,
            "image_url": "string",
            "stock": 10,
            },
    )

    
    assert created_product.status_code == status_code
    slug_product = created_product.json()['product']['slug']
    
    product = await auth_asycn_client.get(f"/api/product/detail/{slug_product}")
    assert product.status_code == 200
    assert product.json()['name'] == name

