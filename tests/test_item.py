"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest

from src.item import Item


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
