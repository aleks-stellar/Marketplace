from typing import Dict, Type, TypeVar

T = TypeVar("T", bound="Product")


class Product:
    """Класс для создания продукта."""

    name: str
    description: str
    price: float
    quantity: int

    def __init__(
            self,
            name: str,
            description: str,
            price: float,
            quantity: int
    ) -> None:
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls: Type[T], product_params: Dict) -> T:
        product_obj = cls(
            product_params["name"],
            product_params["description"],
            product_params["price"],
            product_params["quantity"]
        )
        return product_obj

    def __repr__(self) -> str:
        return f"Product({
            self.name,
            self.description,
            self.price,
            self.quantity
        })"
