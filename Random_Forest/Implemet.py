import numpy
class Tree:
    def __init__(self, date):
        self.best = [numpy.random.uniform(numpy.min(date[:-1, i]), numpy.max(date[:-1, i])) for i in range(len(date[:-1, 0]))]
        self.date = date.copy()

    def Train(self):



        pass

    #am un model de train in folderul meu de ml din C
    def Choice_recursiv(self, tuplu, index):
        if tuplu[index] <= self.best[index]:
            left_index = 2 * index + 1
            if left_index >= len(self.best):
                return 0
            else:
                return self.Choice_recursiv(tuplu, left_index)
        else:
            right_index = 2 * index + 2
            if right_index >= len(self.best):
                return 1
            else:
                return self.Choice_recursiv(tuplu, right_index)

