import asyncio
import json

import pytest
from fastapi.testclient import TestClient
from httpx import AsyncClient
from sqlalchemy import insert

from app.backend.db import Base, async_session, cfg, engine
from app.models.category import Category
from app.models.orders import Order, OrderItem
from app.models.product import Product
from app.models.user import ShippingAddress, User
from app.main import app

@pytest.fixture(scope="session", autouse=True)
async def prepare_db():
      assert cfg.MODE == "TEST"

      async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.drop_all)
            await conn.run_sync(Base.metadata.create_all)
      
      def open_mock_json(model:str):
            with open(f"app/tests/fixtures/mock_{model}.json") as f:
                  return json.load(f)
            
      users = open_mock_json("users")
      products = open_mock_json("products")
      categories = open_mock_json("categories")
      # orders = open_mock_json("order")

      async with async_session() as session:
            async with session.begin():
                  add_users = insert(User).values(users)
                  add_products = insert(Product).values(products)
                  add_categories = insert(Category).values(categories)

                  for query in [add_users, add_categories, add_products, ]:
                        await session.execute(query)

                  await session.commit()



@pytest.fixture(scope="session")
def event_loop(request):
      """ Create an instance of the default event loop for each test case """
      loop = asyncio.get_event_loop_policy().new_event_loop()
      yield loop
      loop.close()


@pytest.fixture(scope="function")
async def asycn_client():
      async with AsyncClient(app=app, base_url="http://test") as ac:
            yield ac


@pytest.fixture(scope="function")
async def auth_asycn_client():
      async with AsyncClient(app=app, base_url="http://test") as ac:
            await ac.post("/api/auth/register", json={"username": "authtestuser1", "email": "authtestuser1@t.com", "password": "test"})
            await ac.post("/api/auth/login", json={"username": "authtestuser1", "password": "test"})

            assert ac.cookies["access_token"]
            
            yield ac


@pytest.fixture(scope="function")
async def session():
      async with async_session() as session:
            yield session