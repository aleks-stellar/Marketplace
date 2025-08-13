from unittest.mock import patch

import pytest
from pytest import CaptureFixture

from src.product import Product


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
