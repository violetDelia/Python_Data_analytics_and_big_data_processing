# !/usr/bin/python
# -*- coding: UTF-8 -*-

import matplotlib.pyplot as plt

group_name = ["A", "B", "C", "D", "E"]
values = [1, 20, 30, 40, 50]

plt.figure(1, figsize=(10, 5))
'''
235 表示二行三列的第五个
'''
plt.subplot(234)
plt.bar(group_name, values)
plt.subplot(235)
plt.scatter(group_name, values)
plt.subplot(232)
plt.plot(group_name, values)
plt.suptitle("分组绘制", fontproperties="SimHei")
plt.show()


