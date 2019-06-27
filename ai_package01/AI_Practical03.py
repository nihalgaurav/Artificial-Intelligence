import numpy
filename = 'indian-diabities.data.csv'
raw_data = open(filename, 'r')
data = numpy.loadtext(raw_data, delimiter = ',')

print("numpy loadtext : ", data.shape)
raw_data.close()