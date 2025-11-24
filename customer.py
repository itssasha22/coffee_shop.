class Customer:
    all = []

    def __init__(self, name):
        self.name = name
        Customer.all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError("Customer name must be a string.")
        if not 1 <= len(name) <= 15:
            raise ValueError("Customer name must be between 1 and 15 characters.")
        self._name = name

    def orders(self):
        from order import Order
        return [order for order in Order.all if order.customer is self]

    def coffees(self):
        return list({order.coffee for order in self.orders()})

    def create_order(self, coffee, price):
        from order import Order
        from coffee import Coffee
        if not isinstance(coffee, Coffee):
            raise TypeError("coffee must be an instance of Coffee")
        if not isinstance(price, (float, int)):
            raise TypeError("price must be a number")
        if not 1.0 <= price <= 10.0:
            raise ValueError("price must be between 1.0 and 10.0")
        new_order = Order(self, coffee, float(price))
        return new_order

    @classmethod
    def most_aficionado(cls, coffee):
        from order import Order
        from coffee import Coffee
        if not isinstance(coffee, Coffee):
            raise TypeError("coffee must be an instance of Coffee")
        customer_spending = {}
        for order in Order.all:
            if order.coffee is coffee:
                customer_spending[order.customer] = customer_spending.get(order.customer, 0) + order.price
        if not customer_spending:
            return None
        max_customer = max(customer_spending, key=customer_spending.get)
        return max_customer

    def __repr__(self):
        return f"<Customer name='{self.name}'>"
