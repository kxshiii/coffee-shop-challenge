import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from coffee import Coffee
from customer import Customer
from order import Order

def test_coffee_name_validation():
    try:
        Coffee(123)
        assert False
    except TypeError:
        pass
    try:
        Coffee("ab")
        assert False
    except ValueError:
        pass
    c = Coffee("Americano")
    assert c.name == "Americano"

def test_coffee_orders_and_customers():
    coffee = Coffee("Cappuccino")
    c1 = Customer("X")
    c2 = Customer("Y")
    o1 = Order(c1, coffee, 2.0)
    o2 = Order(c2, coffee, 3.0)
    assert o1 in coffee.orders()
    assert o2 in coffee.orders()
    assert c1 in coffee.customers()
    assert c2 in coffee.customers()

def test_num_orders_and_average_price():
    coffee = Coffee("Drip")
    c1 = Customer("M")
    c2 = Customer("N")
    Order(c1, coffee, 2.0)
    Order(c2, coffee, 4.0)
    assert coffee.num_orders() == 2
    assert coffee.average_price() == 3.0