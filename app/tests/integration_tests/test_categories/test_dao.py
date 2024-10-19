import pytest

from app.services.dao.category import CategoryDao


async def test_add_and_get_category():
    new_category = await CategoryDao.add(
        name="category_test1", parent_id=None, slug="category_test1", is_active=True
    )

    assert new_category