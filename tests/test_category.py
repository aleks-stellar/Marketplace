from src.category import Category


def test_category_init(cat_1: Category, cat_2: Category) -> None:
    assert cat_1.name == "Смартфоны"
    assert cat_1.description == (
                            "Смартфоны, как средство не только коммуникации, "
                            "но и получения дополнительных функций для удобства жизни"
    )
    assert cat_2.product_count == 3
    assert cat_1.category_count == 2
