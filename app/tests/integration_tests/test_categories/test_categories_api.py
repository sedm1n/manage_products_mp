import pytest

from httpx import AsyncClient


@pytest.mark.parametrize(
    "name, parent_id, is_active , status_code, expected_result",
    [
        ("test_add_and_get_category", 2, True, 201, True),
        ("test_add_and_get_category", 2, True, 409, False),
        
        
    ],
)
async def test_add_and_get_category(
    name: str, parent_id: int, is_active, status_code: int,expected_result: bool,  auth_asycn_client: AsyncClient
):
    created_cateory = await auth_asycn_client.post(
        "/api/category/create",
        json={"name": name, "parent_id": parent_id,"is_active": is_active},
    )
    if expected_result:
        assert created_cateory.status_code == status_code
        id_category = created_cateory.json()['category']['id']
        
        category = await auth_asycn_client.get(f"/api/category/detail/{id_category}")
        assert category.status_code == 200
        assert category.json()['name'] == name
    else:
        assert created_cateory.status_code == status_code

