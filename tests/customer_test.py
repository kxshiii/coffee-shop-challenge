import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from customer import Customer
from coffee import Coffee
from order import Order

def test_customer_name_validation():
    try:
        Customer(123)
        assert False
    except TypeError:
        pass
    try:
        Customer("")
        assert False
    except ValueError:
        pass
    try:
        Customer("a" * 16)
        assert False
    except ValueError:
        pass
    c = Customer("drake")
    assert c.name == "drake"
    c.name = "Emma"
    assert c.name == "Emma"
    try:
        c.name = 123
        assert False
    except TypeError:
        pass
    try:
        c.name = ""
        assert False
    except ValueError:
        pass

def test_customer_orders_and_coffees():
    c = Customer("Eve")
    coffee1 = Coffee("Latte")
    coffee2 = Coffee("Mocha")
    o1 = c.create_order(coffee1, 2.5)
    o2 = c.create_order(coffee2, 3.0)
    assert o1 in c.orders()
    assert o2 in c.orders()
    assert coffee1 in c.coffees()
    assert coffee2 in c.coffees()

def test_most_aficionado():
    c1 = Customer("A")
    c2 = Customer("B")
    coffee = Coffee("Espresso")
    c1.create_order(coffee, 5.0)
    c2.create_order(coffee, 6.0)
    assert Customer.most_aficionado(coffee) == c2