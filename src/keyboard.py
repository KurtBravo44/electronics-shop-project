from src.item import Item
class Product(Item):

    def __init__(self, name, price, quantity, language='EN'):
        self._language = language
        super().__init__(name, price, quantity)

class Product_Mixin:
    @property
    def language(self):
        return self._language

    def change_lang(self):
        if self._language == 'EN':
            self._language = 'RU'
        else:
            self._language = 'EN'


class Keyboard(Product, Product_Mixin):
    pass
