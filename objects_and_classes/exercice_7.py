class Element:
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number

    def __str__(self):
        return str(vars(self))


fifth_element = Element('Hydrogen', 'H', 1)
print(fifth_element)
