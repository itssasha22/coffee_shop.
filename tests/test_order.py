import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from order import Order
from customer import Customer
from coffee import Coffee

def test_order_properties_and_validation():
    c = Customer("Chris")
    coffee = Coffee("Mocha")
    order = Order(c, coffee, 4.0)
    assert order.customer == c
    assert order.coffee == coffee
    assert order.price == 4.0

    with pytest.raises(TypeError):
        Order("notcustomer", coffee, 4.0)
    with pytest.raises(TypeError):
        Order(c, "notcoffee", 4.0)
    with pytest.raises(TypeError):
        Order(c, coffee, "4.0")
    with pytest.raises(ValueError):
        Order(c, coffee, 0.5)
    with pytest.raises(ValueError):
        Order(c, coffee, 15.0)

def test_price_setter_validation():
    c = Customer("Dana")
    coffee = Coffee("Espresso")
    order = Order(c, coffee, 5.0)
    with pytest.raises(TypeError):
        order.price = "cheap"
    with pytest.raises(ValueError):
        order.price = 0.5
    with pytest.raises(ValueError):
        order.price = 15.0
    order.price = 7.5
    assert order.price == 7.5

def test_customer_setter_validation():
    c1 = Customer("Eli")
    c2 = Customer("Fay")
    coffee = Coffee("Latte")
    order = Order(c1, coffee, 3.0)
    with pytest.raises(TypeError):
        order.customer = "notcustomer"
    order.customer = c2
    assert order.customer == c2

def test_coffee_setter_validation():
    c = Customer("Gina")
    coffee1 = Coffee("Macchiato")
    coffee2 = Coffee("Cortado")
    order = Order(c, coffee1, 6.0)
    with pytest.raises(TypeError):
        order.coffee = "notcoffee"
    order.coffee = coffee2
    assert order.coffee == coffee2
