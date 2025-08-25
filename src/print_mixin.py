class PrintMixin:

    def __init__(self) -> None:
        print(repr(self))

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}("
            f"'{self.name}', '{self.description}', {self.__price}, {self.quantity}"
            f")"
        )
