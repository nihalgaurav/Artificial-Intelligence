import urllib.request
import numpy

web_path = urllib.request.urlopen("https://goo.gl/QnHW4g")
dataset = numpy.genfromtxt(web_path, delimiter = ',')

for l in dataset:
    print(l)

print("set of Data from url : ", dataset.shape )
