# 2.> scatter matrix plot

# A scatter plot shows the relation between two variables
# as dots in two dimensions , one axis for each attribute.
# You can create a scatter plot for each pair of attributes in your data.
# Drawing all these scatter together is called scatter plot matrix.
# scatter plots are useful for spotting structured relationships
# between variables, like whether you could summerize the reelationship between two variable with a line.


from matplotlib import pyplot as plt

from pandas import read_csv

# import pandas

from pandas.plotting import scatter_matrix

import warnings
warnings.filterwarnings(action="ignore")

hnames = ['preg','plas','pres','skin','test','mass','pedi','age','class']
dataframe = read_csv('indians-diabetes.data.csv', names= hnames)

scatter_matrix(dataframe)
plt.show()
