class Order:
    all = []

    def __init__(self, customer, coffee, price):
        from customer import Customer
        from coffee import Coffee
        if not isinstance(customer, Customer):
            raise TypeError("Customer must be an instance of the Customer class.")
        if not isinstance(coffee, Coffee):
            raise TypeError("Coffee must be an instance of the Coffee class.")
        if not isinstance(price, (float, int)):
            raise TypeError("Price must be a number.")
        if not 1.0 <= price <= 10.0:
            raise ValueError("Price must be between 1.0 and 10.0.")

        self._customer = customer
        self._coffee = coffee
        self._price = float(price)
        Order.all.append(self)

    @property
    def customer(self):
        return self._customer

    @customer.setter
    def customer(self, customer):
        from customer import Customer
        if not isinstance(customer, Customer):
            raise TypeError("Customer must be an instance of the Customer class.")
        self._customer = customer

    @property
    def coffee(self):
        return self._coffee

    @coffee.setter
    def coffee(self, coffee):
        from coffee import Coffee
        if not isinstance(coffee, Coffee):
            raise TypeError("Coffee must be an instance of the Coffee class.")
        self._coffee = coffee

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price):
        if not isinstance(price, (float, int)):
            raise TypeError("Price must be a number.")
        if not 1.0 <= price <= 10.0:
            raise ValueError("Price must be between 1.0 and 10.0.")
        self._price = float(price)

    def __repr__(self):
        return f"<Order customer='{self.customer.name}' coffee='{self.coffee.name}' price={self.price:.2f}>"
