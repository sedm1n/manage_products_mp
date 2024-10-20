from sys import exc_info
from app.logger import logger
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from sqlalchemy import delete, insert, select, update

from app.backend.db_depents import get_async_session


class BaseDao:
    model = None

    @classmethod
    async def find_by_id(cls, model_id: int):
        async with get_async_session() as session:
            query = select(cls.model).filter_by(id=model_id)
            try:
                result = await session.execute(query)
                return result.scalar_one_or_none()
            except SQLAlchemyError as e:
                extra = {"model_id": model_id}
                logger.error(e, extra=extra, exc_info=True)
                return None

    @classmethod
    async def find_one_or_none(cls, **filter_by):
        async with get_async_session() as session:
            query = select(cls.model).filter_by(**filter_by)
            try:
                result = await session.execute(query)
                return result.scalar_one_or_none()

            except SQLAlchemyError as e:
                extra = {"filter": filter_by}
                logger.error(e, extra=extra, exc_info=True)
                return None

    @classmethod
    async def get_all(cls, **filter_by):
        async with get_async_session() as session:
            query = select(cls.model).filter_by(**filter_by)
            try:
                result = await session.execute(query)
                return result.scalars().all()

            except SQLAlchemyError as e:
                extra = {"filter_by": filter_by}
                logger.error(e, extra=extra, exc_info=True)
                return None

    @classmethod
    async def add(cls, **data):
        
        if not data:
            return None
        
        async with get_async_session() as session:
            query = insert(cls.model).values(**data).returning(cls.model)

            try:
                result = await session.execute(query)
                await session.commit()
                return result.scalar_one()

            except SQLAlchemyError as e:
                extra = {"fdata": data}
                logger.error(e, extra=extra, exc_info=True)
                return None

    @classmethod
    async def delete(cls, model_id: int):
        async with get_async_session() as session:
            query = delete(cls.model).where(cls.model.id == model_id)
            try:
                await session.execute(query)
                await session.commit()

            except SQLAlchemyError as e:
                extra = {"model_id": model_id}
                logger.error(e, extra=extra, exc_info=True)
                return None

    @classmethod
    async def update(cls, model_id: int, **data):
        async with get_async_session() as session:
            query = update(cls.model).where(cls.model.id == model_id).values(**data).returning(cls.model)
            try:
                result = await session.execute(query)
                await session.commit()
                return result.scalar_one()
            
            except SQLAlchemyError as e:
                extra = {"model_id": model_id, "data": data}
                logger.error(e, extra=extra, exc_info=True)
                return None

