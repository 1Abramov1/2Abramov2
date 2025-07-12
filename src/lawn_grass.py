from src.product import Product


class LawnGrass(Product):

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        country: str,
        germination_period: str,
        color: str,
    ):
        super().__init__(name, description, price, quantity)
        """Добавлены методы из родительского класса и новые согласно ТЗ."""
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __repr__(self) -> str:
        return (
            f"Product('{self.name}', {self.price} руб., {self.quantity} шт., {self.country} "
            f"Страна., {self.germination_period} Период прорастания., {self.color} Цвет)"
        )

    def __add__(self, other: "LawnGrass") -> int:
        if not isinstance(other, LawnGrass):
            raise TypeError("Можно складывать только объекты LawnGrass")
        return self.quantity + other.quantity
