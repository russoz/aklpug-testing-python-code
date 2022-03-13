
from collections import namedtuple
from functools import reduce
from operator import add


class Item(namedtuple("_Item", ["name", "price", "unit"])):
    pass


class OrderLine(namedtuple("_OrderLine", ["item", "qty"])):
    def value(self):
        return round(self.item.price * self.qty, 2)


class Cart:
    def __init__(self) -> None:
        self.order_lines = []

    def add_item(self, item: Item, qty: float):
        self.order_lines.append(OrderLine(item, qty))

    def clear(self):
        self.order_lines = []

    @property
    def total(self):
        return reduce(add, [line.value() for line in self.order_lines])

    def __repr__(self) -> str:
        lines = [f"{ind}: {(l.item.name, l.qty, l.value())}"
                 for ind, l in enumerate(self.order_lines)]
        return f"<Cart total=${self.total} : {', '.join(lines)}>"

    def __str__(self) -> str:
        return repr(self)
