from sqlalchemy import delete, insert, select, update

from app.backend.db_depents import get_async_session


class BaseDao:
    model = None

    @classmethod
    async def find_by_id(cls, model_id: int):
        async with get_async_session() as session:
            query = select(cls.model).filter_by(model_id=id)
            result = await session.execute(query)

            return result.scalar_one_or_none()

    @classmethod
    async def find_one_or_none(cls, **filter_by):
        async with get_async_session() as session:
            query = select(cls.model).filter_by(**filter_by)
            result = await session.execute(query)

            return result.scalar_one_or_none()

    @classmethod
    async def get_all(cls, **filter_by):
        async with get_async_session() as session:
            query = select(cls.model).filter_by(**filter_by)
            result = await session.execute(query)

            return result.scalars().all()

    @classmethod
    async def add(cls, **data):
        async with get_async_session() as session:
            query = insert(cls.model).values(**data)
            await session.execute(query)
            await session.commit()

    @classmethod
    async def delete(cls, model_id: int):
        async with get_async_session() as session:
            query = delete(cls.model).where(cls.model.id == model_id)
            await session.execute(query)
            await session.commit()

    @classmethod
    async def update(cls, model_id: int, **data):
        async with get_async_session() as session:
            query = update(cls.model).where(cls.model.id == model_id).values(**data)
            await session.execute(query)
            await session.commit()
