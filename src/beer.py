'''

No libraries used

'''
class Beer:
    '''

    Beer Object

    '''

    def __init__(self, name, size, style, price, quantity):
        '''

        initialize the beer object and its attributes

        '''
        self.name = name
        self.size = size
        self.style = style
        self.price = price
        self.quantity = quantity

    def get_name(self):
        '''

        Returns: name of the beer object

        '''
        return self.name

    def get_size(self):
        '''

        Returns: size of the beer object

        '''
        return self.size

    def get_style(self):
        '''

        Returns: style (aka type) of the beer object

        '''
        return self.style

    def get_price(self):
        '''

        Returns: price of the beer object

        '''
        return self.price

    def get_quantity(self):
        '''

        Returns: the quantity of the beer object

        '''
        return self.quantity

    def is_available(self):
        '''

        Returns: whether the beer is available in stock

        '''
        if int(self.get_quantity()) > 0:
            return True
        return False
