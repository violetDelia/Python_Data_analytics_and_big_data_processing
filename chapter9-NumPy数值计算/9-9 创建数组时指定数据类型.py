import numpy as np

dt = np.array([1, 2, 3, 4, 5], dtype="f8")
print("数组：", dt)
print("数组数据类型：", dt.dtype)
dt = np.array([[1], [2]], dtype=complex)
print("数组：", dt)
print("数组数据类型：", dt.dtype)

