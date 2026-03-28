import numpy
import csv_extraction.reading_data as reading
from analize_data.Comparing_data import DataComparing
from csv_extraction.convert import standardization
data = reading.data_set(r"F:\practica\data_set\creditcard.csv") #add dataset path here
#print(data)
#observarea datelor prin grafice
# observ = DataComparing(data)
# observ.RepFraudNormal()
# observ.BoxPLot()
# observ.ScaterPlot()

#aducem datele in valori ce vor fi procesate
data = standardization(data)



