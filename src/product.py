from typing import Dict, List, Type, TypeVar

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
    def new_product(
            cls: Type[T],
            product_params: Dict,
            products_list: List[T]
    ) -> T:
        name = product_params["name"]
        description = product_params["description"]
        price = product_params["price"]
        quantity = product_params["quantity"]

        for product in products_list:
            # Если товар с тем же именем есть в списке, то обновляем цену и количество
            if product.name == name:
                product.quantity += quantity
                if product.price < price:
                    product.price = price
                return product

        new_prod = cls(name, description, price, quantity)
        products_list.append(new_prod)
        return new_prod

    def __repr__(self) -> str:
        return (f"Product("
                f"'{self.name}', '{self.description}', {self.price}, {self.quantity}"
                f")")
