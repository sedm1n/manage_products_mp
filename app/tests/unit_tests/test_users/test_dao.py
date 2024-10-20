from app.schemas.user import UserCreateSchema
import pytest
from services.dao.user import UserDao

@pytest.mark.parametrize(
      "user_id, is_present",[
            (1, True),
            (3212, False),]
)
async def test_find_user_by_id(user_id:int, is_present:bool):
      user = await UserDao.find_by_id(user_id)
      if is_present:
            assert user
            assert user.id == user_id
      else:
            assert user is None
      


@pytest.mark.parametrize(
      "username, password, email, expected_result",[
            ("test_create_user1", "test", "email1@ya.ru", True),
            ("test_create_user2", "test", "email2@ya.ru", True),
            ("test_create_user2", "test", "email2@ya.ru", False),
            ("test_create_user3", "test", "email2@ya.ru", False),
            ("test_create_user3", "", "email2@ya.ru", False),
            ("", "", "email2@ya.ru", False),
            ("", "", "", False),
            ]
)
async def test_create_user(username:str, password:str, email:str, expected_result:bool):
      new_user = await UserDao.add(
            username=username, hashed_password=password, email=email)
      if expected_result:
            assert new_user is not None
      
      else: 
            assert new_user is None