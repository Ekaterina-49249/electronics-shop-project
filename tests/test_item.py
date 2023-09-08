"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.phone import Phone
from src.item import Item


@pytest.fixture
def phone_class_fix():
    return Phone("Samsung", 50000, 90, 2)


@pytest.fixture
def item_class_fix():
    return Item("LG", 80000, 10)


def test_add_class(item_class_fix, phone_class_fix):
    """Тест на сложение экземпляров двух классов"""
    assert item_class_fix + phone_class_fix == 100
    assert item_class_fix + item_class_fix == 20
    with pytest.raises(ValueError):
        assert item_class_fix + 10000 == "Нельзя складывать экземпляры не дочерних классов"
        assert phone_class_fix + 50 == "Нельзя складывать экземпляры не дочерних классов"


@pytest.fixture()
def dummy_item():
    return Item("", 0, 0)


def test_calculate_total_price():
    item1 = Item("Смартфон", 10000, 20)
    item2 = Item("Ноутбук", 20000, 5)
    assert item1.calculate_total_price() == 200000
    assert item2.calculate_total_price() == 100000


def test_apply_discount():
    item1 = Item("", 5000, 0)

    Item.pay_rate = 0.8
    item1.apply_discount()
    assert item1.price == 4000


def test_name(dummy_item):
    dummy_item.name = "Магнитофон"
    assert dummy_item.name == "Магнитофон"


def test_name_raise_exception(dummy_item):
    with pytest.raises(Exception):
        dummy_item.name = "Компьютерная мышь"


def test_string_to_number():
    assert Item.string_to_number("7") == 7
    assert Item.string_to_number('5.0') == 5


def test_instantiate_from_csv():
    Item.instantiate_from_csv('src/items.csv')
    assert len(Item.all) == 5
    assert type(Item.all[0]) is Item


def test_str():
    ex1 = Item("Чайник", 2000, 10)
    assert str(ex1) == "Чайник"


def test_repr():
    ex2 = Item("Бритва", 1500, 50)
    assert repr(ex2) == "Item('Бритва', 1500, 50)"
