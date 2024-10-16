from app.backend.db import async_session

async def get_async_session() -> AsyncSession:
      db = await async_session()
      try:
            yield db
      finally:
            await db.close()
            