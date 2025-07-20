from typing import Any

import pytest
import unittest

from src.category import Category
from src.product import Product


@pytest.fixture
def sample_product() -> Product:
    return Product("Телевизор", "4K OLED", 100000.0, 10)


@pytest.fixture
def empty_category() -> Category:
    return Category("Пустая категория", "Без товаров", [])


@pytest.fixture
def category_with_products(sample_product: Product) -> Category:
    return Category("Электроника", "Техника", [sample_product])


def test_add_product_to_empty_category(empty_category: Category, sample_product: Product) -> None:
    """Тестирует добавление продукта в пустую категорию."""
    # Проверяем начальное состояние
    assert len(empty_category.products) == 0
    assert Category.total_products == 0

    # Добавляем продукт
    empty_category.add_product(sample_product)

    # Проверяем результаты
    assert len(empty_category.products) == 1
    assert empty_category.products[0] == sample_product
    assert Category.total_products == 1


def test_add_product_to_non_empty_category(category_with_products: Category, sample_product: Product) -> None:
    """Тестирует добавление продукта в непустую категорию."""
    initial_count = len(category_with_products.products)
    initial_total = Category.total_products

    # Создаем и добавляем новый продукт
    new_product = Product("Ноутбук", "Игровой", 150000.0, 5)
    category_with_products.add_product(new_product)

    # Проверяем результаты
    assert len(category_with_products.products) == initial_count + 1
    assert category_with_products.products[-1] == new_product
    assert Category.total_products == initial_total + 1


def test_products_property_getter(category_with_products: Category, sample_product: Product) -> None:
    """Тестирует геттер products на возврат оригинального списка (без копии)."""
    products1 = category_with_products.products
    products2 = category_with_products.products

    assert products1 == products2  # Содержимое одинаковое
    assert products1 is products2  # Это один и тот же объект (не копия)
    assert isinstance(products1, list)
    assert products1[0] == sample_product


def test_products_property_returns_original(category_with_products: Category) -> None:
    """Тестирует, что property возвращает оригинальный список продуктов (не копию)."""
    # Получаем список продуктов через property
    products_reference = category_with_products.products
    original_products = category_with_products.products  # Получаем доступ к оригиналу

    # Проверяем, что это один и тот же объект
    assert products_reference is original_products, "Геттер должен возвращать оригинальный список"

    # Создаем тестовый продукт
    test_product = Product(name="Тестовый продукт", description="Тестовое описание", price=100.0, quantity=1)

    # Запоминаем исходную длину
    original_length = len(original_products)

    # Изменяем полученный список
    products_reference.append(test_product)

    # Проверяем, что оригинальный список ИЗМЕНИЛСЯ
    assert len(original_products) == original_length + 1, "Оригинальный список должен изменяться"
    assert test_product in original_products, "Тестовый продукт должен появиться в оригинальном списке"


@pytest.mark.parametrize(
    "invalid_value",
    [
        "не продукт",  # str
        123,  # int
        {},  # dict
        None,  # None
        ["список", "продуктов"],  # list
    ],
)
def test_add_product_invalid_type(empty_category: Category, invalid_value: Any) -> None:
    """Тестирует обработку невалидных типов при добавлении продукта."""
    with pytest.raises(TypeError) as exc_info:
        empty_category.add_product(invalid_value)

    assert "только объекты класса Product" in str(exc_info.value)
    assert len(empty_category.products) == 0


class TestCategoryStr:
    """Тестирование строкового представления категории (__str__)"""

    def test_empty_category(self) -> None:
        """Категория без продуктов должна показывать 0 товаров"""
        category = Category("Пустая", "Нет товаров", [])
        assert str(category) == "Пустая, количество продуктов: 0 шт."

    def test_single_product(self) -> None:
        """Категория с одним товаром"""
        product = Product("Телефон", "Смартфон", 50000, 10)
        category = Category("Электроника", "Гаджеты", [product])
        assert str(category) == "Электроника, количество продуктов: 10 шт."

    def test_multiple_products(self) -> None:
        """Категория с несколькими товарами (суммирование quantity)"""
        products = [
            Product("Товар 1", "Описание 1", 100, 5),
            Product("Товар 2", "Описание 2", 200, 3),
            Product("Товар 3", "Описание 3", 300, 2),
        ]
        category = Category("Техника", "Разное", products)
        assert str(category) == "Техника, количество продуктов: 10 шт."  # 5 + 3 + 2


class TestAveragePrice(unittest.TestCase):
    def setUp(self) -> None:
        """Подготовка тестовых данных"""
        self.product1 = Product("Товар 1", "Описание 1", 100.0, 2)
        self.product2 = Product("Товар 2", "Описание 2", 200.0, 3)
        self.product3 = Product("Товар 3", "Описание 3", 300.0, 1)
        self.zero_price_product = Product("Бесплатный", "Образец", 0.0, 5)

    def test_average_with_multiple_products(self) -> None:
        """Тест расчета средней цены с несколькими товарами"""
        category = Category("Тест", "Категория", [self.product1, self.product2, self.product3])
        expected_avg = (100 + 200 + 300) / 3
        self.assertAlmostEqual(category.average_price(), expected_avg, places=2)

    def test_empty_category(self) -> None:
        """Тест пустой категории (должен возвращать 0)"""
        empty_category = Category("Пустая", "Категория", [])
        self.assertEqual(empty_category.average_price(), 0.0)

    def test_single_product(self) -> None:
        """Тест категории с одним товаром"""
        category = Category("Один товар", "Категория", [self.product2])
        self.assertEqual(category.average_price(), 200.0)

    def test_zero_price_product(self) -> None:
        """Тест товара с нулевой ценой"""
        category = Category("Нулевая цена", "Категория", [self.zero_price_product])
        self.assertEqual(category.average_price(), 0.0)

    def test_mixed_prices(self) -> None:
        """Тест смешанных цен (обычные и нулевые)"""
        category = Category("Смешанная", "Категория", [self.product1, self.zero_price_product])
        expected_avg = (100 + 0) / 2
        self.assertAlmostEqual(category.average_price(), expected_avg, places=2)

    def test_float_precision(self) -> None:
        """Тест точности вычислений с плавающей точкой"""
        p1 = Product("Т1", "", 10.50, 1)
        p2 = Product("Т2", "", 20.25, 1)
        p3 = Product("Т3", "", 30.75, 1)
        category = Category("Точность", "Категория", [p1, p2, p3])
        expected_avg = (10.50 + 20.25 + 30.75) / 3
        self.assertAlmostEqual(category.average_price(), expected_avg, places=2)


if __name__ == "__main__":
    unittest.main()
