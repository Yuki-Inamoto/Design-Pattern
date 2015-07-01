from implement_observers import DigitObserver, GraphObserver
from RandomNumberGenerator import RandomNumberGenerator


if __name__ == "__main__":
    generator = RandomNumberGenerator()

    observer1 = DigitObserver()
    observer2 = GraphObserver()

    generator.add_observer(observer1)
    generator.add_observer(observer2)

    generator.execute()
