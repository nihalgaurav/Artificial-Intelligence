from copy import deepcopy
import  numpy as np
import  pandas as pd
from  matplotlib import pyplot as plt
import warnings
warnings.filterwarnings(action='ignore')

# plt.style.use('ggplot')

# importing the dataset
data = pd.read_csv('KMeansData.csv')
print("input data and shape : ", data.shape)
print(data.head())

# getting the value and plotting it
f1 = data['V1'].values
f2 = data['V2'].values

plt.scatter(f1, f2, c='black', s=10)
plt.show()


x = np.array(list(zip(f1, f2)))
# [[2.072345,-3.241693], [], []

# Euclidean Distance Calculator
def eu_dist(a, b, ax=1):
    return np.linalg.norm(a-b, axis=ax)

# number of clusters
k = 3
# x cordinates of random centroides

c_x = np.random.randint(0, np.max(x)-20, size=k)
print("C_x : ", c_x)

# Y cordinate of random centroide
c_y = np.random.randint(0, np.max(x)-20, size=k)
print("C_Y : ", c_y)


C = np.array(list(zip(c_x, c_y)), dtype=np.float32)
print("initial centroide (random Position) : ", C)
print(C.shape)

# plotting along with centroide
plt.scatter(f1, f2, s=10, c='k')
plt.scatter(c_x, c_y, marker='*', s=300, c='r')
plt.show()



# to store the value of centroid when its updated
c_old = np.zeros(C.shape)
print("C = ", C)
print("C_old : ", c_old)
print("len(x) : ", len(x))


# cluster label(0,1,2)
clusters = np.zeros(len(x))

# zeroes filled numpy array of 3000 elements
print("clusters : ", clusters)

# error fun. - Distance between new centroids and old centroids
error = eu_dist(C, c_old, None)
print('error : ', error, error.shape,type(error))
# loop will run till an error become zero
while error.all():
    # assigning each value to its closet cluster
    for i in range(len(x)):
        distances = eu_dist(x[i], C)
        cluster = np.argmin(distances)
        clusters[i] = cluster
    # storing the old centroide value
    c_old = deepcopy(C)
    # finding the new centroide by taking the averaage value
    for i in range(k):
        points = [x[j] for j in range(len(x)) if clusters[j] == i]
        C[i] = np.mean(points, axis=0)
    error = eu_dist(C, c_old)

colors = ['b', 'c', 'r']
fig, ax = plt.subplots()
for i in range(k):
    points = np.array([x[j] for j in range(len(x)) if clusters[j] == i])
    print(points)
    ax.scatter(points[:, 0], points[:, 1], s=25, c=colors[i])

ax.scatter(C[:, 0], C[:, 1], marker='*', s=100, c='y')
print(" final centroid : ", C)
plt.show()

# now by core machine learning
from sklearn.cluster import  KMeans
print("mean of cluster")
kmean = KMeans(n_clusters=3)

data = pd.read_csv('KMeansData.csv')

f1 = data['V1'].values
f2 = data["V2"].values

x = np.array(list(zip(f1, f2)))

# fitting the input data
kmean =kmean.fit(x)

# getting the cluster label
labels = kmean.predict(x)
print("labels : ", labels)
print("labels : ", labels)
centroid = kmean.cluster_centers_

# centroid value
print(" kmeans algo centroid values :- \n")
print("KMeanss : manual centroid : \n", C)
print("kmeans sklearn:centroid : \n", centroid)
