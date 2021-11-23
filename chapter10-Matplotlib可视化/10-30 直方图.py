# !/usr/bin/python
# -*- coding: UTF-8 -*-
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams["font.sans-serif"] = ["SimHei"]

data = np.array([0, 1, 1, 2, 2,
                 2, 2, 3, 3, 3,
                 3, 3, 4, 4, 4,
                 4, 6, 6, 6, 10])
'''
bins    条形的个数
color   条形的颜色
edgecolor   条形边缘颜色
alpha   透明度
'''
plt.hist(data, bins=10, color="red", edgecolor="black", alpha=1)
plt.xlabel("范围")
plt.ylabel("频数或者频率")
plt.title("直方图")
plt.show()


