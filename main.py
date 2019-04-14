#!../bin/python
import sklearn as sk
from Dataloader import Dataloader

class MAP(object):
    def __init__(self):
        self.__version__ = 1.0
        pass


if __name__ == '__main__':
    print('HW1 107003820 蔡宗廷')
    data = Dataloader()
    (Sepal_length, Sepal_width, Petal_length, Petal_width, label) = data.load_training()
    (Sepal_length_test, Sepal_width_test, Petal_length_test, Petal_width_test, label_test) = data.load_testing()
    data.plot(Sepal_length, Sepal_width, Petal_length, Petal_width, label)
    data.plot(Sepal_length_test, Sepal_width_test, Petal_length_test, Petal_width_test, label_test)
