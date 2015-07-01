import random
from NumberGenerator import NumberGenerator

class RandomNumberGenerator(NumberGenerator):

    __number = 0

    def __init__(self):
        self.__random = random
        self.__random.seed(1)

    def get_number(self):
        return self.__number

    def execute(self):
        for i in range(0, 10):
            self.__number = self.__random.randint(0,50)
            self.notify_observers()
