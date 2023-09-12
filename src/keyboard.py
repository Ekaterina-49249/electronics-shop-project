from src.item import Item


class LangMixin:
    """Класс хранит и изменяет язык клавиатуры"""

    def __init__(self, language: str = "EN"):
        """Инициализация класса LangMixin"""
        self.__language = language

    @property
    def language(self):
        """Метод сохраняет раскладку клавиатуры"""

        return self.__language

    def change_lang(self):
        """Mетод для изменения раскладки клавиатуры"""

        if self.language == "EN":
            self.__language = "RU"
        elif self.language == "RU":
            self.__language = "EN"
            return self


class Keyboard(Item, LangMixin):

    def __init__(self, name: str, price: float, quantity: int, language: str = "EN"):
        super().__init__(name, price, quantity)
        LangMixin.__init__(self, language)
