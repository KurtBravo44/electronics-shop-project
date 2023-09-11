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
