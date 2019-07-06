import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import pickle
import warnings
warnings.filterwarnings("ignore")


filename = 'indians-diabetes.data.csv'
hnames = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
dataframe = pd.read_csv(filename, names= hnames)
array = dataframe.values

x = array[:, 0:8]
y = array[:, 8]

test_size = 0.33
seed = 7
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=test_size,
                                                    random_state=seed)
model = LogisticRegression()
model.fit(x_train, y_train)

filename = 'finalized_model.sav'
pickle.dump(model, open(filename, 'wb'))
print("model dumped successfully into a file by pickle ........\n..\n...\n..")

print("_"*30,"\n\n\n")
print("some time later...")
print("\n\n\n________________________________----")


loaded_model = pickle.load(open(filename, "rb"))
print("model loaded successfully from file by pickel..")
result = loaded_model.score(x_test, y_test)
print("accuracy result : ", result)






