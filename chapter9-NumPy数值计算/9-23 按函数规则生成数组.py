import numpy as np

dt = np.fromfunction(lambda i, j: i + j, (4, 5), dtype=int)
print("按函数规则创建数组：")
print(dt)


