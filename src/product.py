from typing import Dict, List, Type


class Product:
    __products_list: List["Product"] = []

    name: str
    description: str
    price: float
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
        self.price = price
        self.quantity = quantity
        self.__class__.__products_list.append(self)

    @classmethod
    def new_product(cls: Type["Product"], product_params: Dict) -> "Product":
        name = product_params["name"]
        description = product_params["description"]
        price = product_params["price"]
        quantity = product_params["quantity"]

        for product in cls.__products_list:
            if product.name == name:
                product.quantity += quantity
                if product.price < price:
                    product.price = price
                return product

        return cls(name, description, price, quantity)

    def __repr__(self) -> str:
        return (
            f"Product("
            f"'{self.name}', '{self.description}', {self.price}, {self.quantity}"
            f")"
        )
