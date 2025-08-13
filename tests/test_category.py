from src.category import Category
from src.product import Product


def test_category_init(cat_1: Category, cat_2: Category) -> None:
    assert cat_1.name == "Смартфоны"
    assert cat_1.description == (
                            "Смартфоны, как средство не только коммуникации, "
                            "но и получения дополнительных функций для удобства жизни"
    )
    assert cat_2.product_count == 3
    assert cat_1.category_count == 2


def test_category_add_product(cat_1: Category, prod_3: Product) -> None:
    cat_1.add_product(prod_3)
    result = cat_1.products.split("\n")
    assert result == [
        'Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.',
        'Iphone 15, 210000.0 руб. Остаток: 8 шт.',
        '55\" QLED 4K, 123000.0 руб. Остаток: 7 шт.'
    ]


def test_category_string_representation(cat_1: Category) -> None:
    assert str(cat_1) == "Смартфоны, количество продуктов: 13 шт."
