from sklearn.preprocessing import Binarizer
from pandas import read_csv
from numpy import set_printoptions

filename = 'indians-diabetes.data.csv'

hnames = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
dataframe = read_csv(filename, names= hnames)
array = dataframe.values

x = array[:, 0:8]
y = array[:, 8]

binarizer = Binarizer(threshold=6)
binarizedX = binarizer.fit_transform(x)

set_printoptions(precision=2)
print(binarizedX[0:30, :])
