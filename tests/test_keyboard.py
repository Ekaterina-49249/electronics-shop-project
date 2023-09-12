import pytest
from src.keyboard import Keyboard


@pytest.fixture()
def fix_keyboard():
    return Keyboard("Dark Project KD87A", 9600, 5)


def test_init(fix_keyboard):
    """Тестирование инициализации клавиатуры"""

    assert fix_keyboard.name == "Dark Project KD87A"
    assert fix_keyboard.price == 9600
    assert fix_keyboard.quantity == 5
    assert fix_keyboard.language == "EN"


def test_change_lang(fix_keyboard):
    """Тестирование изменения раскладки клавиатуры"""

    fix_keyboard.change_lang()
    assert fix_keyboard.language == "RU"

    fix_keyboard.change_lang()
    assert fix_keyboard.language == "EN"


