# !/usr/bin/python
# -*- coding: UTF-8 -*-

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

sns.set()
df = pd.DataFrame(dict(time=pd.date_range("2019-1-1", periods=500),
                       value=np.random.randn(500).cumsum()))
g = sns.relplot(x="time", y="value", kind="line", data=df)
'''
调整x轴的角度
'''
g.fig.autofmt_xdate()
plt.show()


