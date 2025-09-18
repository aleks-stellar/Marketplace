from pytest import CaptureFixture

from src.product import Product


def test_print_mixin(capsys: CaptureFixture) -> None:
    Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    message = capsys.readouterr()
    assert message.out.strip() == "Product('Samsung Galaxy S23 Ultra', '256GB, Серый цвет, 200MP камера', 180000.0, 5)"


def test_print_mixin_repr() -> None:
    product = Product("iPhone 15 Pro", "128GB, Titanium", 120000.0, 3)
    assert repr(product) == "Product('iPhone 15 Pro', '128GB, Titanium', 120000.0, 3)"
