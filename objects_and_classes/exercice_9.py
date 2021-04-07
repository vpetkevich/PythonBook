class Bear:
    @staticmethod
    def eats():
        return 'berries'


class Rabbit:
    @staticmethod
    def eats():
        return 'clover'


class Octothorpe:
    @staticmethod
    def eats():
        return 'campers'


teddy = Bear()
print(teddy.eats())

rodger = Rabbit()
print(rodger.eats())

strange = Octothorpe()
print(strange.eats())
