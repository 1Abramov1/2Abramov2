from src.utils import load_data_from_json
from src.utils import Category

if __name__ == "__main__":
    categories = load_data_from_json('./data/products.json')

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