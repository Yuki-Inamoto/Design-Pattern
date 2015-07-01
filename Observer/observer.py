from abc import ABCMeta, abstractclassmethod
from collections import abc

class Observer(metaclass=ABCMeta):
    @abstractclassmethod
    def update(self, generator):
        pass