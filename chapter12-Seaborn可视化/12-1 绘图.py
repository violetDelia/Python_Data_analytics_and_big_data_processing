# !/usr/bin/python
# -*- coding: UTF-8 -*-

import matplotlib.pyplot as plt
import seaborn as sns

sns.set()
tips = sns.load_dataset("tips")
print(tips)
print(tips.info)
print(type(tips))
'''
relplot

'''
sns.relplot(x="total_bill", y="tip", col="time", hue="smoker",
            style="smoker", size="size", data=tips)

plt.show()


