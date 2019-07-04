import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.feature_selection import RFE
import warnings
warnings.filterwarnings("ignore")

filename = 'indians-diabetes.data.csv'

hnames = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
dataframe = pd.read_csv(filename, names= hnames)
array = dataframe.values

x = array[:, 0:8]
y = array[:, 8]

model = LogisticRegression()
rfe = RFE(model, 4)
fit = rfe.fit(x, y)
result = fit.transform(x)

print("num Features : ", fit.n_features_)
print("Selected features : ", fit.support_)
print("feature Ranking : ", fit.ranking_)
print("\n\n\n", result[:20, :])



