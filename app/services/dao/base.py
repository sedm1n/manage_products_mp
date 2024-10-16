from sqlalchemy import select, insert
from app.dependencies.db import async_session

class BaseDao:
      model = None

      @classmethod
      async def find_by_id(cls, model_id:int):
            async with async_session() as session:
                  query = select(cls.model).filter_by(model_id=id)
                  result = await session.execute(query)
                  
                  return result.scalar_one_or_none()

      @classmethod
      async def find_one_or_none(cls, **filter_by):
            async with async_session() as session:
                  query = select(cls.model).filter_by(**filter_by)
                  result = await session.execute(query)
                  
                  return result.scalar_one_or_none()
            
      @classmethod
      async def get_all(cls, **filter_by):
            async with async_session() as session:
                  query = select(cls.model).filter_by(**filter_by)
                  result = await session.execute(query)
                  
                  return result.mappings().all()
          
      @classmethod
      async def add(cls, **data):
            async with async_session() as session:
                  query = insert(cls.model).values(**data)      
                  await session.execute(query)
                  await session.commit()
                  # return user id
                  