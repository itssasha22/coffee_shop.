import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from customer import Customer
from coffee import Coffee
from order import Order

def test_customer_name_valid():
    c = Customer("Alice")
    assert c.name == "Alice"

def test_customer_name_invalid_type():
    with pytest.raises(TypeError):
        Customer(123)

def test_customer_name_too_short():
    with pytest.raises(ValueError):
        Customer("")

def test_customer_name_too_long():
    with pytest.raises(ValueError):
        Customer("a" * 16)

def test_orders_and_coffees_relationship():
    c = Customer("Bob")
    coffee1 = Coffee("Espresso")
    coffee2 = Coffee("Latte")
    order1 = c.create_order(coffee1, 3.5)
    order2 = c.create_order(coffee2, 4.0)
    assert order1 in c.orders()
    assert order2 in c.orders()
    assert coffee1 in c.coffees()
    assert coffee2 in c.coffees()

def test_create_order_invalid_price():
    c = Customer("Carol")
    coffee = Coffee("Mocha")
    with pytest.raises(TypeError):
        c.create_order(coffee, "cheap")
    with pytest.raises(ValueError):
        c.create_order(coffee, 0.5)

def test_most_aficionado():
    c1 = Customer("Dave")
    c2 = Customer("Eve")
    coffee = Coffee("Cappuccino")
    c1.create_order(coffee, 5.0)
    c1.create_order(coffee, 2.0)
    c2.create_order(coffee, 10.0)
    assert Customer.most_aficionado(coffee) == c2

def test_most_aficionado_no_orders():
    coffee = Coffee("NoOrders")
    assert Customer.most_aficionado(coffee) is None
