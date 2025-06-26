from src.utils import load_data_from_json, Category, Product

if __name__ == "__main__":
    # Загружаем категории и товары из JSON
    categories = load_data_from_json('./data/products.json')

    # 1. Преобразуем строковые товары в объекты Product (если такие есть)
    for category in categories:
        # Создаем новый список товаров
        new_products = [
            # Если элемент уже является Product - оставляем как есть
            product if isinstance(product, Product)
            # Иначе создаём новый Product из строки (с минимальными данными)
            else Product(
                name=product,  # сама строка становится названием
                description="Описание отсутствует",
                price=0.0,
                quantity=0
            )
            for product in category.products
        ]
        # Обновляем список товаров в категории
        category.products = new_products  # Убедитесь, что в классе Category есть сеттер для products

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
            # Проверяем, что это Product и имя совпадает
            if isinstance(product, Product) and product.name == new_product.name:
                category.products[i] = new_product  # Заменяем старый товар новым
                break  # Прерываем цикл после первого совпадения

    # 6. Выводим информацию
    print(f"Всего категорий: {Category.total_categories}")
    print(f"Всего уникальных товаров: {Category.total_products}\n")

    for category in categories:
        print(f"Категория: {category.name}")
        print(f"Описание: {category.description}")
        print(f"Товары ({len(category.products)}):")
        for product in category.products:
            print(f"  - {product}")
        print()

    # 7. Подсчёт уникальных товаров (альтернативный способ)
    total_unique_products = sum(category.count_unique_products() for category in categories)
    print(f"Всего уникальных товаров: {total_unique_products}")