class Laser:
    @staticmethod
    def does():
        return 'disintegrate'


class Claw:
    @staticmethod
    def does():
        return 'crush'


class Smartphone:
    @staticmethod
    def does():
        return 'ring'


class Robot:
    laser = Laser()
    claw = Claw()
    smartphone = Smartphone()

    def does(self):
        print(
            self.laser.does(),
            self.claw.does(),
            self.smartphone.does()
        )
