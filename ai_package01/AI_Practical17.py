import numpy as np
arr  = np.array([[11,22,33,0.,44,55]])

print("arr.sum() = ", arr.sum())
print("arr.std() = ", arr.std())
print("arr.mean() = ", arr.mean())
print("arr.max() = ", arr.max())
print("arr.min() = ", arr.min())
print("arr.size : ", arr.size)

# following line will print

print("arr.nonzero() = ",arr.nonzero())
print("arr.dtype = ", arr.dtype)
# are all elment is zero
print(np.all([1,2,3,4]))
print(np.all([1,2,0,3,4]))

# is any element is zero
print(np.any([1,2,3,4]))
print(np.any([1,2,0,3,4]))
print(np.any([0,0,0.,0]))
print(np.any([0,0,0.,0,1]))


