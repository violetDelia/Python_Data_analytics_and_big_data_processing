import numpy as np

a = np.arange(8).reshape(2, 4)
print("原始数组a:")
print(a)

b = a > 4
print("新的布尔数组b：")
print(b)

print("使用布尔数组进行筛选：")
print(a[b])
