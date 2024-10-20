
import pytest
from services.dao.category import CategoryDao


@pytest.mark.parametrize(
    "category_id, expected_result",
    [
        (1, True),
        (3212, False),
    ],
)
async def test_find_category_by_id(category_id: int, expected_result: bool):
    
    category = await CategoryDao.find_by_id(category_id)
    if expected_result:
        assert category
        assert category.id == category_id
    else:
        assert category is None


@pytest.mark.parametrize(
    "name, slug, parent_id, is_active, expected_result",
    [
        ("category_test1", "category_test1", None, True, True),
        ("category_test2", "category_test2", 1, True, True),
        ("category_test3", "category_test3", 1, False, True),
        ("category_test4", "category_test4", 150, True, False),
        ("", "category_test5", None, False, False),
        ("", "",None,None, False),
        (None, None,None,None, False),
    ],
)
async def test_create_category(
    name: str, slug: str, parent_id: int, is_active: bool, expected_result: bool
):
    new_category = await CategoryDao.add(
        name=name, slug=slug, parent_id=parent_id, is_active=is_active
    )

    if expected_result:
        assert new_category is not None

    else:
        assert new_category is None


# @pytest.mark.parametrize(
#     "name, expected_result",
#     [
#         ("test_create_category1", True),
#         ("test_create_category2", True),
#         ("test_create_category2", False),
#         (1234, False),
#         ("цукцукцукцукцук", False),
#         ("", False),
#     ],
# )
# async def test_delete_category(name: str, expected_result: bool):
#     category = await categoryDao.find_one_or_none(name=name)

#     if expected_result:
#         assert category is not None
#         assert category.name == name
#         await categoryDao.delete(category.id)
#         category = await categoryDao.find_one_or_none(name=name)
#         assert category is None
#     else:
#         assert category is None


# @pytest.mark.parametrize(
#     "name, password, email, new_name, new_password, new_email, expected_result",
#     [
#         (
#             "jane_smith","test41",
#             "john.doe@example.com","test_create_category2",
#             "test2","email2@ya.ru",True,
#         ),
#         (
#             "test_create_category4","test41",
#             "email4@ya.ru","test_create_category2",
#             "test2","email2@ya.ru",False,
#         ),

#     ],
# )
# async def test_update_category(
#     name: str,
#     password: str,
#     email: str,
#     new_name,
#     new_password,
#     new_email, expected_result: bool,
# ):
#     category = await categoryDao.find_one_or_none(name=name)
#     assert category is not None

#     updated_category = await categoryDao.update(category.id, name=new_name, hashed_password=new_password, email=new_email)

#     if expected_result:
#         assert updated_category is not None
#         assert updated_category.name == new_name
#         assert updated_category.email == new_email
#         assert updated_category.hashed_password == new_password

#         category = await categoryDao.find_one_or_none(name=new_name)

#         assert category is not None
#         assert category.name == new_name

#     else:
#         assert updated_category is None
