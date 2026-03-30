import numpy
class Tree:
    def __init__(self, date):
        self.best = [numpy.random.uniform(numpy.min(date[:, i]), numpy.max(date[:, i])) for i in range(len(date[:, 0]))]


    #am un model de train in folderul meu de ml din C
    def Train(self):
        pass
    

    def Choice(self, tuplu):
        if tuplu[0] < self.best[0]: #v1
            if tuplu[1] < self.best[1]: #v2
                

        else:

            if tuplu[2] < self.best[2]: #v3

        pass