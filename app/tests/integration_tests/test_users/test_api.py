from httpx import AsyncClient
import pytest


@pytest.mark.parametrize(
    "username, email, password, status_code",
    [
        ("testuser1", "testuser1@t.com", "test", 200),
        ("testuser1", "testu2ser@t.com", "test", 409),
    ],
)
async def test_register(
    username, email, password, status_code, asycn_client: AsyncClient
):
    response = await asycn_client.post(
        "/api/auth/register",
        json={"username": username, "email": email, "password": "test"},
    )

    assert response.status_code == status_code


@pytest.mark.parametrize(
    "username, password, status_code",
    [
        ("testuser1", "test", 200),
        ("testuser1_not", "test", 401),
        ("testuser1", "bad_test", 401),
        ("testuser1", "", 401),
        ("", "", 401),
    ],
)
async def test_login(username, password, status_code, asycn_client: AsyncClient):
    response = await asycn_client.post(
        "/api/auth/login", json={"username": username, "password": password}
    )

    assert response.status_code == status_code
