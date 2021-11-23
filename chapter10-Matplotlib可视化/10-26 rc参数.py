# !/usr/bin/python
# -*- coding: UTF-8 -*-

import matplotlib.pyplot as plt
import numpy as np
from sympy.physics.quantum.tests.test_circuitplot import mpl

'''
设置rc参数动态修改图形样式
'''
mpl.rcParams['lines.linewidth'] = 2
mpl.rcParams['lines.color'] = 'r'
plt.plot(np.sin(np.arange(0, 10)), 'b-.')
plt.show()
