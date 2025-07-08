import pytest

from src.product import Product
from src.smart_phone import Smartphone


def test_smartphone_init() -> None:
    """Тестирует корректность инициализации объекта Smartphone."""
    smartphone = Smartphone(
        name="iPhone 15",
        description="Latest model",
        price=999.99,
        quantity=10,
        efficiency="High",
        model="15 Pro",
        memory=256,
        color="Space Gray",
    )

    assert smartphone.name == "iPhone 15"
    assert smartphone.description == "Latest model"
    assert smartphone.price == 999.99
    assert smartphone.quantity == 10
    assert smartphone.efficiency == "High"
    assert smartphone.model == "15 Pro"
    assert smartphone.memory == 256
    assert smartphone.color == "Space Gray"


def test_smartphone_repr() -> None:
    """Тестирует строковое представление объекта Smartphone."""
    smartphone = Smartphone(
        name="iPhone 15",
        description="Latest model",
        price=999.99,
        quantity=10,
        efficiency="High",
        model="15 Pro",
        memory=256,
        color="Space Gray",
    )

    expected_repr = "Smartphone('iPhone 15', 'Latest model', 999.99, 10, " "'High', '15 Pro', 256, 'Space Gray')"
    assert repr(smartphone) == expected_repr


def test_smartphone_add_success() -> None:
    """Тестирует успешное сложение двух объектов Smartphone."""
    smartphone1 = Smartphone(
        name="iPhone 15",
        description="Latest model",
        price=999.99,
        quantity=10,
        efficiency="High",
        model="15 Pro",
        memory=256,
        color="Space Gray",
    )

    smartphone2 = Smartphone(
        name="iPhone 14",
        description="Previous model",
        price=799.99,
        quantity=5,
        efficiency="Medium",
        model="14 Pro",
        memory=128,
        color="Silver",
    )

    total_quantity = smartphone1 + smartphone2  # Используем оператор + вместо .add()
    assert total_quantity == 15

