class Element:
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number


fifth_element = Element('Hydrogen', 'H', 1)


# args solution
class Element2:
    def __init__(self, *args):
        params = ['name', 'symbol', 'number']
        self.attributes = dict(pair for pair in zip(params, args))


fourth_element = Element2('Hydrogen', 'H', 1)
