from factory import Product, Factory


class IDCard(Product):

    def __init__(self, owner):
        self.owner = owner
        print(owner + "のカードを作ります")

    def use(self):
        print(self.owner + "のカードを使います")

    def get_owner(self):
        return self.owner

class IDCard_factory(Factory):
