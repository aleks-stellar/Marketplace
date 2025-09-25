from typing import Any, Dict, List, Self, Union

from src.base_product import BaseProduct
from src.print_mixin import PrintMixin


class Product(BaseProduct, PrintMixin):
    __products_list: List[Self] = []

    name: str
    description: str
    __price: float
    quantity: int

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
    ) -> None:
        self.name = name
        self.description = description
        self.__price = price
        if quantity == 0:
            raise ValueError("Товар с нулевым количеством не может быть добавлен")
        self.quantity = quantity
        self.__class__.__products_list.append(self)
        super().__init__()

    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, new_price: float) -> None:
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        elif new_price < self.__price:
            agreement = str(input('Если согласны на понижение цены, введите "y": '))
            if agreement == "y":
                self.__price = new_price
        else:
            self.__price = new_price

    @classmethod
    def new_product(cls, product_params: Dict) -> Union[Self, Any]:
        name = product_params["name"]
        description = product_params["description"]
        price = product_params["price"]
        quantity = product_params["quantity"]

        for product in cls.__products_list:
            if product.name == name:
                product.quantity += quantity
                if product.__price < price:
                    product.__price = price
                return product

        return cls(name, description, price, quantity)

    def __add__(self, other: Self) -> float:
        if type(other) is type(self):
            summ = self.quantity * self.__price + other.quantity * other.__price
            return float(summ)
        else:
            raise TypeError("Слагаемые должны принадлежать одному подклассу класса Product.")

    def __str__(self) -> str:
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __repr__(self) -> str:
        return (
            f"Product("
            f"'{self.name}', '{self.description}', {self.__price}, {self.quantity}"
            f")"
        )


class Smartphone(Product):
    """Дочерний класс для категории продуктов - смартфоны."""

    efficiency: float
    model: str
    memory: int
    color: str

    def __init__(
            self,
            name: str,
            description: str,
            price: float,
            quantity: int,
            efficiency: float,
            model: str,
            memory: int,
            color: str
    ) -> None:
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product):
    """Дочерний класс для категории продуктов - трава газонная."""

    country: str
    germination_period: str
    color: str

    def __init__(
            self,
            name: str,
            description: str,
            price: float,
            quantity: int,
            country: str,
            germination_period: str,
            color: str
    ) -> None:
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color
