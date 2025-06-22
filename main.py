from src.utils import load_data_from_json, Category, Product


if __name__ == "__main__":
    categories = load_data_from_json('./data/products.json')

    # Пример использования new_product
    existing_products = []  # Сначала тебе понадобится список текущих продуктов
    for category in categories:
        for product in category.products:
            existing_products.append(product)  # Заполняем список существующими продуктами


    # Добавляем или обновляем продукт
    new_product_data = {
        "name": "New Product",
        "description": "Описание продукта",
        "price": 120.0,
        "quantity": 10
    }
    new_product = Product.new_product(existing_products, **new_product_data)
    # Найди нужную категорию и обнови список продуктов
    for category in categories:
        if new_product in category.products:
            # Убедись, что продукт обновлен в категории
            for i, product in enumerate(category.products):
                if product.name == new_product.name:
                    category.products[i] = new_product
            break

    # Выводим информацию
    print(f"Всего категорий: {Category.total_categories}")
    print(f"Всего уникальных товаров: {Category.total_products}\n")

    for category in categories:
        print(f"Категория: {category.name}")
        print(f"Описание: {category.description}")
        print(f"Товары ({len(category.products)}):")
        for product in category.products:
            print(f"  - {product}")
        print()

    total_unique_products = sum(category.count_unique_products() for category in categories)
    print(f"Всего уникальных товаров: {total_unique_products}")