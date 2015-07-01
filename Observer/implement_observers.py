import time
import sys
from observer import Observer

class DigitObserver(Observer):

    def update(self, generator):
        print('DigitObserver: ' + str(generator.get_number()))
        try:
            time.sleep(5)
        except:
            pass

class GraphObserver(Observer):

    def update(self, generator):
        # sys.stdout.writeで改行しない出力
        sys.stdout.write("GraphObserver:")
        count = generator.get_number()
        for i in range(0, count):
            sys.stdout.write("*")
        print('')
        try:
            time.sleep(5)
        except:
            pass