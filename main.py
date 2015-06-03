# -*- coding: utf-8 -*-
from IDCard import IDCardFactory


if __name__ == "__main__":
    factory = IDCardFactory()

    card1 = factory.create("Yamada Taro")
    card2 = factory.create("Yamada Jiro")
    card3 = factory.create("Yamada Saburo")

    card1.use()
    card2.use()
    card3.use()
