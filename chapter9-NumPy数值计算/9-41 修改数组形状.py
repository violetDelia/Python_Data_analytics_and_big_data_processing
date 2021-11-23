import numpy as np

a = np.floor(10 * np.random.random((4, 5)))
print("原始数组形状：", a.shape)

b = a.ravel()
print("将多维数组转为一维数组", b, "新数组的形状：", b.shape)
print(b)

print("将数组修改为指定形状：")
c = a.reshape(2, 10)
print("新数组形状为：", c.shape)

d = a.T
print("对数组进行行列转换（矩阵转置）：", d.shape)


