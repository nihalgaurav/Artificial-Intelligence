# 3. > example of univariate box and whisker plots.
# another useful way to review the distribution of each attribute is to use box andd whisker
# plot or boxplot for short

# boxplot summerises the distribution of ach attribute
# drawing the line for the median (middle value) and the box around the
# 25thand 75th percentile ( yhe middle 75 % of the data ).
#
# the whisker gives an idea of the spread of the data and dots outside
# of the whisker shows candidate outlier values.

#( values that are 1.5 times greater than the spread of the middle 50 % of the data)

from matplotlib import pyplot as plt
import pandas
filename = 'indians-diabetes.data.csv'
hnames = ['preg','plas','pres','skin','test','mass','pedi','age','class']
df = pandas.read_csv(filename, names=hnames)

df.plot(kind = 'box', subplots = True, layout = (3,3), sharex = False)
plt.show()