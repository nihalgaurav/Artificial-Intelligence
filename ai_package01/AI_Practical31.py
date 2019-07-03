import matplotlib.pyplot as plt
import  numpy as np

# plotting with default setting
x = np.linspace(-np.pi, np.pi, 256, endpoint=True)
print("x= ", x)

s = np.sin(x)  # sin0 = 0 and sin90 = 1
c = np.cos(x)  # cos0 = 1 and cos90 = 0

plt.plot(x, s)
plt.plot(x, c)
#plt.plot(x, x*0)

plt.show()
