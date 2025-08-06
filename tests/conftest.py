import pytest

from src.product import Product
from src.category import Category


@pytest.fixture
def prod_1() -> Product:
    return Product(
        "Samsung Galaxy S23 Ultra",
        "256GB, Серый цвет, 200MP камера",
        180000.0,
        5
    )


@pytest.fixture
def prod_2() -> Product:
    return Product(
        "Iphone 15",
        "512GB, Gray space",
        210000.0,
        8
    )


@pytest.fixture
def prod_3() -> Product:
    return Product(
        "55\" QLED 4K",
        "Фоновая подсветка",
        123000.0,
        7
    )


@pytest.fixture
def cat_1(prod_1: Product, prod_2: Product) -> Category:
    return Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, "
        "но и получения дополнительных функций для удобства жизни",
        [prod_1, prod_2]
    )


@pytest.fixture
def cat_2(prod_3: Product) -> Category:
    return Category(
        "Телевизоры",
        "Современный телевизор, который позволяет наслаждаться просмотром, "
        "станет вашим другом и помощником",
        [prod_3]
    )
