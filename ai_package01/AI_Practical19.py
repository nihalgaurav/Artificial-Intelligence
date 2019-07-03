import numpy as np
n4 = np.array([10,-1,0,90,300,3,-6,2])

print(n4)
n4.sort() # in place sorting
print("after n4.sort() = ", n4)

n4 = np.array([10,-1,0,90,300,3,-6,2])

print("n4 = ", n4)
print("\nn4.argsort() = ", n4.argsort())
print("\nn4 = ", n4,"\n")

for i in n4.argsort() :
    print( n4[[i]], end=" ")

print('\n', n4[ n4.argsort()])
print("\nn4 = ", n4)

na = np.array([ [1,2,3],
                [4,5,6]])

print("na = \n", na)
print("na.transpose() = \n",na.transpose())
print("na = ", na)

print("np.eye = \n", np.eye(6))

a= np.ones([3,3])
a = a * 3
a[2,2] = 4
i = np.eye(3)
b = np.dot(a,i)

print(a,"\n")
print(i,"\n")
print(b,"\n")

na = np.array([[1,2],
              [5,6]])

print("na = \n ", na)
print("-" * 50)
print("np.dot(na , na) = \n", np.dot(na, na))
print("na * na = \n",na * na)

a = np.array([1, 2, 3, 4])
b = np.array([4, 2, 2, 4])
print(" a == b : ", a==b)
print("a > b : ", a > b)

print("array wise comparision ", "-" * 30)

a = np.array([1,2,3,4])
b = np.array([4,2,2,4])
c = np.array([1,2,3,4])
print(np.array_equal(a, b))
print(np.array_equal(a, c))

print("-"* 30,"logical operation :", "-"*30)

a= np.array([1,1,0,0], dtype=bool)
b = np.array([1,0,1,0], dtype=bool)

print("a = ", a)
print("b = ", b)

print("\nnp.logical_or(a, b) : ",np.logical_or(a, b))
print("\nnp.logical_and(a, b) : ",np.logical_and(a, b))

print(np.pi)

print("\nnp.linspace(-5, 5, 11) : \n",np.linspace(-5, 5, 11))

print("\nnp.linspace(-np.pi, np.pi, 256) : \n",np.linspace(-np.pi, np.pi, 256))

# assignment

j = np.arange(5)
print(2 **(j +1) - j)
