class Element:
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number

    def dump(self):
        print(vars(self))


fifth_element = Element('Hydrogen', 'H', 1)
fifth_element.dump()
