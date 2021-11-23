import matplotlib.pyplot as plt

'''
传入的数组会转换为NumPy的数组
'''
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
plt.plot(data)
'''
fontproperties="SimHei"才能显示中文
'''
plt.ylabel("数字序列", fontproperties="SimHei")
plt.show()

