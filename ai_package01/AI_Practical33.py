import matplotlib.pyplot as plt
import  numpy as np

# use numpy to generate bunch of random data

n = 5 + np.random.randn(1000)

print("n = ",  n)

# m for m in range(len(n))

m = list(range(len(n)))

print("m =  ", m)

plt.bar(m, n)

plt.title(" Raw data")
plt.show()

plt.hist(n, bins=200)
plt.title("histogram")
plt.show()

