
from unittest import TestCase, skip

from online_store.cart import Item, OrderLine


class OrderLineTests(TestCase):
    potatoes = Item("potatoes", 5.80, "bag 2.5kg")
    apples = Item("apples", 3.99, "kg")
    cabbage = Item("cabbage", 3.00, "piece")
    chicken = Item("chicken", 22.99, "kg")

    @skip("not ready yet")
    def test_apples_295(self):
        line = OrderLine(self.apples, 2.95)
        self.assertEqual(line.value(), 11.77)

    def test_apples_200(self):
        line = OrderLine(self.apples, 2)
        self.assertEqual(line.value(), 7.98)
