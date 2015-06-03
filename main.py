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
