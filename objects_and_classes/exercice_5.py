class Element:
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number


object_attributes = {'name': 'Hydrogen', 'symbol': 'H', 'number': 1}

fifth_element = Element(
    object_attributes['name'],
    object_attributes['symbol'],
    object_attributes['number']
)
