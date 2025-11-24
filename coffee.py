class Coffee:
    all = []

    def __init__(self, name):
        self.name = name
        Coffee.all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError("Coffee name must be a string.")
        if len(name) < 3:
            raise ValueError("Coffee name must be at least 3 characters long.")
        self._name = name

    def orders(self):
        from order import Order 
        return [order for order in Order.all if order.coffee is self]

    def customers(self):
        return list({order.customer for order in self.orders()})

    def num_orders(self):
        return len(self.orders())

    def average_price(self):
        orders_list = self.orders()
        if not orders_list:
            return 0.0
        total = sum(order.price for order in orders_list)
        return total / len(orders_list)

    def __repr__(self):
        return f"<Coffee name='{self.name}'>"
