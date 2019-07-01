# Multi vatriate plots

# 1.> Correlation Matrix plot
# 2.> Scatter matrix plot

# correlation gives an indication of how related the change are between variables
# if two variable change in the same direction they are positively correlated .
# if they change in opposite direction together ( one goes up , one goes down ), they are negatively correlated.

# you can calculate the correlation between each pair of attributes.
# this is called correlation matrix
# you can plot the correlation matrix and get the idea of which
# variable has a high correlation with each other,

import warnings
warnings.filterwarnings(action="ignore")

# correlation matrix plot
from matplotlib import pyplot as plt
import  pandas as pd
import numpy

#pd.set_option("display.width", 2000)

hnames = ['preg','plas','pres','skin','test','mass','pedi','age','class']
dataframe = pd.read_csv('indians-diabetes.data.csv', names= hnames)
correlation= dataframe.corr()
print(correlation)

# plot correlation matrix

fig = plt.figure()
print(type(fig))

# following will add matrix and side bar in entire area
subfig = fig.add_subplot(111)
print(type(subfig))


cax = subfig.matshow(correlation, vmin = -1, vmax = 1)
print(type(cax))
fig.colorbar(cax)

# -------
ticks = numpy.arange(0,9) # it will generate value from 0 to 8
subfig.set_xticks(ticks)
subfig.set_yticks(ticks)
subfig.set_xticklabels(hnames)
subfig.set_yticklabels(hnames)

plt.show()
