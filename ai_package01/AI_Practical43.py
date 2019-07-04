import pandas as pd
from numpy import set_printoptions
from sklearn.preprocessing import StandardScaler

filename = 'indians-diabetes.data.csv'

hnames = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
dataframe = pd.read_csv(filename, names= hnames)
array = dataframe.values

x = array[:, 0:8]
y = array[:, 8]

scaler = StandardScaler()

rescaledX = scaler.fit_transform(x)

set_printoptions(precision=2)
print(rescaledX[:30, :])




