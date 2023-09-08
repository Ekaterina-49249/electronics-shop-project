import pytest
from src.phone import Phone


@pytest.fixture
def phone_fix():
    return Phone("iPhone 14", 120_000, 5, 2)


def test_numbers_sim(phone_fix):
    """Тест на кол-во симкарт"""
    assert phone_fix.number_of_sim == 2

    phone_fix.number_of_sim = 3
    assert phone_fix.number_of_sim == 3

    with pytest.raises(ValueError):
        phone_fix.number_of_sim = 0
        assert phone_fix.number_of_sim == 'Количество физических SIM-карт должно быть целым числом больше нуля'


def test_repr(phone_fix):
    """Тест repr"""
    assert repr(phone_fix) == "Phone('iPhone 14', 120000, 5, 2)"


def test_str(phone_fix):
    """Тест str"""
    assert str(phone_fix) == 'iPhone 14'
