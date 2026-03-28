import numpy
#make data smaller for processing
def standardization(data):
    standard_deviations = numpy.std(data, axis = 0)
    means = numpy.average(data, axis = 0)
    populatie = data.copy()
    for i in range(len(data[0])):
        populatie[:, i] = (data[:, i] - means[i])/standard_deviations[i]
    return populatie

