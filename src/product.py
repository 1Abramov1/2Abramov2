class Product:
    def __init__(self, name: str, description: str, price: float, quantity: int):
        """Инициализация продукта. Все параметры обязательны."""
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    def __repr__(self) -> str:
        return f"Product('{self.name}', {self.price} руб., {self.quantity} шт.)"