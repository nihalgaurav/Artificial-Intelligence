# understanding the data with visualizatiion

# a.> Univariate plots
# in this section we will look at three techniques
# that you can use  to understand each attribute of
# your dataset indenpendently.
    # 1. univariate histogram plots.
    # 2. univarite density plots.
    # 3. univariate box and whisker plots.

# 1.> example of univariate histogram plots:-
# a fast way to get an idea of the distribution
# of each attribute is to look at the histograms,

# histogram groups dataa into bins and provide you
# a count of the number of observation in each bin

# from the shape of the bin you can quickly get a feeling for
# whether an attribute is gaussian, skewed or even has an exponential distribution

# code :-
# from matplotlib import pyplot as plt
# import pandas
#
# filename = 'indians-diabetes.data.csv'
# hnames = ['preg','plas','pres','skin','test','mass','pedi','age','class']
# df = pandas.read_csv(filename, names=hnames)
# print(type(df))
# df.hist()
# plt.show()


# 2.> example of univariate density plot :-

# density plot are another way to getting a quick idea of the distribution of each attribute
# the plot looks like a abstract histogram with a smooth curve drawn through
# the top of each bin, much like your eye tried to do with the histograms.


# code :-
from matplotlib import pyplot as plt
import pandas

filename = 'indians-diabetes.data.csv'
hnames = ['preg','plas','pres','skin','test','mass','pedi','age','class']
df = pandas.read_csv(filename, names=hnames)

df.plot(kind = 'density', subplots = True, layout = (3,3), sharex = False)
plt.show()
