from src.item import Item


class Phone(Item):
    """Phone содержит все атрибуты класса Item и дополнительно атрибут,
       содержащий количество поддерживаемых сим-карт"""

    def __init__(self, name: str, price: int, quantity: int, number_of_sim: int):
        super().__init__(name, price, quantity)
        self.number_of_sim = number_of_sim

    def __str__(self):
        return f"{self.name}"

    def __repr__(self):
        """Отображение инфо в режиме отладки"""
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.__number_of_sim})"

    @property
    def number_of_sim(self):
        """Метод выводит кол-во симкарт"""
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, figure):
        """Запись и проверка кол-ва симкарт"""
        if figure <= 0 or type(figure) != int:
            raise ValueError('Количество физических SIM-карт должно быть целым числом больше нуля')
        else:
            self.__number_of_sim = figure
