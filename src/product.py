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

    def __repr__(self) -> str:
        return f"Product({
            self.name,
            self.description,
            self.price,
            self.quantity
        })"
