import matplotlib.pyplot as Plot





class DataCompare:
    def __init__(self, data):
        self.data = data

    def RepFraudNormal(self):
        count_Normal = sum(1 for k in self.data if k[-1]==0)
        count_Fraud = sum(1 for k in self.data if k[-1]==1)
        Plot.bar(count_Normal, count_Fraud)
