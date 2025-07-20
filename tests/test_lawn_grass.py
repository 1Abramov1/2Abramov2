from src.lawn_grass import LawnGrass
from src.product import Product


def test_lawn_grass_init() -> None:
    """Тестирование инициализации объекта LawnGrass."""
    lg = LawnGrass("Газонная трава", "Зеленая трава для газона", 1000, 50, "Россия", "14 дней", "зеленый")

    assert lg.name == "Газонная трава"
    assert lg.description == "Зеленая трава для газона"
    assert lg.price == 1000
    assert lg.quantity == 50
    assert lg.country == "Россия"
    assert lg.germination_period == "14 дней"
    assert lg.color == "зеленый"


def test_lawn_grass_repr() -> None:
    """Тестирование метода __repr__."""
    lg = LawnGrass("Газонная трава", "Зеленая трава для газона", 1000, 50, "Россия", "14 дней", "зеленый")
    expected_repr = (
        "Product('Газонная трава', 1000 руб., 50 шт., Россия " "Страна., 14 дней Период прорастания., зеленый Цвет)"
    )

    assert repr(lg) == expected_repr


def test_lawn_grass_add_success() -> None:
    """Тестирование сложения двух объектов LawnGrass."""
    lg1 = LawnGrass("Газонная трава", "Зеленая трава", 1000, 50, "Россия", "14 дней", "зеленый")
    lg2 = LawnGrass("Газонная трава", "Зеленая трава", 1000, 30, "Россия", "14 дней", "зеленый")

    assert lg1 + lg2 == 80


def test_lawn_grass_inheritance() -> None:
    """Тестирование, что LawnGrass является подклассом Product."""
    assert issubclass(LawnGrass, Product)
