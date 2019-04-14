import scipy.io as sio
import matplotlib.pyplot as plt

print_load_msg = False

class Dataloader(object):
    def __init__(self):
        self.__version__ = 1.0
        pass

    def load_training(self, training_set="training.mat"):
        dataset = sio.loadmat(training_set)
        Sepal_length = dataset['Sepal_length'][0]
        Sepal_width = dataset['Sepal_width'][0]
        Petal_length = dataset['Petal_length'][0]
        Petal_width = dataset['Petal_width'][0]
        label = dataset['label'][0]

        print("Training set Size",len(label))
        if print_load_msg == True:
            print("Sepal_length\n", Sepal_length, "\n")
            print("Sepal_width\n", Sepal_width, "\n")
            print("Petal_length\n", Petal_length, "\n")
            print("Petal_width\n", Petal_width, "\n")
            print("label\n", label, "\n")

        return (Sepal_length, Sepal_width, Petal_length, Petal_width, label)

    def load_testing(self, testing_set="testing.mat"):
        dataset = sio.loadmat(testing_set)
        Sepal_length_test = dataset['Sepal_length_test'][0]
        Sepal_width_test = dataset['Sepal_width_test'][0]
        Petal_length_test = dataset['Petal_length_test'][0]
        Petal_width_test = dataset['Petal_width_test'][0]
        label_test = dataset['label_test'][0]

        print("Testing set Size",len(label_test))
        if print_load_msg == True:            
            print("Sepal_length\n", Sepal_length_test, "\n")
            print("Sepal_width\n", Sepal_width_test, "\n")
            print("Petal_length\n", Petal_length_test, "\n")
            print("Petal_width\n", Petal_width_test, "\n")
            print("label_test\n", label_test, "\n")

        return (Sepal_length_test, Sepal_width_test, Petal_length_test, Petal_width_test, label_test)

    def plot(self, Sepal_length, Sepal_width, Petal_length, Petal_width, labels):
        plt.figure()

        plt.subplot(2,1,1)
        for (i, label) in enumerate(labels):
            if label == 0:
                plt.plot(Sepal_length[i], Sepal_width[i], 'ro')
            if label == 1:
                plt.plot(Sepal_length[i], Sepal_width[i], 'yo')
            if label == 2:
                plt.plot(Sepal_length[i], Sepal_width[i], 'bo')

        xlabel = "Sepal-length"
        ylabel = "Sepal-width"
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)

        plt.subplot(2,1,2)        
        for (i, label) in enumerate(labels):
            if label == 0:
                plt.plot(Petal_length[i], Petal_width[i], 'ro')
            if label == 1:
                plt.plot(Petal_length[i], Petal_width[i], 'yo')
            if label == 2:
                plt.plot(Petal_length[i], Petal_width[i], 'bo')

        xlabel = "Petal-length"
        ylabel = "Petal-width"
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)

        plt.show()
        pass
