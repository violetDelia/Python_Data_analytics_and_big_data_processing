# !/usr/bin/python
# -*- coding: UTF-8 -*-

import matplotlib.pyplot as plt
import numpy as np

#data = np.linspace(0,10)
#plt.plot(data)
with plt.style.context(("dark_background")):
    data = np.linspace(0, 3 * np.pi)
    print (data)
    plt.plot(np.sin(data), "r-o")
    plt.show()

	
