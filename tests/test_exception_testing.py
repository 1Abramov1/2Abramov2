import unittest
from src.product import Product


class TestProductQuantityValidation(unittest.TestCase):
    def test_zero_quantity_raises_value_error(self) -> None:
        """Тест, что при quantity=0 выбрасывается ValueError"""
        with self.assertRaises(ValueError) as context:
            Product("Тестовый товар", "Описание", 100.0, 0)

        # Проверяем текст сообщения об ошибке
        self.assertEqual(str(context.exception), "Товар с нулевым количеством не может быть добавлен")

    def test_positive_quantity_works(self) -> None:
        """Тест, что при quantity>0 товар создается нормально"""
        product = Product("Тестовый товар", "Описание", 100.0, 1)
        self.assertEqual(product.quantity, 1)

    def test_negative_quantity_raises_value_error(self) -> None:
        """Тест, что при quantity<0 выбрасывается ValueError"""
        with self.assertRaises(ValueError) as context:
            Product("Тестовый товар", "Описание", 100.0, -1)

        # Проверяем текст сообщения об ошибке
        self.assertEqual(str(context.exception), "Количество товара должно быть положительным числом")


if __name__ == "__main__":
    unittest.main()
