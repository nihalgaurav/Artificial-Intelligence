import matplotlib.pyplot as plt

# if you make multiple lines with one plot command,
# the kwargs apply to all
# those lines , eg. :

x1 = [1, 2, 3]
y1 = [1, 2, 3]
x2 = [1, 2, 3]
y2 = [1, 4, 9]

plt.plot(x1, y1, x2, y2, linewidth = 3)
plt.show()