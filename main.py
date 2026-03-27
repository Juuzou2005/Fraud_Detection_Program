import numpy
import csv_extraction.reading_data as reading
from analize_data.Comparing_data import DataComparing

data = reading.data_set(r"F:\practica\data_set\creditcard.csv") #add dataset path here
print(data)
observ = DataComparing(data)
observ.RepFraudNormal()



