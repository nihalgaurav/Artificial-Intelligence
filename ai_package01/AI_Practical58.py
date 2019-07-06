from pandas import read_csv
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression



filename = "housing.csv"

hnames = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'b', 'LSTAT', 'MDEV']

dataframe = read_csv(filename, names=hnames)
array = dataframe.values

x = array[:, 0:13]
y = array[:, 13]


kfold = KFold(n_splits=10, random_state=7)
mmodel = LinearRegression()

# scoringmethod = 'neg_mean_absolute_error'
# scoringmethod = 'neg_mean_squared_error'
scoringmethod = 'r2'

results = cross_val_score(mmodel, x, y, cv=kfold, scoring=scoringmethod)
print(results)

print('MAE : %.3f (%.3f)' % (results.mean(), results.std()))


