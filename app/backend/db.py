from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

from app.backend.config import cfg


DATABASE_URL = f"postgresql+asyncpg://{cfg.DB_USER}:{cfg.DB_PASSWORD}@{cfg.DB_HOST}:{cfg.DB_PORT}/{cfg.DB_NAME}"


engine = create_async_engine(DATABASE_URL, pool_pre_ping=True)
async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


class Base(DeclarativeBase):
    pass
