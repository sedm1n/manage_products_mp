
import pytest
from services.dao.user import UserDao


@pytest.mark.parametrize(
    "user_id, expected_result",
    [
        (1, True),
        (3212, False),
    ],
)
async def test_find_user_by_id(user_id: int, expected_result: bool):
    user = await UserDao.find_by_id(user_id)
    if expected_result:
        assert user
        assert user.id == user_id
    else:
        assert user is None


@pytest.mark.parametrize(
    "username, password, email, expected_result",
    [
        ("test_create_user1", "test1", "email1@ya.ru", True),
        ("test_create_user2", "test2", "email2@ya.ru", True),
        ("test_create_user4", "test4", "email4@ya.ru", True),
        ("test_create_user2", "test3", "email2@ya.ru", False),
        ("test_create_user3", "test4", "email2@ya.ru", False),
        ("test_create_user3", "", "email2@ya.ru", False),
        ("", "", "email2@ya.ru", False),
        ("", "", "", False),
    ],
)
async def test_create_user(
    username: str, password: str, email: str, expected_result: bool
):
    new_user = await UserDao.add(
        username=username, hashed_password=password, email=email
    )

    if expected_result:
        assert new_user is not None

    else:
        assert new_user is None


@pytest.mark.parametrize(
    "username, expected_result",
    [
        ("test_create_user1", True),
        ("test_create_user2", True),
        ("test_create_user2", False),
        (1234, False),
        ("цукцукцукцукцук", False),
        ("", False),
    ],
)
async def test_delete_user(username: str, expected_result: bool):
    user = await UserDao.find_one_or_none(username=username)

    if expected_result:
        assert user is not None
        assert user.username == username
        await UserDao.delete(user.id)
        user = await UserDao.find_one_or_none(username=username)
        assert user is None
    else:
        assert user is None


@pytest.mark.parametrize(
    "username, password, email, new_username, new_password, new_email, expected_result",
    [
        (
            "jane_smith","test41",
            "john.doe@example.com","test_create_user2",
            "test2","email2@ya.ru",True,
        ),
        (
            "test_create_user4","test41",
            "email4@ya.ru","test_create_user2",
            "test2","email2@ya.ru",False,
        ),

    ],
)
async def test_update_user(
    username: str,
    password: str,
    email: str,
    new_username,
    new_password,
    new_email, expected_result: bool,
):
    user = await UserDao.find_one_or_none(username=username)
    assert user is not None

    updated_user = await UserDao.update(user.id, username=new_username, hashed_password=new_password, email=new_email)

    if expected_result:
        assert updated_user is not None
        assert updated_user.username == new_username
        assert updated_user.email == new_email
        assert updated_user.hashed_password == new_password

        user = await UserDao.find_one_or_none(username=new_username)

        assert user is not None
        assert user.username == new_username

    else:
        assert updated_user is None
