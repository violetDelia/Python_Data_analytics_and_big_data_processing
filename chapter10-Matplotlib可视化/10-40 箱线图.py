# !/usr/bin/python
# -*- coding: UTF-8 -*-
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["font.sans-serif"] = ["SimHei"]

data = np.array([92, 68, 78, 69, 95, 99, 89, 72,
                 46, 34, 39, 60, 74, 85, 59, 98, 0])
plt.boxplot(data, meanline=True, notch=True)
plt.show()
'''
箱线图结构
极大值
上四分位数
中位数
下四分位数
极小值
'o'异常值
'''
