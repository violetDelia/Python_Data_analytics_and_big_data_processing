import numpy as np

a = (np.sin(np.arange(12) * 10)).reshape(4, 3)
print("原始数组")
print(a)

max_val_posi = a.argmax(axis=0)
print("每个列上最大值的位置：")
print(max_val_posi)

data_max = a[max_val_posi, range(3)]
print("检索最大值，并返回新的数组：")
print(data_max)

max_val_posi_raw = a.argmax(axis=1)
print(max_val_posi_raw)
data_max_raw = a[range(4), max_val_posi_raw]
print(data_max_raw)