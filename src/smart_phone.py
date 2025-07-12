from src.product import Product


class Smartphone(Product):
    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        efficiency: str,
        model: str,
        memory: int,
        color: str,
    ) -> None:
        super().__init__(name, description, price, quantity)
        """Добавлены методы из родительского класса и новые согласно ТЗ."""

        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __repr__(self) -> str:
        return (
            f"Smartphone('{self.name}', '{self.description}', {self.price}, {self.quantity}, "
            f"'{self.efficiency}', '{self.model}', {self.memory}, '{self.color}')"
        )

    def __add__(self, other: "Smartphone") -> int:
        if not isinstance(other, Smartphone):
            raise TypeError("Можно складывать только объекты Smartphone")
        return self.quantity + other.quantity
