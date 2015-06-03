# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod


class Product(metaclass=ABCMeta):
    @abstractmethod
    def use(self):
        pass


class Factory(metaclass=ABCMeta):

    def create(self, owner):
        product = self.create_product(owner)
        self.register_product(product)
        return product

    @abstractmethod
    def create_product(self, owner):
        pass

    @abstractmethod
<<<<<<< HEAD
    def register_product(self, product):
=======
<<<<<<< HEAD
    def register_product(self, product):
=======
    def register_product(self, owner):
>>>>>>> 453cc352229bfe9d037c3b73feb82af6a9e9d34f
>>>>>>> e60e1fc4f964f7cd4fafc041abfe2ec0ff8d6f36
        pass
