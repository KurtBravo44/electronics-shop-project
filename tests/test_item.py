"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest

from src.item import Item

pay_rate = 2.0
ex = Item("Холодильник", 5000.0, 10)
def test_calculate_total_price():
    assert ex.price * ex.quantity == 50000.0
    assert Item.calculate_total_price(ex) == 50000.0

def test_apply_discount():
    assert Item.apply_discount(ex) == None


def test_string_to_number():
    assert Item.string_to_number('2') == 2
    assert Item.string_to_number('6.5') == 6


ex_1 = Item('Car', 100, 5)
def test_name():
    ex_1.name = 'SuperCar'
    assert ex_1.name == "SuperCar"
    ex_1.name = 'SuperSuperCar'
    assert ex_1.name == 'SuperSuper'

def test_instantiate_from_csv():
    Item.instantiate_from_csv('../src/items.csv')
    assert len(Item.all) == 5

ex_2 = Item('Calculator', 100, 10)
def test__repr__():
    assert repr(ex_2) == "Item('Calculator', 100, 10)"

def test__str__():
    assert  str(ex_2) == 'Calculator'
