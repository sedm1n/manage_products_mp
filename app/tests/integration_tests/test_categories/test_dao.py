import pytest

from app.services.dao.category import CategoryDao

@pytest.mark.parametrize("name, slug, parent_id, is_active, expected_result", 
                         [
                             ("category_test1", "category_test1", None, True, True),
                             ("category_test2", "category_test2", 1, True, True),
                             ("category_test3", "category_test3", 1, False, True),
                             ("category_test4", "category_test4", 150, True, False),
                             ])
async def test_add_and_get_category(name: str, slug: str, parent_id: int, is_active: bool, expected_result: bool):
    
    if expected_result:

        new_category = await CategoryDao.add(
            name=name, parent_id=parent_id, slug=slug, is_active=is_active
            )

        assert new_category is not None
        assert new_category.name == name
        assert new_category.slug == slug
        assert new_category.parent_id == parent_id
        assert new_category.is_active == is_active

        get_category = await CategoryDao.find_by_id(new_category.id)

        assert get_category is not None
        assert get_category.name == name
        assert get_category.slug == slug
        assert get_category.parent_id == parent_id
        assert get_category.is_active == is_active

    else:
        new_category = await CategoryDao.add(
            name=name, parent_id=parent_id, slug=slug, is_active=is_active
            )

        assert new_category is None

    