from src.utils import load_data_from_json, Category, Product

if __name__ == "__main__":
    # Загружаем категории и товары из JSON
    categories = load_data_from_json('./data/products.json')

    # 1. Преобразуем строковые товары в объекты Product
    for category in categories:
        new_products = [
            product if isinstance(product, Product)
            else Product(
                name=product,  # сама строка становится названием
                description="Описание отсутствует",
                price=0.0,
                quantity=0
            )
            for product in category.products
        ]
        category.products = new_products

    # 2. Собираем все существующие товары в один список
    existing_products = []
    for category in categories:
        existing_products.extend(category.products)

    # 3. Данные для нового/обновляемого товара
    new_product_data = {
        "name": "New Product",
        "description": "Описание продукта",
        "price": 120.0,
        "quantity": 10
    }

    # 4. Создаём или обновляем товар
    new_product = Product.new_product(existing_products, **new_product_data)

    # 5. Обновляем товары в категориях
    for category in categories:
        for i, product in enumerate(category.products):
            if isinstance(product, Product) and product.name == new_product.name:
                category.products[i] = new_product
                break

    # 6. Выводим информацию с использованием строкового представления
    print("\n=== ОБЩАЯ ИНФОРМАЦИЯ ===")
    print(f"Всего категорий: {Category.total_categories}")
    print(f"Всего уникальных товаров: {Category.total_products}\n")

    print("\n=== КАТЕГОРИИ И ТОВАРЫ ===")
    for category in categories:
        # Используем строковое представление категории
        print(f"\n{category}")
        print(f"Описание: {category.description}")
        print("Список товаров:")
        for product in category.products:
            # Используем строковое представление продукта
            print(f"  • {product}")

    # 7. Подсчёт уникальных товаров (альтернативный способ)
    total_unique_products = sum(category.count_unique_products() for category in categories)
    print(f"\n=== ИТОГИ ===")
    print(f"Всего уникальных товаров (проверка): {total_unique_products}")
