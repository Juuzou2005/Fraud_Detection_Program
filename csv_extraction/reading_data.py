import numpy as np
import csv
import pandas
#data will contain
#moment of tranzaction
#personal data that are encoded in numbers(city, bank, country etc..)
#amount tranzactioned
#if the value is or not a fraud

def data_set(file_name): #numeric dataset
    with open(file_name, newline="") as file:
        read = csv.reader(file)
        next(read)

        data_list = []
        for row in read:
            val_row = [float(val) for val in row]
            data_list.append(val_row)

        return np.array(data_list)

def better_read(file_name): #poate citi si stringuri si floaturi
    df = pandas.read_csv(file_name)
    return df
def verificareDateNull(df):
    print(df.isnull().sum())


# if __name__ == "__main__":
#     better_read(r"F:\practica\data_set\creditcard.csv")