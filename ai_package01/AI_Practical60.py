import  warnings
warnings.filterwarnings(action='ignore')


import pandas as pd
from sklearn.model_selection import KFold
from sklearn.model_selection import  cross_val_score

filename = 'indians-diabetes.data.csv'
headingName = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
dataframe = pd.read_csv(filename, names= headingName)
array = dataframe.values

x = array[:, 0:8]
y = array[:, 8]

kfold = KFold(n_splits=10, random_state=7)


# 1.> spot checking for Logistic Regression
# -------------------------------------------------------------------------
from sklearn.linear_model import LogisticRegression
model = LogisticRegression()
result = cross_val_score(model, x, y, cv=kfold)
print("validation Score for LogisticRegression : ",result.mean())


# 2.> spot checking for Linear Discriminant Analysis(LDA)
# ---------------------------------------------------------------------------
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
model = LinearDiscriminantAnalysis()
result = cross_val_score(model, x, y, cv=kfold)
print("validation Score for LinearDiscriminantAnalysis: ",result.mean())


# 3.> spot checking for Linear K-Nearest Neighbor (KNN)
# ---------------------------------------------------------------------------
from sklearn.neighbors import KNeighborsClassifier
model = KNeighborsClassifier()
result = cross_val_score(model, x, y, cv=kfold)
print("validation Score for K-Nearest Neighbor (KNN): ",result.mean())


# 4.> spot checking for Gaussian Naive Bayes
# ---------------------------------------------------------------------------
from sklearn.naive_bayes import GaussianNB
model = GaussianNB()
result = cross_val_score(model, x, y, cv=kfold)
print("validation Score for GaussianNB: ",result.mean())


# 5.> spot checking for Decision Tree Classifier(CART)
# ---------------------------------------------------------------------------
from sklearn.tree import DecisionTreeClassifier
model = DecisionTreeClassifier()
result = cross_val_score(model, x, y, cv=kfold)
print("validation Score for DecisionTreeClassifier: ",result.mean())


# 5.> spot checking for Support Vector(SVC)
# ---------------------------------------------------------------------------
from sklearn.svm import SVC
model = SVC()
result = cross_val_score(model, x, y, cv=kfold)
print("validation Score for SVM: ",result.mean())


