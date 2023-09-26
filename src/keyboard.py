from src.item import Item
class Product(Item):

    def __init__(self, name, price, quantity, language='EN'):
        self.language = language
        super().__init__(name, price, quantity)

class Product_Mixin:
    def change_lang(self):
        if self.language == 'EN':
            self.language = 'RU'
        else:
            self.language = 'EN'

class Keyboard(Product, Product_Mixin):
    pass

