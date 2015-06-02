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
    def create_product(self):
        pass

    @abstractmethod
    def register_product(self):
        pass
