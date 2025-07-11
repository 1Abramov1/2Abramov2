from typing import Any
from typing import List
from typing import Type
from typing import TypeVar

T = TypeVar("T", bound="Product")  # Предполагается, что это метод класса Product


class Product:
    def __init__(self, name: str, description: str, price: float, quantity: int):
        """Инициализация продукта. Все параметры обязательны."""
        self.name = name
        self.description = description
        self.__price = price  # Приватный атрибут цены
        self.quantity = quantity

    def __repr__(self) -> str:
        return f"Product('{self.name}', {self.__price} руб., {self.quantity} шт.)"

    def __str__(self) -> str:
        return f"{self.name}, {int(self.price)} руб. Остаток: {self.quantity} шт."

    def __add__(self, other: 'Product') -> float:

        """Перегрузка оператора сложения для вычисления общей стоимости товаров."""

        if not isinstance(other, Product):
            raise TypeError("Можно складывать только объекты класса Product")

        return self.price * self.quantity + other.price * other.quantity

    @property
    def price(self) -> float:
        """Геттер для цены"""
        return self.__price

    @price.setter
    def price(self, new_price: float) -> None:
        """Сеттер для цены с проверками"""
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return

        # Дополнительная проверка для понижения цены
        if new_price < self.__price:
            answer = input(f"Вы уверены, что хотите понизить цену с {self.__price} до {new_price}? (y/n): ")
            if answer.lower() != "y":
                print("Изменение цены отменено")
                return

        self.__price = new_price

    @classmethod
    def new_product(cls: Type[T], products: List[T], **kwargs: Any) -> T:
        """Создает новый продукт или обновляет существующий с тем же именем."""
        for product in products:
            if isinstance(product, cls) and product.name == kwargs["name"]:
                product.quantity += kwargs["quantity"]
                if kwargs["price"] > product.price:  # Обновляем цену только если новая выше
                    product.price = kwargs["price"]
                return product
        return cls(**kwargs)
