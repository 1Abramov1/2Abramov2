from src.product import Product

class Category:
    # Атрибуты класса (общие для всех объектов)
    total_categories = 0  # Общее количество категорий
    total_products = 0  # Общее количество уникальных товаров

    def __init__(self, name: str, description: str, products: list[Product]):
        """Инициализация категории. Все параметры обязательны."""
        self.name = name
        self.description = description
        self.products = products

        # Обновляем атрибуты класса
        Category.total_categories += 1
        Category.total_products += len(products)

    def __repr__(self) -> str:
        return f"Category('{self.name}', товаров: {len(self.products)})"