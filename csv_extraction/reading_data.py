import numpy as np
import csv
#data will contain
#moment of tranzaction
#personal data that are encoded in numbers(city, bank, country etc..)
#amount tranzactioned
#if the value is or not a fraud
def data_set(file_name):
    with open(file_name, newline="") as file:
        read = csv.reader(file)
        next(read)

        data_list = []
        for row in read:
            val_row = [float(val) for val in row]
            data_list.append(val_row)

        data_list.append(val_row)
        return np.array(data_list)

