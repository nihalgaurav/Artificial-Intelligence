import matplotlib.pyplot as plt

labels = ['s1', 's2', 's3']
section = [300, 510, 250]
color = ['c', 'g', 'y']

plt.pie(section, labels=labels, colors=color, startangle=45, explode=(0, 0, 0.1), autopct='%2.2f%%')

# plt.axis('equal")  # try commenting this out
plt.title('pie chart example')
plt.show()


