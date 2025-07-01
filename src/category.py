from src.product import Product
from typing import List, TypeVar

# Предположим, что Product - это класс продукта
T = TypeVar('T', bound='Product')


class Category:

    def count_unique_products(self) -> int:
        """
        Возвращает количество уникальных товаров в категории.

        :return: Количество уникальных товаров.
        """
        return len(self.__products)

    # Атрибуты класса (общие для всех объектов)
    total_categories = 0  # Общее количество категорий
    total_products = 0  # Общее количество уникальных товаров

    def __init__(self, name: str, description: str, products: list[Product]):
        """Инициализация категории. Все параметры обязательны."""
        self.name = name
        self.description = description
        self.__products = products  # Приватный атрибут списка товаров

        # Обновляем атрибуты класса
        Category.total_categories += 1
        Category.total_products += len(products)

    def add_product(self, product: Product) -> None:
        """Добавляет товар в приватный список продуктов категории."""
        if not isinstance(product, Product):
            raise TypeError("Можно добавлять только объекты класса Product")
        self.__products.append(product)
        Category.total_products += 1

    # Увеличиваем счетчик товаров

    def __repr__(self) -> str:
        return f"Category('{self.name}', товаров: {len(self.__products)})"


    def __str__(self) -> str:
        total_quantity = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."


    @property
    def products(self) -> List[Product]:
        return self.__products

    @products.setter
    def products(self, value: List[Product]) -> None:
        self.__products = value

