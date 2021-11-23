# !/usr/bin/python
# -*- coding: UTF-8 -*-

import matplotlib.pyplot as plt
import seaborn as sns

sns.set()
tips = sns.load_dataset("tips")
print(tips.columns)
'''
普通散点图
'''
#sns.relplot(x="total_bill", y="tip", data=tips)
'''
根据分类着色
'''
#sns.relplot(x="total_bill", y="tip", hue="smoker", data=tips)
'''
调整点的形状
'''
#sns.relplot(x="total_bill", y="tip", hue="smoker", style="smoker", data=tips)

#sns.relplot(x="total_bill", y="tip", hue="smoker", style="time", data=tips)
'''
调整大小差异
'''
sns.relplot(x="total_bill", y="tip", hue="smoker", size="size", sizes=(15, 200), data=tips)
plt.show()
