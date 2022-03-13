
import pytest

from online_store.cart import Item, OrderLine


apples = Item("apples", 3.99, "kg")
potatoes = Item("potatoes", 5.80, "bag 2.5kg")
cabbage = Item("cabbage", 3.00, "piece")
chicken = Item("chicken", 22.99, "kg")


def test_apples_295():
    line = OrderLine(apples, 2.95)
    assert line.value() == 11.77

def test_apples_200():
    line = OrderLine(apples, 2)
    assert line.value() == 7.98
