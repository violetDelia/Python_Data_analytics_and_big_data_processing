import numpy as np

a = np.arange(8).reshape(2, 4)
print(a)
b1 = np.array([False, True])
b2 = np.array([True, False, True, False])
print("选取第一维的第2行所有列")
print(a[b1, :])
print("选取第一维的第2行，第二维的第1,3列")
print(a[b1, b2])




