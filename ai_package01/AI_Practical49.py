import pandas as pd
from sklearn.ensemble import ExtraTreesClassifier
import warnings
warnings.filterwarnings("ignore")

filename = 'indians-diabetes.data.csv'

hnames = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
dataframe = pd.read_csv(filename, names= hnames)
array = dataframe.values

x = array[:, 0:8]
y = array[:, 8]

model = ExtraTreesClassifier()

fit = model.fit(x, y)
scores = model.feature_importances_
print(scores)

result = list(zip(hnames, scores))
print('\n result \n\n', result)

#print("explained variance ration :%s" %fit.explained_variance_ratio_)

from operator import itemgetter
print(sorted(result, key=itemgetter(1), reverse=True))

