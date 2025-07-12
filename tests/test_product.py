import logging
import unittest
from io import StringIO  # для перехвата вывода в консоль
from typing import Any
from unittest.mock import patch

from src.product import MixinLog
from src.product import Product


# Создаем класс для тестирования функционала, связанного с ценой продукта
class TestProductPrice(unittest.TestCase):
    def setUp(self) -> None:
        """Метод setUp выполняется перед каждым тестом.
        Здесь создаем тестовый продукт с начальными параметрами:
        название, описание, цена=100.0, количество=10"""
        self.product = Product("Тестовый товар", "Описание", 100.0, 10)

    def test_price_getter(self) -> None:
        """Тест проверяет корректность работы геттера для цены.
        Убеждаемся, что возвращается правильное значение цены."""
        self.assertEqual(self.product.price, 100.0)

    def test_price_setter_valid(self) -> None:
        """Тест проверяет установку корректного значения цены.
        Устанавливаем новую цену 150.0 и проверяем, что она сохранилась."""
        self.product.price = 150.0
        self.assertEqual(self.product.price, 150.0)

    def test_price_setter_invalid_negative(self) -> None:
        """Тест проверяет обработку попытки установить отрицательную цену.
        Используем patch для перехвата вывода в консоль.
        Цена не должна измениться, в консоли должно быть сообщение об ошибке."""
        with patch("sys.stdout", new=StringIO()) as fake_out:
            self.product.price = -50.0
            self.assertEqual(self.product.price, 100.0)  # Проверяем, что цена не изменилась
            self.assertIn("Цена не должна быть нулевая или отрицательная", fake_out.getvalue())

    def test_price_setter_invalid_zero(self) -> None:
        """Тест аналогичен предыдущему, но для нулевой цены.
        Проверяем, что система отвергает нулевую цену."""
        with patch("sys.stdout", new=StringIO()) as fake_out:
            self.product.price = 0.0
            self.assertEqual(self.product.price, 100.0)  # Цена не должна измениться
            self.assertIn("Цена не должна быть нулевая или отрицательная", fake_out.getvalue())

    @patch("builtins.input", return_value="y")
    def test_price_decrease_with_confirmation(self, mock_input: Any) -> None:
        """Тест проверяет понижение цены с подтверждением пользователя.
        Используем декоратор patch для имитации ввода 'y' (yes).
        Цена должна успешно измениться на 80.0."""
        self.product.price = 80.0
        self.assertEqual(self.product.price, 80.0)

    @patch("builtins.input", return_value="n")
    def test_price_decrease_with_rejection(self, mock_input: Any) -> None:
        """Тест проверяет понижение цены, когда пользователь отказывается (вводит 'n').
        Используем patch для перехвата вывода в консоль.
        Цена не должна измениться, в консоли должно быть сообщение об отмене."""
        with patch("sys.stdout", new=StringIO()) as fake_out:
            self.product.price = 80.0
            self.assertEqual(self.product.price, 100.0)  # Цена не должна измениться
            self.assertIn("Изменение цены отменено", fake_out.getvalue())

    def test_price_increase_no_confirmation_needed(self) -> None:
        """Тест проверяет повышение цены без необходимости подтверждения.
        В этом случае цена должна меняться сразу без дополнительных вопросов."""
        self.product.price = 120.0
        self.assertEqual(self.product.price, 120.0)

    def test_add_two_products(self) -> None:
        """Тест сложения двух товаров."""
        product1 = Product("Тестовый товар1", "серый", 10000, 2)  # цена 10000, количество 2
        product2 = Product("Тестовый товар2", "желтый", 30000, 3)  # цена 30, количество 3
        total = product1.add(product2)
        self.assertEqual(total, 10000 * 2 + 30000 * 3)

    def test_add_with_different_types_prices(self) -> None:
        """Тест сложения товаров с разными типами цен (int и float)."""
        product1 = Product("Тестовый товар1", "черный", 30.5, 2)  # цена float
        product2 = Product("Тестовый товар2", "желтый", 10, 3)  # цена int
        total = product1.add(product2)
        self.assertAlmostEqual(total, 30.5 * 2 + 10 * 3)


class TestMixinLogAndBaseProduct(unittest.TestCase):
    def setUp(self) -> None:
        # Перенаправляем вывод логов в StringIO для проверки
        self.log_stream = StringIO()
        handler = logging.StreamHandler(self.log_stream)
        logging.basicConfig(level=logging.INFO, handlers=[handler])

        # Сбросим множество созданных классов перед каждым тестом
        MixinLog._created_objects = set()

    def test_mixin_log_creation(self) -> None:
        """Тестируем логирование создания объекта"""
        with self.assertLogs("root", level="INFO") as cm:
            Product("Тестовый продукт", "Описание", 100.0, 10)

        # Проверяем наличие сообщения в output логов
        self.assertTrue(any("Создан объект класса Product" in message for message in cm.output))

    def test_base_product_abstract_method(self) -> None:
        """Тестируем, что Product реализует абстрактный метод get_info"""
        product = Product("Тестовый продукт", "Описание", 100.0, 10)
        self.assertEqual(product.get_info(), "Тестовый продукт, цена: 100.0 руб.")

    def test_product_creation(self) -> None:
        """Тестируем корректность создания продукта"""
        product = Product("Ноутбук", "Мощный ноутбук", 50000.0, 5)

        self.assertEqual(product.name, "Ноутбук")
        self.assertEqual(product.description, "Мощный ноутбук")
        self.assertEqual(product.price, 50000.0)
        self.assertEqual(product.quantity, 5)

    def test_price_setter_validation(self) -> None:
        """Тестируем валидацию цены"""
        product = Product("Телефон", "Смартфон", 30000.0, 3)

        # Попытка установить отрицательную цену
        with patch("builtins.print") as mocked_print:
            product.price = -1000
            mocked_print.assert_called_with("Цена не должна быть нулевая или отрицательная")
            self.assertEqual(product.price, 30000.0)

        # Попытка понизить цену (имитируем отказ пользователя)
        with patch("builtins.input", return_value="n"):
            with patch("builtins.print") as mocked_print:
                product.price = 20000.0
                mocked_print.assert_called_with("Изменение цены отменено")
                self.assertEqual(product.price, 30000.0)

        # Успешное повышение цены
        product.price = 35000.0
        self.assertEqual(product.price, 35000.0)

    def test_add_method(self) -> None:
        """Тестируем метод сложения продуктов"""
        product1 = Product("Планшет", "Графический планшет", 20000.0, 2)
        product2 = Product("Мышь", "Беспроводная мышь", 1500.0, 3)

        # Проверяем корректное сложение
        total = product1.add(product2)
        self.assertEqual(total, 20000.0 * 2 + 1500.0 * 3)


if __name__ == "__main__":
    unittest.main()
