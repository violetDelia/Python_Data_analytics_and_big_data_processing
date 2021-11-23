import numpy as np
'''
会从多维数组的第一个维度上进行取值
'''
data = np.array([[0, 0, 0, 99],
                 [168, 0, 0, 23],
                 [0, 198, 0, 78],
                 [0, 0, 23, 64],
                 [121, 0, 88, 36]])
index = np.array([[1, 2, 3, 4], [0, 2, 1, 3]])
print(data[index])


