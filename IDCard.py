from factory import Product, Factory


class IDCard(Product):

    def __init__(self, owner):
        self.owner = owner
        print(owner + "のカードを作ります")

    def use(self):
        print(self.owner + "のカードを使います")

    def get_owner(self):
        return self.owner


<<<<<<< HEAD
class IDCardFactory(Factory):

    def __init__(self):
    	self.owners = []

    def create_product(self, owner):
        return IDCard(owner)

    def register_product(self, product):
        owners.append(product.get_owner())

    def get_owners(self):
    	return self.owners
=======
class IDCard_Factory(Factory):

    def create_product(self, owner):
        return IDCard_Factory(owner)

    def register_product(self, owner):
        pass
>>>>>>> 453cc352229bfe9d037c3b73feb82af6a9e9d34f

