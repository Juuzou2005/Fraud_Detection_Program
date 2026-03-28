import numpy
import csv_extraction.reading_data as reading
from analize_data.Comparing_data import DataComparing

data = reading.data_set(r"F:\practica\data_set\creditcard.csv") #add dataset path here
#print(data)
#observarea datelor prin grafice
# observ = DataComparing(data)
# observ.RepFraudNormal()
# observ.BoxPLot()
# observ.ScaterPlot()

x= [numpy.min(data[:, i]) for i in range(1, 27)]
print(x)



