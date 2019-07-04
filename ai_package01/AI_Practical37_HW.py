import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import urllib.request


webpath = urllib.request.urlopen("https://goo.gl/QnHW4g")
hname = ['sepal-length','sepal-width','petal-lenght','petal-width','class']
dataframe = pd.read_csv(webpath, names=hname, sep=',')

#print(df1)
# print(dataframe)
# print(dataframe.columns)
# print(dataframe.shape)
# print(dataframe.head())
# print(dataframe.dtypes)

pd.set_option('precision', 2)

# print(dataframe.describe())
# print(dataframe.describe(include='all'))
print(type(dataframe))

class_counts = dataframe.groupby('class').size()
print(class_counts)

correlation = dataframe.corr()
print(correlation)

dataframe.plot(kind='density', subplots=True, layout=(2, 2), sharex=False)
dataframe.hist()
dataframe.plot(kind='box', subplots=True, layout=(2, 2), sharex=True)

fig = plt.figure()
print(type(fig))
subfig = fig.add_subplot(111)
print(type(subfig))

cax = subfig.matshow(correlation, vmin=-1, vmax=1)
print(type(cax))

fig.colorbar(cax)

ticks = np.arange(0, 5)
subfig.set_xticks(ticks)
subfig.set_yticks(ticks)
subfig.set_xticklabels(hname)
subfig.set_yticklabels(hname)


arr1 = np.array(dataframe)
for i in range(len(arr1)):
    if arr1[i,4] == 'Iris-setosa':
        arr1[i, 4] = 1
    elif arr1[i,4] == 'Iris-versicolor':
        arr1[i, 4] = 2
    elif arr1[i,4] == 'Iris-virginica':
        arr1[i, 4] = 3
    else:
        arr1[i, 4] = 4

print(arr1.ndim)
print(arr1.shape)
print(arr1.size)
print(arr1.dtype)
print(np.zeros([4,3]))
print(np.ones([4,3]))
print(arr1.sum())
print(arr1.mean())
print(arr1.std())
print(arr1.max())
print(arr1.min())
print(np.all(arr1))
print(np.any(arr1))
print(arr1.argsort())
print(arr1.transpose())
print(np.eye(6))
# np.dot(), np.array_equal(a, b), np.logical_or(a, b), np.logical_and(a, b)
print(np.linspace(5, 10, 20))
a = np.arange(1, 10)
print(np.sin(a))
print(np.log(a))
print(np.exp(a))
print(np.sum(arr1, axis=0))
print(np.sum(arr1, axis=1))

plt.figure(4)
plt.subplot(211)
plt.plot([1, 2, 3, 4, 5], [1, 2, 3, 4, 5],
         "go-", label = 'line2', linewidth = 2)
plt.subplot(212)
plt.plot([1, 2, 3, 4, 5], [1, 4, 9, 16, 25],
         "rs--", label = 'line2', linewidth = 4)

plt.axis([0, 6, 0, 26])
plt.legend()

x = [2, 3, 4, 5, 6, 7]
y = [4, 9, 16, 25, 36, 49]
plt.figure(5)
plt.plot(x, y, marker = 'o', markerfacecolor = 'red',
         markersize = 15, linestyle = 'dashed', color = 'blue')
plt.title("numbers with square values")
plt.xlabel("------numbers--------->", fontsize = 14, color = 'red')
plt.ylabel('----square-->', fontsize = 14, color = 'blue')

plt.figure(6)
t = np.arange(0.0, 5.0,0.2)
plt.plot(t, t, 'r*-', t, t+3, 'bs-', t, t+6, 'r-',t, t+6, 'yo' , markersize = 5)

plt.figure(7)
x = np.linspace(-np.pi, np.pi, 256, endpoint=True)

s = np.sin(x)  # sin0 = 0 and sin90 = 1
c = np.cos(x)  # cos0 = 1 and cos90 = 0

plt.plot(x, s)
plt.plot(x, c)

plt.show()

