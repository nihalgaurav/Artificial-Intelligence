import warnings
warnings.filterwarnings(action="ignore")

import pandas
import urllib.request

hname = ['sepal-length','sepal-width','petal-lenght','petal-width','class']

webpath = urllib.request.urlopen("https://goo.gl/QnHW4g")

dataframe = pandas.read_csv(webpath, names= hname)

# print(dataframe.shape)
# print(dataframe)
# print(dataframe.columns)

# peak your data
# review the first 20 rows of your data using head()
# function on the pandas dataframe
print(dataframe.head())
#head, tail(def = 5 lines), sample
print("-*-" * 20 )

# dimention of the dataframe
print("Dataframe shape : ", dataframe.shape)
print("-*-" * 20 )

# data type for each attributes
print(dataframe.dtypes)
print("-*-" * 20 )

# discriptive statistics
# pandas.set_option('display.width',1000)
pandas.set_option('precision',2)


print("description = \n", dataframe.describe())
print("description = \n", dataframe.describe(include='all'))
print("-*-" * 20 )

# class distribution
print()

class_counts = dataframe.groupby('class').size()
print(class_counts)
print("-*-" * 20 )

# correlation between attributes
# correlation refers to the relation between two variables
# and how the may or may not change together

correlation = dataframe.corr(method= 'pearson')