import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from order import Order
from customer import Customer
from coffee import Coffee

def setup_function():
    Order._all.clear()
    Customer._all.clear()
    Coffee._all.clear()

def test_order_validation():
    setup_function()
    c = Customer("Emma")
    coffee = Coffee("Latte")
    try:
        Order("not_customer", coffee, 2.0)
        assert False
    except TypeError:
        pass
    try:
        Order(c, "not_coffee", 2.0)
        assert False
    except TypeError:
        pass
    try:
        Order(c, coffee, "not_float")
        assert False
    except TypeError:
        pass
    try:
        Order(c, coffee, 0.5)
        assert False
    except ValueError:
        pass
    try:
        Order(c, coffee, 11.0)
        assert False
    except ValueError:
        pass
    o = Order(c, coffee, 3.5)
    assert o.customer == c
    assert o.coffee == coffee
    assert o.price == 3.5

def test_order_all_list():
    setup_function()
    c = Customer("Drake")
    coffee = Coffee("Espresso")
    o1 = Order(c, coffee, 2.5)
    o2 = Order(c, coffee, 3.0)
    assert o1 in Order._all
    assert o2 in Order._all
    assert len(Order._all) == 2