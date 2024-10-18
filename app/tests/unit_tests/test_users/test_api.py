from httpx import AsyncClient

async def test_register(asycn_client:AsyncClient):
      response =await asycn_client.post('/api/auth/register', json={
            "username": "test",
            "email": "test@test.com",
            "password": "test"
      })

      assert response.status_code == 200