# -*- coding: utf-8 -*-
from factory import Product, Factory


class IDCard(Product):

    def __init__(self, owner):
        self.owner = owner
        print(owner + "のカードを作ります")

    def use(self):
        print(self.owner + "のカードを使います")

    def get_owner(self):
        return self.owner


class IDCardFactory(Factory):

    def __init__(self):
        self.owners = []
<<<<<<< HEAD
=======
=======
<<<<<<< HEAD
class IDCardFactory(Factory):

    def __init__(self):
    	self.owners = []
>>>>>>> bfc45261be3c369b976b076e992c5642d3f1f3f8

    def create_product(self, owner):
        return IDCard(owner)

    def register_product(self, product):
        owners.append(product.get_owner())

    def get_owners(self):
    	return self.owners
<<<<<<< HEAD
=======
=======
class IDCard_Factory(Factory):
>>>>>>> e60e1fc4f964f7cd4fafc041abfe2ec0ff8d6f36

    def create_product(self, owner):
        return IDCard(owner)

<<<<<<< HEAD
    def register_product(self, product):
        self.owners.append(product.get_owner())
=======
    def register_product(self, owner):
        pass
>>>>>>> 453cc352229bfe9d037c3b73feb82af6a9e9d34f
>>>>>>> e60e1fc4f964f7cd4fafc041abfe2ec0ff8d6f36

    def get_owners(self):
        return self.owners
>>>>>>> bfc45261be3c369b976b076e992c5642d3f1f3f8
