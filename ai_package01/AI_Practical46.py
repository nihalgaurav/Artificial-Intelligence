import pandas as pd
from numpy import set_printoptions

from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
import warnings
warnings.filterwarnings("ignore")

filename = 'indians-diabetes.data.csv'

hnames = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
dataframe = pd.read_csv(filename, names= hnames)
array = dataframe.values

x = array[:, 0:8]
y = array[:, 8]

# feature extraction
test = SelectKBest(score_func=chi2, k=4)
fit = test.fit(x, y)

# summarized score
set_printoptions(precision=3)
print(fit.scores_)
features = fit.transform(x)

# summarize selected features
print('\n\n')
print(features[0:20, :])








