import numpy as np

dt = np.dtype(np.int32)
print("创建整形类型:", dt)
dt = np.dtype(np.float64)
print("创建浮点类型:", dt)
dt = np.dtype(np.bool_)
print("创建布尔类型:", dt)
dt = np.dtype(np.complex128)
print("创建复数类型:", dt)
dt = np.dtype([("2018", np.str_), ("GDP", np.float64)])
print("创建自定义类型:", dt)


