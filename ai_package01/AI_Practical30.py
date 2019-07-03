import warnings
warnings.filterwarnings(action='ignore')

import matplotlib.pyplot as plt

plt.figure(1)  # plotting on figure 1

plt.subplot(311)  # 311 :- 3 rows 1 col and 1st part
plt.plot([1, 2, 3])

plt.subplot(312)  # 312 :- 3 rows 1 col and 2nd part
plt.plot([4, 5, 6])

plt.subplot(313)  # 313 :- 3 rows 1 col and 3rd part
plt.plot([5, 6, 7])

plt.figure(2)  # now plotting on figure 2
plt.plot([11, 12, 13])

plt.figure(1)  # again plotting on figure 1
plt.subplot(311)
plt.title('easy as 1, 2, 3 ')


plt.show()
