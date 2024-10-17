from contextlib import asynccontextmanager

from sqlalchemy.ext.asyncio import AsyncSession

from app.backend.db import async_session


@asynccontextmanager
async def get_async_session() -> AsyncSession:
      async with async_session() as session:
        try:
            yield session
        finally:
            await session.close()
