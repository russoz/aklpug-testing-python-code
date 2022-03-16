import pytest

from online_store.shop import Shop, OutOfStockException, TooLargeQuantityException
from online_store.cart import Item


user = "johndoe"

apples = Item("apples", 3.99, "kg")
potatoes = Item("potatoes", 5.80, "bag 2.5kg")
cabbage = Item("cabbage", 3.00, "piece")
chicken = Item("chicken", 22.99, "kg")


@pytest.fixture()
def make_shop():
    shop = Shop()

    shop.add_to_shelf(apples, 7)
    shop.add_to_shelf(potatoes, 10)
    shop.add_to_shelf(cabbage, 5)
    shop.add_to_shelf(chicken, 2)
    return shop

def test_add_to_shelf(make_shop):
    shop = make_shop

    assert len(shop.shelf) == 4
    assert set(shop.shelf.keys()) == {"apples", "potatoes", "cabbage", "chicken"}
    assert shop.shelf["apples"] == (Item("apples", 3.99, "kg"), 7)
    assert shop.shelf["potatoes"] == (Item("potatoes", 5.80, "bag 2.5kg"), 10)
    assert shop.shelf["cabbage"] == (Item("cabbage", 3.00, "piece"), 5)
    assert shop.shelf["chicken"] == (Item("chicken", 22.99, "kg"), 2)


remove_testdata = [
    (apples, 3, 4),
    (potatoes, 2, 8),
    (cabbage, 1, 4),
    (chicken, 1, 1),
]

@pytest.mark.parametrize("item,qty,remaining", remove_testdata)
def test_shop_remove_from_shelf(make_shop, item, qty, remaining):
    shop = make_shop

    shop.remove_from_shelf(item, qty)
    assert shop.shelf[item.name] == (item, remaining)

exc_testdata = [
    (apples, 200, TooLargeQuantityException),
    (potatoes, 100, TooLargeQuantityException),
    (Item("banana", 3.5, "unit"), 5, OutOfStockException),
]

@pytest.mark.parametrize("item,qty,exception", exc_testdata)
def test_shop_remove_exception(make_shop, item, qty, exception):
    shop = make_shop
    with pytest.raises(exception):
        shop.remove_from_shelf(item, qty)
