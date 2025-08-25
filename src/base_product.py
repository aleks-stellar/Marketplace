from abc import ABC, abstractmethod
from typing import Dict, Self


class BaseProduct(ABC):

    @abstractmethod
    def __init__(self) -> None:
        pass

    @classmethod
    @abstractmethod
    def new_product(cls, product_params: Dict) -> Self:
        pass

    @property
    @abstractmethod
    def price(self) -> float:
        pass

    @price.setter
    @abstractmethod
    def price(self, new_price: float) -> None:
        pass

    @abstractmethod
    def __add__(self, other: Self) -> float:
        pass
