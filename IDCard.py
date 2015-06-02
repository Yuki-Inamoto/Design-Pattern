from factory import Product, Factory


class IDCard(Product):

    def __init__(self, owner):
        self.owner = owner
        print(owner + "�̃J�[�h�����܂�")

    def use(self):
        print(self.owner + "�̃J�[�h���g���܂�")

    def get_owner(self):
        return self.owner


class IDCardFactory(Factory):

    def __init__(self):
    	self.owners = []

    def create_product(self, owner):
        return IDCard(owner)

    def register_product(self, product):
        owners.append(product.get_owner())

    def get_owners(self):
    	return self.owners

