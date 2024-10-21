import pytest
from services.dao.product import ProductDao


@pytest.mark.parametrize(
    "product_id, expected_result",
    [
        (1, True),
        (3212, False),
    ],
)
async def test_find_product_by_id(product_id: int, expected_result: bool):
    product = await ProductDao.find_by_id(product_id)
    if expected_result:
        assert product
        assert product.id == product_id
    else:
        assert product is None


@pytest.mark.parametrize(
    "name, slug, description, price, stock, image_url,supplier_id, category_id, rating, is_active, expected_result",
    [
        (
            "test_create_product1",
            "test_create_product1",
            "test_create_product1_desc",
            99,
            10,
            "image_url",
            1,
            1,
            5.0,
            True,
            True,
        ),
    ],
)
async def test_create_product(
    name: str,
    slug: str,
    description: str,
    price: int,
    stock: int,
    image_url: str,
    supplier_id: int,
    category_id: int,
    rating: float,
    is_active: bool,
    expected_result: bool,
):
    new_product = await ProductDao.add(
        name=name,
        slug=slug,
        description=description,
        price=price,
        stock=stock,
        image_url=image_url,
        supplier_id=supplier_id,
        category_id=category_id,
        rating=rating,
        is_active=is_active,
    )

    if expected_result:
        assert new_product is not None

    else:
        assert new_product is None


@pytest.mark.parametrize(
    "name, new_name, new_slug, new_category_id,new_price,new_stock,new_image_url,new_supplier_id,new_rating,new_is_active ,expected_result",
    [
        (
            "test_create_product1",
            "new_test_create_product1",
            "new_test_create_product1",
            2,
            199,
            110,
            "new_image_url",
            2,
            4.1,
            True,
            True,
        ),
        (
            "product2",
            "new_test_create_product2",
            "new_test_create_product1",
            2,
            199,
            110,
            "new_image_url",
            2,
            4.1,
            True,
            False,
        ),
    ],
)
async def test_update_product(
    name: str,
    new_name: str,
    new_slug: str,
    new_category_id: int,
    new_price: float,
    new_stock: int,
    new_image_url: str,
    new_supplier_id: int,
    new_rating: float,
    new_is_active: bool,
    expected_result: bool,
):
    product = await ProductDao.find_one_or_none(name=name)

    if expected_result:
        updated_product = await ProductDao.update(
            product.id,
            name=new_name,
            slug=new_slug,
            category_id=new_category_id,
            price=new_price,
            stock=new_stock,
            image_url=new_image_url,
            supplier_id=new_supplier_id,
            rating=new_rating,
            is_active=new_is_active,
        )

        assert updated_product is not None
        assert updated_product.name == new_name
        assert updated_product.slug == new_slug
        assert updated_product.category_id == new_category_id
        assert updated_product.price == new_price
        assert updated_product.stock == new_stock
        assert updated_product.image_url == new_image_url
        assert updated_product.supplier_id == new_supplier_id
        assert updated_product.rating == new_rating
        assert updated_product.is_active == new_is_active
        product = await ProductDao.find_one_or_none(name=new_name)

        assert product is not None
        assert product.name == new_name

    else:
        assert product is None


@pytest.mark.parametrize(
    "name, expected_result",
    [
        ("new_test_create_product1", True),
        ("test_create_product1", False),
        (1234, False),
        ("", False),
    ],
)
async def test_delete_product(name: str, expected_result: bool):
    product = await ProductDao.find_one_or_none(name=name)

    if expected_result:
        assert product is not None
        assert product.name == name
        await ProductDao.delete(product.id)
        product = await ProductDao.find_one_or_none(name=name)
        assert product is None
    else:
        assert product is None
