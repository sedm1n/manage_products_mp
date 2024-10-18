from services.dao.user import UserDao

async def test_find_user_by_id():
      user = await UserDao.find_by_id(1)
      print(user)