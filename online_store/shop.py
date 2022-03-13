from online_store.cart import Cart
from online_store.payment_svc import PaymentService


class OutOfStockException(Exception):
    def __init__(self, item):
        self.item = item
        super().__init__(f"Item out of stock: {item.name}")


class TooLargeQuantityException(Exception):
    def __init__(self, item, qty: float, available: float):
        self.item = item
        self.qty = qty
        self.available = available
        super().__init__(f"Not enough in stock to fulfill order: "
                         f"{qty}x {item.name} ({available} available")


class Shop:
    shelf = {}
    carts = {}
    payment_service = PaymentService

    def add_to_shelf(self, item, qty: float):
        if item.name in self.shelf:
            _, shelf_qty = self.shelf[item.name]
            qty = qty + shelf_qty
        self.shelf[item.name] = (item, qty)

    def remove_from_shelf(self, item, qty: float):
        if item.name not in self.shelf:
            raise OutOfStockException(item)
        _, shelf_qty = self.shelf[item]
        if shelf_qty < qty:
            raise TooLargeQuantityException(item, qty, shelf_qty)
        self.shelf[item.name] = (item, shelf_qty - qty)

    def get_cart(self, user: str):
        if user not in self.carts:
            self.carts[user] = Cart()
        return self.carts[user]

    def add_to_cart(self, user: str, item, qty: float):
        cart = self.get_cart(user)
        self.remove_from_shelf(item, qty)
        cart.add_item(item, qty)

    def checkout(self, user: str):
        total = self.get_cart(user).total
        self.payment_service.charge(user, total)

    def clear_cart(self, user: str):
        cart = self.get_cart(user)
        for line in cart.order_lines:
            self.add_to_shelf(line.item, line.qty)
        cart.clear()
