import numpy
class Tree:
    def __init__(self, date):
        self.best = numpy.zeros(len(date[0, :]) - 1)
        self.date = date.copy()


    def calculate_gini(self, count0, count1):
        total = count0 + count1
        if total == 0:
            return 0

        p0 = count0/total
        p1 = count1/total
        return 1-(p0**2 + p1**2)



    def Train(self):
        for col in range(len(self.date[0, :]) - 1):
            gini_best = 999
            for threshold in self.date[:, col]:
                left_mask = self.date[:, col] <= threshold
                right_mask = self.date[:, col] > threshold

                left_labels = self.date[left_mask, -1]
                right_labels = self.date[right_mask, -1]

                left_0 = numpy.sum(left_labels == 0)
                left_1 = numpy.sum(left_labels == 1)
                right_0 = numpy.sum(right_labels == 0)
                right_1 = numpy.sum(right_labels == 1)

                gini_left = self.calculate_gini(left_0, left_1)
                gini_right = self.calculate_gini(right_0, right_1)

                total_left = len(left_labels)
                total_right = len(right_labels)
                total_rows = len(self.date)

                gini_split = (total_left / total_rows) * gini_left + (total_right / total_rows) * gini_right

                if gini_split < gini_best:
                    gini_best = gini_split
                    self.best[col] = threshold


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

