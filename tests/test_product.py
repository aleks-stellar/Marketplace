from unittest.mock import patch

import pytest
from pytest import CaptureFixture

from src.product import LawnGrass, Product, Smartphone


def test_product_init(prod_1: Product) -> None:
    assert prod_1.name == "Samsung Galaxy S23 Ultra"
    assert prod_1.description == "256GB, Серый цвет, 200MP камера"
    assert prod_1.price == 180000.0
    assert prod_1.quantity == 5
    assert repr(prod_1) == (
                    f''
                    f"Product('Samsung Galaxy S23 Ultra', '256GB, Серый цвет, 200MP камера', "
                    f"{float(180000.0)}, {int(5)})"
    )


def test_product_price_get(prod_1: Product) -> None:
    assert prod_1.price == 180000.0
    prod_1.price = 200000.0
    assert prod_1.price == 200000.0


def test_product_price_zero(prod_1: Product) -> None:
    with patch("builtins.input", return_value="y"):
        assert input("...") == "y"
        prod_1.price = 1000
        assert prod_1.price == 1000
    with patch("builtins.input", return_value="..."):
        assert input("...") == "..."
        prod_1.price = 100
        # Цена у prod1 поменялась на 0 в прошлом assert
        assert prod_1.price == 1000


def test_product_price_zero_no_agreement(
        prod_1: Product,
        capsys: CaptureFixture
) -> None:
    with patch("builtins.input", return_value="..."):
        assert input("...") == "..."
        prod_1.price = 0
        assert prod_1.price == 180000.0


def test_product_price_neg(
        prod_1: Product,
        monkeypatch: pytest.MonkeyPatch,
        capsys: CaptureFixture
) -> None:
    monkeypatch.setattr("builtins.input", lambda _: "y")
    assert input("") == "y"
    prod_1.price = -10
    assert prod_1.price == 180000.0
    captured = capsys.readouterr()
    assert captured.out == "Цена не должна быть нулевая или отрицательная\n"


def test_product_price_neg_no_agreement(
        prod_1: Product,
        monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.setattr("builtins.input", lambda _: "-")
    assert input("") == "-"
    prod_1.price = -10
    assert prod_1.price == 180000.0


def test_product_new_product(prod_1: Product) -> None:
    params = {
        "name": "prod_name",
        "description": "prod_description",
        "price": 1000,
        "quantity": 10
    }

    new_prod = prod_1.new_product(product_params=params)
    assert new_prod.name == "prod_name"
    assert new_prod.quantity == 10


def test_product_new_product_same_name(prod_1: Product) -> None:
    params = {
        "name": "Samsung Galaxy S23 Ultra",
        "description": "prod_description",
        "price": 200000.0,
        "quantity": 10
    }

    new_prod = prod_1.new_product(product_params=params)
    assert new_prod.name == "Samsung Galaxy S23 Ultra"
    assert new_prod.quantity == 15
    assert new_prod.price == 200000.0


def test_product_string_representation(prod_1: Product) -> None:
    assert str(prod_1) == "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт."


def test_add_products(prod_2: Product, prod_3: Product) -> None:
    result = prod_2 + prod_3
    assert result == 2541000.0
    with pytest.raises(TypeError):
        prod_2 + 100.0


def test_smartphone_init() -> None:
    phone = Smartphone(
        "Samsung Galaxy S23 Ultra",
        "256GB, Серый цвет, 200MP камера",
        180000.0,
        5,
        95.5,
        "S23 Ultra",
        256,
        "Серый"
    )
    assert phone.name == "Samsung Galaxy S23 Ultra"
    assert phone.description == "256GB, Серый цвет, 200MP камера"
    assert phone.price == 180000.0
    assert phone.quantity == 5
    assert phone.efficiency == 95.5
    assert phone.model == "S23 Ultra"
    assert phone.memory == 256
    assert phone.color == "Серый"


def test_lawngrass_init() -> None:
    grass = LawnGrass(
        "Газонная трава",
        "Элитная трава для газона",
        500.0,
        20,
        "Россия",
        "7 дней",
        "Зеленый"
    )
    assert grass.name == "Газонная трава"
    assert grass.description == "Элитная трава для газона"
    assert grass.price == 500.0
    assert grass.quantity == 20
    assert grass.country == "Россия"
    assert grass.germination_period == "7 дней"
    assert grass.color == "Зеленый"


def test_create_invalid_product() -> None:
    """Тестирует создание продукта в количестве ноль ед."""
    with pytest.raises(ValueError):
        invalid_product = Product("prod", "invalid product", 100, 0)
        print(invalid_product)
