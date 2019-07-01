list1 = [1,2,3]

print("list1 * 4 = ", list1 * 4)

import numpy as np

nparr = np.array(list1)

print(nparr)

print("nparr * 4 = ", nparr * 4)
print("nparr + 4 = ", nparr + 4)

print("nparr / 2 = ", nparr/2)
print("nparr / 2.0 = ", nparr/2.0)

print("nparr // 2.0 = ", nparr//2.0)
print("nparr // 2 = ", nparr//2)

a = 10
print(type(a))

a = 12.5
print(type(a))

print(type(nparr))
print("nparr.dtype = ", nparr.dtype)

print("nparr.size = ", nparr.size)

# list1 * 4 =  [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]
# [1 2 3]
# nparr * 4 =  [ 4  8 12]
# nparr + 4 =  [5 6 7]
# nparr / 2 =  [0.5 1.  1.5]
# nparr / 2.0 =  [0.5 1.  1.5]
# nparr // 2.0 =  [0. 1. 1.]
# nparr // 2 =  [0 1 1]
# <class 'int'>
# <class 'float'>
# <class 'numpy.ndarray'> #numpy n dimensional array
# nparr.dtype =  int32
