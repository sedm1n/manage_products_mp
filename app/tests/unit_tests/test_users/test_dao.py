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
      
