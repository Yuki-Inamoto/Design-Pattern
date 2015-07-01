from abc import ABCMeta, abstractclassmethod


class NumberGenerator(metaclass=ABCMeta):
    __observers = []

    def add_observer(self, observer):
        self.__observers.append(observer)

    def delete_observe(self, observer):
        self.__observers.remove(observer)

    def notify_observers(self):
        for observer in self.__observers:
            observer.update(self)

    @abstractclassmethod
    def get_number(self):
        pass

    @abstractclassmethod
    def execute(self):
        pass