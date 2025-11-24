import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from coffee import Coffee
from customer import Customer

def test_coffee_name_valid():
    coffee = Coffee("Americano")
    assert coffee.name == "Americano"

def test_coffee_name_invalid_type():
    with pytest.raises(TypeError):
        Coffee(123)

def test_coffee_name_too_short():
    with pytest.raises(ValueError):
        Coffee("ab")

def test_orders_customers_num_orders_average_price():
    coffee = Coffee("Flat White")
    c1 = Customer("Anna")
    c2 = Customer("Ben")
    o1 = c1.create_order(coffee, 4.5)
    o2 = c2.create_order(coffee, 5.5)

    orders = coffee.orders()
    customers = coffee.customers()
    num_orders = coffee.num_orders()
    avg_price = coffee.average_price()

    assert o1 in orders
    assert o2 in orders
    assert c1 in customers
    assert c2 in customers
    assert num_orders == 2
    assert avg_price == pytest.approx((4.5 + 5.5) / 2)
