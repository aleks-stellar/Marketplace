from typing import Dict, List, Type


class Product:
    __products_list: List["Product"] = []

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
        self.quantity = quantity
        self.__class__.__products_list.append(self)

    @property
    def price(self) -> float:
        if self.__price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return self.__price
        else:
            return self.__price

    @price.setter
    def price(self, new_price: float) -> None:
        self.__price = new_price

    @classmethod
    def new_product(cls: Type["Product"], product_params: Dict) -> "Product":
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

    def __repr__(self) -> str:
        return (
            f"Product("
            f"'{self.name}', '{self.description}', {self.__price}, {self.quantity}"
            f")"
        )
