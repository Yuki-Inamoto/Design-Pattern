from factory import Product, Factory


class IDCard(Product):

    def __init__(self, owner):
        self.owner = owner
        print(owner + "�̃J�[�h�����܂�")

    def use(self):
        print(self.owner + "�̃J�[�h���g���܂�")

    def get_owner(self):
        return self.owner

class IDCard_factory(Factory):
