import matplotlib.pyplot as Plot
import numpy




class DataComparing:
    def __init__(self, data):
        self.data =numpy.array(data)

    def RepFraudNormal(self): #reprezentasion of Fraud and Normal tranzactions
        labels = numpy.array(self.data[:, -1])
        count_Normal = numpy.sum(labels == 0)
        count_Fraud = numpy.sum(labels == 1)

        Plot.bar(["Normal tranz", "Fraud tranz"],[count_Normal, count_Fraud], color=["green", "red"])
        Plot.xlabel("Transaction Type")
        Plot.ylabel("Count")
        Plot.title("Fraud vs Normal Transactions")
        Plot.show()