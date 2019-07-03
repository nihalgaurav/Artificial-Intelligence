import numpy as np

print("-" * 90)

ddarr = np.array([[1,2,3],[4,5,6]])
print("ddarr.ndim = ", ddarr.ndim)
print("ddarr.nshape = ", ddarr.shape)
print("ddarr.size = ", ddarr.size)
print("ddarr.ndtype = ", ddarr.dtype)
print(ddarr)

print("*"*90)

print("ddarr[0,1]", ddarr[0,1])
print("ddarr[0]", ddarr[0])
print("ddarr[ : , 0 ] = ", ddarr[: , 0])
print("ddarr[ 1 , :] = ", ddarr[ 1 , : ])


