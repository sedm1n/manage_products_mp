import json

import pytest
from sqlalchemy import insert

from app.backend.db import Base, async_session, cfg, engine
from app.models.category import Category
from app.models.orders import Order, OrderItem
from app.models.product import Product
from app.models.user import ShippingAddress, User


@pytest.fixture(scope="session", autouse=True)
async def prepare_db():
      assert cfg.MODE == "TEST"

      async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.drop_all)
            await conn.run_sync(Base.metadata.create_all)
      
      def open_mock_json(model:str):
            with open(f"app/tests/fixtures/mock_{model}.json") as f:
                  return json.load(f)
            
      users = open_mock_json("user")
      products = open_mock_json("product")
      categories = open_mock_json("category")
      # orders = open_mock_json("order")

      async with async_session() as session:
            async with session.begin():
                  add_users = insert(User).values(users)
                  add_products = insert(Product).values(products)
                  add_categories = insert(Category).values(categories)

                  for query in [add_users, add_products, add_categories]:
                        await session.execute(query)

                  await session.commit()



@pytest.fixture(scope="session")
def event_loop(request):
      """ Create an instance of the default event loop for each test case """
      loop = asyncio.get_event_loop_policy().new_event_loop()
      yield loop
      loop.close()