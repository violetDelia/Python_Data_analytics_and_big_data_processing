import numpy as np
'''
用empty()生成的元素是随机产生的，若不指定类型，则随即采用一种数据类型生成随机数
'''
dt = np.empty([2, 2], dtype=int)
print(dt)
dt1 = np.empty([2, 2])
print(dt1.dtype)
print(dt1)

