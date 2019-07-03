import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
plt.plot([1, 2, 3, 4], list(a**2 for a in x))
plt.xlabel("-------some numbers-------->")
plt.ylabel("-------squared value------->")
plt.show()

