from src.product import Product


def test_product_init(prod_1: Product) -> None:
    assert prod_1.name == "Samsung Galaxy S23 Ultra"
    assert prod_1.description == "256GB, Серый цвет, 200MP камера"
    assert prod_1.price == 180000.0
    assert prod_1.quantity == 5
    assert str(prod_1) == (f''
                      f"Product(('Samsung Galaxy S23 Ultra', '256GB, Серый цвет, 200MP камера', "
                      f"{float(180000.0)}, {int(5)}))")
