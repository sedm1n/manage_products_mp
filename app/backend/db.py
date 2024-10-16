from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

from app.config import db_cfg


DATABASE_URL = f"postgresql+asyncpg://{db_cfg.DB_USER}:{db_cfg.DB_PASSWORD}@{db_cfg.DB_HOST}:{db_cfg.DB_PORT}/{db_cfg.DB_NAME}"


engine = create_async_engine(DATABASE_URL, pool_pre_ping=True)
async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


class Base(DeclarativeBase):
    pass
