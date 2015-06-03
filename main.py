<<<<<<< HEAD
# -*- coding: utf-8 -*-
from IDCard import IDCardFactory


if __name__ == "__main__":
    factory = IDCardFactory()

    card1 = factory.create("Yamada Taro")
    card2 = factory.create("Kato Jiro")
    card3 = factory.create("Hudo Saburo")

    card1.use()
    card2.use()
    card3.use()
=======
from IDCard import IDCard, IDCardFactory


def __main__:
	factory = IDCardFactory()

	card1 = factory.create("Yamada Taro")
	card2 = factory.create("Yamada Jiro")
	card3 = factory.create("Yamada Saburo")

	card1.use()
	card2.use()
	card3.use()
>>>>>>> e60e1fc4f964f7cd4fafc041abfe2ec0ff8d6f36
