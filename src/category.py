from typing import List

from src.product import Product


class Category:
    """Класс создания категории товара."""

    category_count = 0
    product_count = 0

    name: str
    description: str
    __products: List[Product]

    def __init__(
            self,
            name: str,
            description: str,
            products: List[Product]
    ) -> None:
        self.name = name
        self.description = description
        self.__products = products

        Category.category_count += 1
        Category.product_count += len(self.__products)

    def add_product(self, new_product: Product) -> None:
        self.__products.append(new_product)
        Category.product_count += 1

    @property
    def products(self) -> str:
        products_list = []
        for product in self.__products:
            products_list.append(f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.")
        result = "\n".join(products_list)
        return result
