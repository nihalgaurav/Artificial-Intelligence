import numpy as np

d1 = np.array([[1,2],
               [3,4],
               [5,6],
               [7,8],
               [9,10],
               [11,12],
               [13,15] ])

print(d1)
print(d1.shape)
print(d1.ndim)

# entire expression before "," is for rows

print("d1[: :3, 0] = ", d1[1: :3, 0])
print("d1[: :2] = ",d1[: :2] )

print( d1[1: :2 , 1])