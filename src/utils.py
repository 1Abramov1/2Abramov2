import json


class Product:
    def __init__(self, name: str, description: str, price: float, quantity: int):
        """Инициализация продукта. Все параметры обязательны."""
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    def __repr__(self) -> str:
        return f"Product('{self.name}', {self.price} руб., {self.quantity} шт.)"


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


def load_data_from_json(file_path: str) -> list[Category]:
    """Загружает данные из JSON и создает объекты Category и Product."""
    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)

    categories = []
    for category_data in data:
        products = []
        for product_data in category_data["products"]:
            product = Product(
                name=product_data["name"],
                description=product_data["description"],
                price=product_data["price"],
                quantity=product_data["quantity"],
            )
            products.append(product)

        category = Category(name=category_data["name"], description=category_data["description"], products=products)
        categories.append(category)

    return categories
