import csv
import math

class InstantiateCSVError(Exception):
    def __init__(self, *args, **kwargs):
        self.message = 'Файл item.csv поврежден'

    def __str__(self):
        return self.message

class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity

        Item.all.append(self)

    def __repr__(self):
        return f'{self.__class__.__name__}{self.__name, self.price, self.quantity}'

    def __str__(self):
        return f'{self.__name}'


    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if len(name) > 10:
            name = name[:10]
        self.__name = name

    @classmethod
    def instantiate_from_csv(cls, data="../src/items.csv"):
        try:
            Item.all =[]
            with open(data, 'r', encoding='windows-1251') as file:

                f = csv.DictReader(file)
                len_reader = len(f.fieldnames)
                if len_reader != 3:
                    raise InstantiateCSVError

                for i in f:
                    Item(i['name'], i['price'], i['quantity'])

        except FileNotFoundError:
            print("Отсутствует файл item.csv")
            raise
        except InstantiateCSVError:
            print("Файл item.csv поврежден")
            raise



    @staticmethod
    def string_to_number(num):
        if "." in num:
            num = float(num)
            return math.floor(num)
        else:
            num = int(num)
            return num

    def __add__(self, other):
        if not issubclass(other.__class__, self.__class__):
            raise ValueError('Можно складывать объекты Item и их дочерних')
        return self.quantity + other.quantity

