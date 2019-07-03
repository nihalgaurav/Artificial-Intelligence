# Basic Reductions
# --------------------------------------
# computing sum

import numpy as np

x = np.array([1, 2, 3, 4])
print("np.sum(x) : ", np.sum(x))  # external node
print("x.sum() : ", x.sum())  # internal mode


print("sum by row and by column ", "-" * 40)

x = np.array([[1, 2], [3, 4]])

print(" x = \n", x)

print(x.sum())

print(x.sum(axis=0))  # column's sum

print(x[:, 0].sum(), x[:, 1].sum())

print("\n", x.sum(axis=1))  # row's sum

print(x[0,:].sum(), x[1,:].sum())


print(" extrema ", "-"* 50)
x = np.array([1, 3, 2])
print(x.min())  # 1
print(x.max())  # 3


# logical operator

print(np.all([True, True, False]))
print(np.any([True, True, False]))

print(" numpy can be used for array comprehension :", "-" * 50)

a = np.zeros([10, 10])
print(" a = \n", a)
print(np.any(a != 0))  # False external
print(np.all(a == a))  # True external
print((a != 0).any())  # False internal
print((a == a).all())  # True internal


a = np.array([1, 2, 3, 2])
b = np.array([2, 2, 3, 2])
c = np.array([6, 4, 4, 5])
print(((a<=b) & (b <= c)).all())  # True

print("--------------  statistics :","-"* 40)
x = np.array([1, 2, 3, 1, 1])

print("x.mean() : ", x.mean())
print("np.median(x) : ", np.median(x))
print("x.std() : ", x.std())

