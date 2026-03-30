import numpy
class Tree:
    def __init__(self, date):
        self.optims = [numpy.random.uniform(numpy.min(date[:, i]), numpy.max(date[:, i])) for i in range(len(date[:, 0]))]


    #am un model de train in folderul meu de ml din C
    def Train(self):
        pass
    

    def Choice(self):
        pass