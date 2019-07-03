import matplotlib.pyplot as plt

import numpy as np

# evenly sample times at 200ms interval

t = np.arange(0.0, 5.0,0.2)
print(t)

# red dashes , blue squares and green triangles
#plt.plot(t, t, 'r*-', t, t+3, 'bs-', t, t+6, 'ro-', markerfacecolor='green', markersize = 5)
plt.plot(t, t, 'r*-', t, t+3, 'bs-', t, t+6, 'r-',t, t+6, 'yo' , markersize = 5)

plt.show()

