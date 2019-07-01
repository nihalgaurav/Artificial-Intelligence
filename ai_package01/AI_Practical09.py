# 1.> example of univariate histogram plots:-
# a fast way to get an idea of the distribution
# of each attribute is to look at the histograms,

# histogram groups dataa into bins and provide you
# a count of the number of observation in each bin

# from the shape of the bin you can quickly get a feeling for
# whether an attribute is gaussian, skewed or even has an exponential distribution

import warnings
warnings.filterwarnings(action="ignore")

from matplotlib import pyplot as plt
import pandas
import urllib.request

hname = ['sepal-length','sepal-width','petal-lenght','petal-width','class']

webpath = urllib.request.urlopen("https://goo.gl/QnHW4g")

dataframe = pandas.read_csv(webpath, names= hname)

print(type(dataframe))
dataframe.hist()
plt.show()
