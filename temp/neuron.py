import numpy
import random
import math
#propunere in caz de cv sa folosim sigmoid pentru a nu trece de valori 0<val<1
#folisim sigmoid pentru a avea valori booleane
def sigmod(x):
    return 1/(1+numpy.exp(-x))

class Neuron:

    def __init__(self):
        self.weight = numpy.random.uniform(0, 1, 31)
        self.bios = random.uniform(0,1)



    def rez(self, x):
        return float(sigmod((numpy.sum(x[i] * self.weight[i] for  i in range(31))+self.bios)))


    def test(self):
        print(self.weight)
        print(self.bios)

