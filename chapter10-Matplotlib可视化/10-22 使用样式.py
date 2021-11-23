# !/usr/bin/python
# -*- coding: UTF-8 -*-

import matplotlib.pyplot as plt
import numpy as np

plt.style.use("fivethirtyeight")
data = np.random.randn(50)
plt.plot(data)
plt.show()
'''
可用样式列表
'''
print(plt.style.available)


