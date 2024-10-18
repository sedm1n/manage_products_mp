from httpx import AsyncClient
import pytest


@pytest.mark.parametrize("username, email, password, status_code", [
 ("testuser", "testuser@t.com", "test", 200),
 ("testuser", "testuser@t.com", "test", 409),
])
async def test_register(username, email, password,status_code,asycn_client:AsyncClient):
      response =await asycn_client.post('/api/auth/register', json={
            "username": username,
            "email": email,
            "password": "test"
      })

      assert response.status_code == status_code