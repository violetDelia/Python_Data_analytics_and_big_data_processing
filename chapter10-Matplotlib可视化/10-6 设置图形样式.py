import matplotlib.pyplot as plt

data_x = [1, 2, 3, 4, 5]
data_y = [3, 5, 4, 7, 10]

plt.ylabel("数字序列", fontproperties="SimHei")
plt.plot(data_x, data_y,'ro')
plt.axis([0, 10, 2, 12])
plt.show()


