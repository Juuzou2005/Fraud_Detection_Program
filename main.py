import numpy
import csv_extraction.reading_data as reading
from analize_data.Comparing_data import DataComparing
from csv_extraction.convert import standardization
from Random_Forest.Implemet import Tree



data = reading.data_set(r"F:\practica\data_set\creditcard.csv") #add dataset path here
#print(data)
#observarea datelor prin grafice
# observ = DataComparing(data)
# observ.RepFraudNormal()
# observ.BoxPLot()
# observ.ScaterPlot()

#aducem datele in valori ce vor fi procesate
data = standardization(data)
print("ce voi introduce:")
print(data[-1])
t1 = Tree(data[:1000])
t1.Train()
print("besturile:")
print(t1.best)
print("rez")
print(t1.Choice_recursiv(data[-1], 0))
index_prima_frauda = numpy.argmax(data[:, -1] == 1)
print(t1.Choice_recursiv(data[index_prima_frauda], 0))


