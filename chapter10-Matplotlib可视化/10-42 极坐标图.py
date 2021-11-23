# !/usr/bin/python
# -*- coding: UTF-8 -*-
import matplotlib.pyplot as plt
import numpy as np

data = np.arange(0, 100, 10)
print(data)
ax = plt.subplot(111, projection="polar")
xlable =["S1", "S2", "S3", "S4", "S5", "S6", "S7", "8"]
ax.set_xticklabels(xlable)
ax.plot(data, data, "-.", lw=2)
plt.show()


