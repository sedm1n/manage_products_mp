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
        "/api/product/create",
        json={"name": name, "category_id": category_id, "is_active": is_active},
    )

    
    assert created_product.status_code == status_code
    id_product = created_product.json()['product']['id']
    
    product = await auth_asycn_client.get(f"/api/product/detail/{id_product}")
    assert product.status_code == 200
    assert product.json()['name'] == name

