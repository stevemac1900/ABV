class Beer:
    # pylint: disable=too-many-arguments
    def __init__(self, name, size, style, price, quantity):
        self.name = name
        self.size = size
        self.style = style
        self.price = price
        self.quantity = quantity

    def get_name(self):
        return self.name

    def get_size(self):
        return self.size

    def get_style(self):
        return self.style

    def get_price(self):
        return self.price

    def get_quantity(self):
        return self.quantity

    def is_available(self):
        if float(self.get_quantity()) > 0.0:
            return True
        return False
